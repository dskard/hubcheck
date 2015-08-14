import os
import paramiko
from .sshshell import SSHShell

SSH_PORT=22

class SSHClient(SSHShell):

    def __init__(self, host, port=SSH_PORT, username=None, password=None,
                 key_filename=None, debug=False, log_user=False,
                 buffer_size=4096):

        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._key_filename = key_filename

        if key_filename is not None:
            self._key_filename = os.path.expanduser(
                                    os.path.expandvars(key_filename))

        # setup the ssh client and authenticate
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.load_system_host_keys()
        self._client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            key_filename=key_filename,
            allow_agent=False,
            look_for_keys=False)

        # invoke a new shell
        channel = self._client.invoke_shell(width=1000,height=1000)

        # feed our ssh_client to the SSHShell object constructor
        super(SSHClient,self).__init__(
            client = self._client,
            channel = channel,
            debug = debug,
            log_user = log_user,
            buffer_size = buffer_size
        )
