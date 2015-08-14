# common functions for stuff you would want to do inside of a workspace.

import ConfigParser
import logging
import os
import paramiko
import re
import StringIO

from .sshshell import SSHShell

class ToolSessionShell(SSHShell):


    def importfile(self,remotepath,localpath,mode=None,is_data=False):
        """
        import a file into the workspace.

        do an sftp put of a file on your system (remotepath) into
        the tool session container (localpath).  optionally set the
        mode for the file. if the is_data flag is set to True,
        then remotepath is treated as data to be written to the
        file at localpath. The file localpath will be opened, the
        value of the variable remotepath will be written to it,
        and the file will be closed. in this case, no file is
        written to disk inside of the tool session container.
        the number of bytes written is returned.
        """

        if self._sftp_client is None :
            transport = self._ssh_client.get_transport()
            self._sftp_channel = transport.open_session()
            self._sftp_channel.invoke_subsystem('sftp')
            self._sftp_client = paramiko.SFTPClient(self._sftp_channel)

        # NOTE:
        # remember that this is from the perspective of being inside of the
        # container. so localpath is the file inside of the tool session
        # container, and remotepath is the file on your own system.

        self.logger.debug("sftp'ing local file '%s' to workspace file '%s'"\
            % (remotepath,localpath))

        fsize = 0
        if is_data is True:
            f = self._sftp_client.open(localpath,mode='w')
            f.write(remotepath)
            fsize = f.tell()
            f.close()
        else:
            s = self._sftp_client.put(remotepath,localpath)
            fsize = s.st_size

        if mode is not None:
            self._sftp_client.chmod(localpath,int(mode))

        return fsize


    def exportfile(self,localpath,remotepath,mode=None,is_data=False):
        """
        export a file from the workspace.

        do an sftp get of a file in the tool session container (localpath)
        out to a file on your system (remotepath). optionally set the
        mode for the file. if the is_data flag is set to True,
        then the contents of localpath is returned to the caller. in
        this case, remotepath and mode are ignored; no file will be
        written to disk on your system.
        """

        if self._sftp_client is None :
            transport = self._ssh_client.get_transport()
            self._sftp_channel = transport.open_session()
            self._sftp_channel.invoke_subsystem('sftp')
            self._sftp_client = paramiko.SFTPClient(self._sftp_channel)

        # NOTE:
        # remember that this is from the perspective of being inside of the
        # container. so localpath is the file inside of the tool session
        # container, and remotepath is the file on your own system.

        self.logger.debug("sftp'ing workspace file '%s' to local file '%s'"\
            % (localpath,remotepath))

        data = None

        if is_data is True:
            f = self._sftp_client.open(localpath,mode='r')
            data = f.read()
            f.close()
        else:
            self._sftp_client.get(localpath,remotepath)
            if mode is not None:
                os.chmod(remotepath,int(mode))

        return data


    def _parse_resources_file(self):
        """
        parse the tool session container's resources file

        the file is located at $SESSIONDIR/resources. each line should
        contain a resource key/value pair, separated by a space.
        """

        r = {}
        data = self.read_file('$SESSIONDIR/resources')
        for (k,v,junk) in re.findall('([^\s]+)[ \t]*([^\s]+)?(\n|$)',data):
            r[k] = v

        return r


    def get_nanovis_hosts(self):
        """
        return a list of nanovis servers
        """

        resources = self._parse_resources_file()
        hosts = resources['nanovis_server'].split(',')

        self.logger.debug('nanovis_server: %s' % (hosts))

        return hosts


    def get_molvis_hosts(self):
        """
        return a list of molvis servers
        """

        resources = self._parse_resources_file()
        hosts = resources['molvis_server'].split(',')

        self.logger.debug('molvis_server: %s' % (hosts))

        return hosts


    def get_vtkvis_hosts(self):
        """
        return a list of vtkvis servers
        """

        resources = self._parse_resources_file()
        hosts = resources['vtkvis_server'].split(',')

        self.logger.debug('vtkvis_server: %s' % (hosts))

        return hosts


    def get_vmdmds_hosts(self):
        """
        return a list of vmdmds servers
        """

        resources = self._parse_resources_file()
        hosts = resources['vmdmds_server'].split(',')

        self.logger.debug('vmdmds_server: %s' % (hosts))

        return hosts


    def get_submit_hosts(self):
        """
        return a list of listenURIs for the submit client.
        this information is gathered from the submit client
        configuration file /etc/submit/submit-client.conf.
        """

        path = '/etc/submit/submit-client.conf'
        data = StringIO.StringIO(self.read_file(path))

        config = ConfigParser.ConfigParser(allow_no_value=True)
        config.readfp(data)

        data.close()

        # grab the uris from the file
        uris = config.get('client','listenURIs')
        uris = uris.split(',')

        # clean up extra spaces in the value
        for i in range(len(uris)):
            uris[i] = uris[i].strip()

        self.logger.debug('submit hosts: %s' % (uris))

        return uris


    def get_session_number(self):
        """
        return the session number

        usually 'echo $SESSION' is enough, but sometimesi
        you need to remove the L or D suffix.
        """

        session_number,es = self.execute('echo $SESSION')

        # normalize the session number (remove D and L sufficies)
        sn_match = re.search('(\d+)',session_number)
        if sn_match is None:
            raise RuntimeError('invalid session number returned: %s'
                % (session_number))
        session_number = int(sn_match.group(1))

        return session_number
