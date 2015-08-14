import datetime
import os
import re
import sys
import pprint
import logging
import paramiko
from .toolsessionshell import ToolSessionShell

SSH_PORT=22
PTY_WIDTH=1000
PTY_HEIGHT=1000

class ToolSession(object):

    def __init__(self,host,port=SSH_PORT,username=None,password=None,key_filename=None):

        self.logger = logging.getLogger(__name__)
        self.logger.debug("host = %s" % (host))
        self.logger.debug("port = %s" % (port))
        self.logger.debug("username = %s" % (username))
        self.logger.debug("key_filename = %s" % (key_filename))

        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._key_filename = key_filename

        if key_filename is not None:
            self._key_filename = os.path.expanduser(
                                    os.path.expandvars(key_filename))

        self.debug = False
        self.log_user = False

        self._ssh_client = None

    def __del__(self):

        if self._ssh_client is not None:

            logging.debug("closing toolsession object")
            transport = self._ssh_client.get_transport()

            if transport is not None and \
               transport.is_active() and \
               transport.is_authenticated():

                # close the ssh connection
                logging.debug("closing ssh client")
                self._ssh_client.close()

            # clear our handle
            self._ssh_client = None


    def _new_ssh_client(self):

        self.logger.info("creating a new toolsession ssh client")

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(
            hostname=self._host,
            port=self._port,
            username=self._username,
            password=self._password,
            key_filename=self._key_filename,
            allow_agent=False,
            look_for_keys=False)

        return client


    def _new_ssh_channel(self,client,command):

        self.logger.info("creating a new channel for the ssh client")

        channel = client.get_transport().open_session()
        channel.get_pty(width=PTY_WIDTH,height=PTY_HEIGHT)
        channel.exec_command(command)

        return channel


    def _new_ssh_client_and_channel(self,command):

        client = self._new_ssh_client()
        channel = self._new_ssh_channel(client,command)

        return client,channel


    def help(self):

        """ssh    user@<hub> session help
                print the help message.
        """

        self.logger.info("session help")

        if self._ssh_client is None:
            self._ssh_client = self._new_ssh_client()

        return self._ssh_client.exec_command("session help")


    def access(self,session_number=None,command=None):

        """ssh    user@<hub>
                    create a session if none exists, or enter the
                    first session found (interactive shell)

                    ex: not implemented

           ssh    user@<hub> session
                    create a session if none exists, or enter the
                    first session found (non-interactive shell)

                    ** NOT SUPPORTED **

                    ex: self.access(use_pty=False)

           ssh -t user@<hub> session
                    same as above but get a command prompt
                    (interactive shell).

                    ex: self.access()

           ssh -t user@<hub> session <command>
                    execute the command, if necessary creating
                    a workspace.

                    ex: self.access(use_pty=True,command='echo hi')

           ssh -t user@<hub> session <session #>
                    Access session # (interactive).

                    ex: self.access(use_pty=True,session_number=6193)

           ssh    user@<hub> session <session #> <command>
                    Access session # and execute command.

                    client.exec_command("session %s %s") % (snum,cmd)
                    ex: self.access(use_pty=False,session_number=61,
                            command='echo hi')
        """

        cmd = "session"

        if session_number is not None:
            cmd += " %s" % (session_number)

        self.logger.info("accessing a tool session container")

        if command is not None:
            cmd += " %s" % (command)

            if self._ssh_client is None:
                self._ssh_client = self._new_ssh_client()

            # if you give a command argument, the command will
            # automatically allocate an pty. this is an error for now
            # return (stdin,stdout,stderr) tuple
            self.logger.debug("exec'ing user command: %s" % (command))

            return self._ssh_client.exec_command(cmd)

        else:
            (client,channel) = self._new_ssh_client_and_channel(cmd)

            # return an interactive shell from the session command
            shell = ToolSessionShell(client=client, channel=channel,
                     debug=self.debug, log_user=self.log_user,timeout=60,
                     pty_width=PTY_WIDTH,pty_height=PTY_HEIGHT,startup_cmd=cmd)
            shell.timeout = 10

            return shell


    def list(self):

        """ssh    user@<hub> session list
                    provide a listing of your existing sessions
        """

        self.logger.info("session list")

        if self._ssh_client is None:
            self._ssh_client = self._new_ssh_client()

        return self._ssh_client.exec_command("session list")


    def create(self,title=None,toolname=None):

        """ssh -t user@<hub> session create <session title> <toolname>
                    create a new session. optionally specify a title
                    for the session and a tool to launch.
        """

        cmd = "session create"
        if title is not None:
            cmd += " %s" % (title)

        if toolname is not None:
            if title is None:
                # a title is required when specifying which tool to launch
                title = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                cmd += " %s" % (title)
            cmd += " %s" % (toolname)

        self.logger.info(cmd)

        if self._ssh_client is None:
            self._ssh_client = self._new_ssh_client()

        return self._ssh_client.exec_command(cmd)


    def start(self):

        """ssh -t user@<hub> session start
                    start and enter a new session.
        """

        self.logger.info("session start")

        cmd = 'session start'

        (client,channel) = self._new_ssh_client_and_channel(cmd)

        # return an interactive shell from the session command
        shell = ToolSessionShell(client=client, channel=channel,
                 debug=self.debug, log_user=self.log_user,timeout=60,
                 pty_width=PTY_WIDTH,pty_height=PTY_HEIGHT,startup_cmd=cmd)
        shell.timeout = 10

        return shell


    def stop(self,session_number):

        """ssh -t user@<hub> session stop <session #>
                    stop that session.
        """

        cmd = "session stop %s" % (session_number)
        self.logger.info(cmd)

        if self._ssh_client is None:
            self._ssh_client = self._new_ssh_client()

        return self._ssh_client.exec_command(cmd)


    def get_open_session_detail(self):

        """call the 'session list' command
           return a dictionary with session details.
        """

        self.logger.info("retrieving open session detail")

        i,o,e = self.list()
        data = o.read(1024)
        detailsre = re.compile('(\d+)\s+(\*?)\s+([^\s]+)\s+(.+)$')
        details = {}
        rownum = 0
        for line in data.split('\n'):
            match = detailsre.search(line)
            if match:
                (session_num,default,name,title) = match.groups()
                details.update({
                    rownum : {
                        'session_number'    : session_num,
                        'default'           : True if default == '*' else False,
                        'name'              : name,
                        'title'             : title,
                    }
                })
                rownum += 1

        self.logger.debug(pprint.pformat(details))
        return details

    def get_session_number_by_title(self,title,create=False):

        """find the first session with a title matching the provided title
           and return it's session number. if no session has a matching
           title, return -1. there is about a 2-5 second delay between
           when a session is created and when the 'session list' command
           is updated with the new session title.
        """

        self.logger.info("retrieving session number with title \"%s\"" % (title))

        session_number = -1

        data = self.get_open_session_detail()

        for (key,value) in data.items():
            if value['title'] == title:
                session_number = value['session_number']
                break

        if session_number == -1 and create:
            i,o,e = self.create(title)
            output = o.read(1024)
            session_number = re.search('(\d+)',output).group(0)
            if session_number <= 0:
                # we still don't have a valid session number
                raise RuntimeError("invalid session number: '%s'" % session_number)

        self.logger.info("title \"%s\" matches session number %s" % (title,session_number))
        return session_number

    def sftp(self):

        """
        open a new sftp channel
        """

        if self._ssh_client is None:
            self._ssh_client = self._new_ssh_client()

        transport = self._ssh_client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp



