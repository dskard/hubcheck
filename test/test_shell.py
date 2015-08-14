import paramiko
import pytest
import hubcheck
import tempfile
import os
import re
import time

from hubcheck.shell import SSHShell, ToolSession
from hubcheck.exceptions import ExitCodeError

pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_shell,
             ]

HOST = ''
USERNAME = ''
PASSWORD = ''
KEY_FNAME = None


@pytest.fixture(scope="module")
def ssh_shell(request):
    """create and clean up an SSHShell
    """

    host = getattr(request.module,"HOST","myhub.org")
    username = getattr(request.module,"USERNAME","testuser")
    password = getattr(request.module,"PASSWORD","abc123")
    key_fname = getattr(request.module,"KEY_FNAME","")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host,username=USERNAME,password=PASSWORD,
        key_filename=KEY_FNAME)

    channel = client.invoke_shell()

    shell = SSHShell(client,channel,debug=False,log_user=False)

    def fin():
        shell.close()

    request.addfinalizer(fin)

    return shell


@pytest.fixture(scope="function")
def tmpfname(request):
    """create a temporary file for tests and clean it up afterwards
    """

    (fd,fname) = tempfile.mkstemp()

    def fin():
        try:
            os.close(fd)
        except OSError:
            pass
        if os.path.isfile(fname):
            os.remove(fname)

    request.addfinalizer(fin)

    return fname


@pytest.mark.sshshell
class TestHCUnitSSHShell(object):

    def test_get_buffer_3(self,ssh_shell):
        """check for empty buffer after retrieving prompt
        """

        p = ssh_shell.get_prompt()
        buf = ssh_shell.get_buffer()
        assert buf == '', "buf = '%s', expected ''" % (buf)


    def test_get_buffer_4(self,ssh_shell):
        """check for non empty buffer after sending command
        """

        ssh_shell.send('echo hi')
        buf = ssh_shell.get_buffer()
        assert buf != '', "buf is empty"


    def test_execute_1(self,ssh_shell):
        """execute a single command in a list
        """

        output,es = ssh_shell.execute(['echo hi'])
        assert output == 'hi'


    def test_execute_2(self,ssh_shell):
        """execute a single command as a string
        """

        output,es = ssh_shell.execute('echo hi')
        assert output == 'hi'


    def test_execute_3(self,ssh_shell):
        """execute multiple commands
        """

        output,es = ssh_shell.execute(['echo hi','date','echo bye'])
        assert output == 'bye'


    def test_execute_4(self,ssh_shell):
        """execute a single command that fails
        """

        with pytest.raises(ExitCodeError):
            ssh_shell.execute(['badcommand'])


    def test_execute_5(self,ssh_shell):
        """execute multiple commands that fails at start
        """

        with pytest.raises(ExitCodeError):
            ssh_shell.execute(['badcommand','echo hi','echo bye'])


    def test_execute_6(self,ssh_shell):
        """ execute multiple commands that fails in the middle
        """

        with pytest.raises(ExitCodeError):
            ssh_shell.execute(['echo hi','badcommand','echo bye'])


    def test_execute_7(self,ssh_shell):
        """execute multiple commands that fails at the end
        """

        with pytest.raises(ExitCodeError):
            ssh_shell.execute(['echo hi','echo bye','badcommand'])


    def test_log_user(self,ssh_shell,tmpfname):
        """turn on log_user
        """

        with open(tmpfname,'w') as fh:
            ssh_shell.log_user = True

            # start logging
            ssh_shell.log_file(fh)

            ssh_shell.execute(['echo hi'])

            # stop logging
            ssh_shell.log_file()

        # read the log data from the file
        with open(tmpfname,'r') as f:
            data = f.read()

        # check if we wrote anything
        assert len(data) > 0, 'failed to write log file'


    def test_debug(self,ssh_shell,tmpfname):
        """put object into debug mode
        """

        with open(tmpfname,'w') as f:
            ssh_shell.debug = True

            # start logging
            ssh_shell.log_file(f)

            ssh_shell.execute(['echo hi'])

            # stop logging
            ssh_shell.log_file()

        # read the log data from the file
        with open(tmpfname,'r') as f:
            data = f.read()

        # check if we wrote anything
        assert len(data) > 0, 'failed to write log file'


@pytest.fixture(scope="module")
def session(request):
    """create and clean up a ToolSession object
    """

    host = getattr(request.module,"HOST","myhub.org")
    username = getattr(request.module,"USERNAME","testuser")
    password = getattr(request.module,"PASSWORD","abc123")
    key_fname = getattr(request.module,"KEY_FNAME","")

    session = ToolSession(host=host, username=username,
                          password=password, key_filename=key_fname)

    return session


@pytest.fixture(scope="module")
def session_number(request,session):
    """create and clean up a ToolSession object
    """

    i,o,e = session.access(command='env | grep SESSION= | cut -d"=" -f 2')
    session_number = int(o.read(1024).strip())

    def fin():
        session.stop(session_number)

    request.addfinalizer(fin)

    return session_number


@pytest.mark.toolsession
class TestHCUnitToolSession(object):


    def test_session_help(self,session):
        """issue the 'session help' command
        """

        i,o,e = session.help()
        output = o.read(1024)
        assert output != '', "output is empty, no help data printed"


