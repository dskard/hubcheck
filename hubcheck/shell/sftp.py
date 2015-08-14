import os
import paramiko

SSH_PORT = 22

class SFTPClient(paramiko.SFTPClient):

    def __init__(self,host,port=SSH_PORT,username=None,password=None,key_filename=None):

        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._key_filename = key_filename

        if key_filename is not None:
            self._key_filename = os.path.expanduser(
                                    os.path.expandvars(key_filename))

        # use an ssh connection so we can
        # set missing host key policy
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.load_system_host_keys()
        self._ssh_client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            key_filename=key_filename,
            allow_agent=False,
            look_for_keys=False)

        transport = self._ssh_client.get_transport()

        # open a new sftp channel
        self._channel = transport.open_session()
        self._channel.invoke_subsystem('sftp')

        # feed the new channel to be initialized as a paramiko.SFTPClient object
        super(SFTPClient,self).__init__(self._channel)


    def __del__(self):

        transport = self._ssh_client.get_transport()
        if transport.is_active():

            # close the channel
            self._channel.close()
            self._channel = None

            # close the ssh client connection
            self._ssh_client.close()
            self._ssh_client = None


class SFTPClient2(paramiko.SFTPClient):

    def __init__(self,host,username,password,port=SSH_PORT):

        self._host = host
        self._port = port
        self._username = username
        self._password = password

        self._transport = paramiko.Transport((host,port))
        self._transport.connect(username=username,password=password)

        # open a new sftp channel
        self._channel = self._transport.open_session()
        self._channel.invoke_subsystem('sftp')

        # feed the new channel to be initialized as a paramiko.SFTPClient object
        super(SFTPClient2,self).__init__(self._channel)


    def __del__(self):

        if self._transport.is_active():

            # close the channel
            self._channel.close()
            self._channel = None

