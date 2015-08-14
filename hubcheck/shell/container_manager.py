from .toolsession import ToolSession
from hubcheck.exceptions import ConnectionClosedError
from hubcheck.exceptions import SessionCreateError

import logging
import pprint
import re
import hubcheck.conf


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ContainerManager(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._lookup = {
            # Example:
            # host : {
            #   username : {
            #       'sessionobj' : sessionObj,
            #       'sessions' : [ {'number' : sessionNum, 'toolname' : toolname},
            #                      {'number' : sessionNum, 'toolname' : toolname},
            #                      ... ],
            #   }
            # }
        }


    def __repr__(self):
        return "ContainerManager(%s)" % (pprint.pformat(self._lookup))


#    def __del__(self):
#
#        self.stop_all()


    def _find_session_number_for(self,host,username,toolname=None):

        self.logger.debug(
            'cm looking for session number for %s on %s with toolname %s' \
            % (username,host,toolname))

        self.logger.debug(
            'session dictionary:\n%s' \
            % (pprint.pformat(self._lookup)))

        session_obj = None
        session_number = None
        session = None

        # check if the host,user combination exists
        try:
            sessions = self._lookup[host][username]['sessions']
            session_obj = self._lookup[host][username]['sessionobj']
        except KeyError:
            return session_obj,session_number


        if len(sessions) == 0:
            session_number = None
            return session_obj,session_number

        if toolname is None:
            # return the first available session
            session_number = sessions[0]['number']
            return session_obj,session_number

        # find a session that matches the toolname
        for session in sessions:
            if session['toolname'] == toolname:
                session_number = session['number']
                break

        return session_obj,session_number


    def _create_session_number_record(self,host,username,session_number,
                                      session_obj,toolname):

        if host not in self._lookup:
            self._lookup[host] = {}

        session_number = int(session_number)

        if username not in self._lookup[host]:
            # add a new record
            self.logger.debug(
                'adding cm record for %s:%s -> %s,%s' \
                % (host,username,session_number,toolname))
            self._lookup[host][username] = {
                'sessionobj' : session_obj,
                'sessions' : [{'number':session_number,'toolname':toolname}],
            }
        else:
            # update an existing record
            self.logger.debug(
                'updating cm record for %s:%s -> %s,%s' \
                % (host,username,session_number,toolname))
            self._lookup[host][username]['sessions'].append(
                {'number':session_number,'toolname':toolname})

        self.logger.info(
            "cm user sessions: host='%s' username='%s' sessions='%s'" \
            % (host,username,self._lookup[host][username]['sessions']))


    def _delete_session_number_record(self,host,username,session_number):

        session_number = int(session_number)

        self.logger.debug(
            "removing cm session record for %s:%s -> %s" \
            % (host,username,session_number))

        # update an existing record
        for i in xrange(0,len(self._lookup[host][username]['sessions'])):
            session = self._lookup[host][username]['sessions'][i]
            if session['number'] == int(session_number):
                del self._lookup[host][username]['sessions'][i]
                break

        self.logger.info(
            "cm user sessions: host='%s' username='%s' sessions='%s'" \
            % (host,username,self._lookup[host][username]['sessions']))


    def create(self,host,username,password,session=None,title=None,toolname=None):

        self.logger.info("cm creating new session")

        if session is None:
            session = ToolSession(host=host,
                                  username=username,
                                  password=password)

        # read the configuration to find the name of the default workspace
        if toolname is None:
            toolname = hubcheck.conf.settings.default_workspace_toolname

        # create the session
        i,o,e = session.create(title,toolname)
        output = o.read(1024)
        try:
            session_number = int(re.search('(\d+)',output).group(0))
        except:
            msg = "Failed to locate session number: %s" % (output)
            raise SessionCreateError(msg)

        # enter the session
        ws = session.access(session_number=session_number)

        # store the session number
        self._create_session_number_record(host,username,session_number,session,toolname)

        return ws


    def access(self,host,username,password,toolname=None):

        ws = None

        # FIXME:
        # we should probably grab all of the open sessions
        # and loop through them, trying to connect. if we
        # get to the end, then we open a new session.

        session,session_number = self._find_session_number_for(host,username,toolname=toolname)

        if session_number is not None:
            # an open session was returned
            # open a shell in that session

            self.logger.info("cm accessing session %s" % (session_number))

            try:
                ws = session.access(session_number=session_number)
            except ConnectionClosedError as e:
                self.logger.exception(e)
                self.logger.debug("session access failed, trying to recover...")
                self.logger.debug("checking if closed")
                # accessing the session failed
                # check if the session is closed
                d = session.get_open_session_detail()
                for k,v in d.items():
                    if int(v['session_number']) == session_number:
                        # session is still listed in table
                        # probably something wrong trying to connect to it.
                        self.logger.debug("session %d appears open"
                            % (session_number))
                        raise
                # session was not in the table, it is probably closed
                # force a fall through to the next if clause
                self.logger.debug("session appears closed, open a new one")
                self._delete_session_number_record(host,username,session_number)
                session_number = None

        if session_number is None:
            # no stored open sessions for the user on this host
            # create a new session and store it

            ws = self.create(host,username,password,session,toolname=toolname)

        return ws


    def sync_open_sessions(self,host=None,username=None):

        self.logger.info("sync'ing open sessions: host = %s, username = %s"
            % (host,username))

        for key_host in self._lookup.keys():

            if (host is not None) and (key_host != host):
                continue

            for key_user in self._lookup[key_host].keys():

                if (username is not None) and (key_user != username):
                    continue

                # get the list of open session from the "session list" command
                session = self._lookup[key_host][key_user]['sessionobj']
                open_sessions_dict = session.get_open_session_detail()

                open_sessions = []
                open_session_data = {}
                for k,v in open_sessions_dict.items():
                    open_sessions.append(int(v['session_number']))
                    toolname =  re.sub('_r\d+$','',v['name'])
                    open_session_data[int(v['session_number'])] = toolname

                # figure out which sessions cm has listed as open,
                # verses the sessions listed as open by "session list"
                # closed_sessions = set(userd['sessions']) - set(open_sessions)

                stored_session_data = self._lookup[key_host][key_user]['sessions']
                stored_sessions = []
                for session in stored_session_data:
                    stored_sessions.append(session['number'])

                self.logger.debug("stored open sessions: %s" % (stored_sessions))
                self.logger.debug("session list results: %s" % (open_sessions))

                new_open_sessions = set(stored_sessions) & set(open_sessions)

                # rebuild the container manager's open session data
                self._lookup[key_host][key_user]['sessions'] = []

                for session_number in new_open_sessions:
                    self._lookup[key_host][key_user]['sessions'].append(
                        {'number':session_number,
                         'toolname':open_session_data[session_number]}
                    )

                self.logger.debug("new open sessions: %s"
                    % (self._lookup[key_host][key_user]['sessions']))



    def stop(self,host,username,session_number):
        """
        stop a session container
        """

        self.logger.info("cm stopping session %s" % (session_number))

        session = self._lookup[host][username]['sessionobj']

        # check if the session is open
        is_session_open = False
        open_sessions_dict = session.get_open_session_detail()
        for k,v in open_sessions_dict.items():
            if int(v['session_number']) == int(session_number):
                is_session_open = True
                break

        if is_session_open is False:
            self.logger.info("session %s is not listed as open" % (session_number))
            try:
                self._delete_session_number_record(host,username,session_number)
            except:
                pass
            return

        i,o,e = session.stop(session_number=session_number)
        output = o.read(1024)

        self.logger.debug("session stop output: %s" % (output))

        #FIXME:
        # should probably read the output to make sure
        # there were no errors
        self._delete_session_number_record(host,username,session_number)


    def stop_all(self):

        for host in self._lookup.keys():

            for user in self._lookup[host].keys():

                sessions = list(self._lookup[host][user]['sessions'])
                self.logger.debug('closing %s:%s\'s open sessions: %s'
                    % (host,user,sessions))

                # stop each session
                for s in sessions:
                    self.stop(host,user,s['number'])

                # kill the session object
                del self._lookup[host][user]['sessionobj']
                self._lookup[host][user]['sessionobj'] = None

                # delete the user record
                del self._lookup[host][user]

        self.clear()


    def clear(self):

        self._lookup = {}