#    def test_session_access_1(self,session):
#        """issue 'ssh user@<hub> session'
#           interactive shell without pty is not currently supported
#        """
#        shell = session.access(use_pty=False)
#        # since there is no pty, there is no prompt and
#        # we cannot use the execute() function
#        shell.send('echo $SESSION')
#        buf = shell.get_buffer()
#        idx = shell.expect(['(\d+)'])
#        assert idx == 0, "echo $SESSION returned '%s'" % (buf)


    def test_session_access_2(self,session):
        """issue 'ssh -t user@<hub> session'
        """

        shell = session.access()
        output,es = shell.execute('echo hi')
        assert output == 'hi', "output = %s" % (output)


    def test_session_access_3(self,session):
        """issue 'ssh -t user@<hub> session <command>'
        """

        i,o,e = session.access(command='echo hi')
        output = o.read(1024)
        assert output == 'hi\n', "output = %s" % (output)


    def test_session_access_4(self,session,session_number):
        """issue 'ssh -t user@<hub> session <session #>'
        """

        shell = session.access(session_number=session_number)
        output,es = shell.execute('echo $SESSION')
        assert int(output) == int(session_number), "output = %s" % (output)


    def test_session_access_5(self,session,session_number):
        """issue 'ssh -t user@<hub> session <session #> <command>'
        """

        i,o,e = session.access(session_number=session_number,
                               command='echo $SESSION')
        output = int(re.search('(\d+)',o.read(1024)).group(0))
        assert output == session_number, "output = %s" % (output)


    def test_session_start(self,session):
        """issue 'ssh -t user@<hub> session start'
        """

        self.session = session

        shell = self.session.start()
        output,es = shell.execute('echo $SESSION')
        assert int(output) > 0,"output = %s" % (output)
        shell.close()


    def test_session_list(self,session):
        """issue 'ssh user@<hub> session list'
        """

        i,o,e = session.list()
        output = o.read(1024)
        assert output != '', "output of list command is empty"


    def test_get_open_session_detail_1(self,session,session_number):
        """get_open_session_detail should call 'session list', returns a dict
        """

        data = session.get_open_session_detail()
        assert len(data) > 0, "data is empty"


    def test_get_open_session_detail_2(self,session):
        """test that opening a new session shows up in get_open_session_detai
        """

        shell = session.start()
        session_number = int(shell.execute('echo $SESSION')[0])
        assert session_number > 0, \
            "invalid session number: %s" % (session_number)
        shell.close()

        data = session.get_open_session_detail()

        session.stop(session_number)

        has_session = False
        for session_info in data.values():
            if int(session_info['session_number']) == session_number:
                has_session = True
                break

        assert has_session, \
            "newly opened session number %d does not appear in %s" % \
            (session_number,data)


    def test_get_session_number_by_title_1(self,session):
        """test searching the 'session list' command for a session by title
           when there is a matching title.
        """

        title = 'tstest1'

        # start a test session with a title
        i,o,e = session.create(title)
        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))

        assert session_number > 0, \
            "invalid session number: %s\noutput = '%s'" % \
            (session_number,output)


        try:
            # account for the 5 seconds it takes between when the
            # session is created to when the 'session list' command
            # is updated
            time.sleep(5)

            test_sn = int(session.get_session_number_by_title(title))

            assert session_number == test_sn, \
                "session_number = '%s', test_sn = '%s', output = '%s'" % \
                (session_number,test_sn,output)
        finally:
            session.stop(session_number)


    def test_get_session_number_by_title_2(self,session):
        """test searching the 'session list' command for a session by title
           when there is no matching title.
        """

        title = 'tstest2'

        test_sn = int(session.get_session_number_by_title(title))

        assert test_sn == -1, "test_sn = '%s'" % (test_sn)




@pytest.mark.toolsession
class TestHCUnitToolSession2(object):

    def setup_method(self,method):
        self.session = None
        self.session_number = None


    def teardown_method(self,method):
        if self.session_number is not None:
            self.session.stop(self.session_number)


    def test_session_create_1(self,session):
        """issue 'ssh user@<hub> session create'
        """

        self.session = session

        i,o,e = self.session.create()

        output = o.read(1024)
        self.session_number = int(re.search('(\d+)',output).group(0))
        assert self.session_number > 0, \
            "output = %s\ninvalid session number: %s" % \
            (output,self.session_number)


    def test_session_create_2(self,session):
        """test issuing 'ssh user@<hub> session create <title>'"""

        self.session = session

        i,o,e = self.session.create(title="hc_test_workspace")

        output = o.read(1024)
        self.session_number = int(re.search('(\d+)',output).group(0))
        assert self.session_number > 0, \
            "output = %s\ninvalid session number: %s" % \
            (output,self.session_number)


    def test_session_create_3(self,session):
        """test issuing 'ssh user@<hub> session create <title> <toolname>'"""

        self.session = session

        i,o,e = self.session.create(title="hc_test_workspace_create",toolname="workspace")

        output = o.read(1024)
        self.session_number = int(re.search('(\d+)',output).group(0))
        assert self.session_number > 0, \
            "output = %s\ninvalid session number: %s" % \
            (output,self.session_number)


    def test_session_stop(self,session):
        """issue 'ssh -t user@<hub> session stop <session #>'
        """

        self.session = session

        # start up a session so we can get the session number
        i,o,e = self.session.create()
        self.session_number = int(re.search('(\d+)',o.read(1024)).group(0))
        assert self.session_number > 0, \
            "session_number = %s" % (self.session_number)

        # stop the session
        i,o,e = self.session.stop(session_number=self.session_number)
        output = o.read(1024)

# 'stopping session' message doesnt seem to come across stdout or stderr
#        match = re.search("stopping session (\d+)",output)
#
#        self.assertTrue(match is not None,"output = %s" % (output))
#
#        out_session_number = match.group(0)
#        self.assertTrue(out_session_number == session_number,
#            "out_session_number = %s\nsession_number=%s" % \
#            (out_session_number,session_number))
#



