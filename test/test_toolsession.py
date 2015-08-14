import unittest
import re
import sys
import hubcheck

class tool_session_tests(unittest.TestCase):

    def setUp(self):

        host = ''
        username = None
        password = None
        key_filename = None

        self.session = hubcheck.shell.ToolSession(
            host=host, username=username,
            password=password, key_filename=key_filename)

        self._session_number = -1


    def test_session_help(self):
        """test issuing the 'session help' command"""
        i,o,e = self.session.help()
        output = o.read(1024)
        self.assertTrue(output != '',
            "output is empty, no help data printed")

#    def test_session_access_1(self):
#        """test issuing 'ssh user@<hub> session'
#           interactive shell without pty is not currently supported
#        """
#        shell = self.session.access(use_pty=False)
#        # since there is no pty, there is no prompt and
#        # we cannot use the execute() function
#        shell.send('echo $SESSION')
#        buf = self.get_buffer()
#        idx = shell.expect(['(\d+)'])
#        self.assertTrue(idx == 0,"echo $SESSION returned '%s'" % (buf))

    def test_session_access_2(self):
        """test issuing 'ssh -t user@<hub> session'"""
        shell = self.session.access()
        output,es = shell.execute('echo hi')
        self.assertTrue(output == 'hi',"output = %s" % (output))

    def test_session_access_3(self):
        """test issuing 'ssh -t user@<hub> session <command>'"""
        i,o,e = self.session.access(command='echo hi')
        output = o.read(1024)
        self.assertTrue(output == 'hi\n',"output = %s" % (output))

    def test_session_access_4(self):
        """test issuing 'ssh -t user@<hub> session <session #>'"""

        # start up a session so we can get the session number
        i,o,e = self.session.create()
        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))
        self.assertTrue(session_number > 0,
            "session_number = %s\noutput = %s" % (session_number,output))

        self._session_number = session_number

        # try to access the newly started session
        shell = self.session.access(session_number=session_number)
        output,es = shell.execute('echo $SESSION')
        self.assertTrue(int(output) > 0,"output = %s" % (output))

    def test_session_access_5(self):
        """test issuing 'ssh -t user@<hub> session <session #> <command>'"""

        # start up a session so we can get the session number
        i,o,e = self.session.create()
        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))
        self.assertTrue(session_number > 0,
            "session_number = %s\noutput = %s" % (session_number,output))

        self._session_number = session_number

        # access the newly started session to run a command
        i,o,e = self.session.access(session_number=session_number,command='echo $SESSION')
        output = int(re.search('(\d+)',o.read(1024)).group(0))
        self.assertTrue(output > 0,"output = %s" % (output))

    def test_session_list(self):
        """test issuing 'ssh user@<hub> session list'"""
        i,o,e = self.session.list()
        output = o.read(1024)
        self.assertTrue(output != '',"output of list command is empty")


    def test_session_create_1(self):
        """test issuing 'ssh user@<hub> session create'"""

        i,o,e = self.session.create()

        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))
        self.assertTrue(session_number > 0,
            "output = %s\ninvalid session number: %s" % \
            (output,session_number))
        self._session_number = session_number


    def test_session_create_2(self):
        """test issuing 'ssh user@<hub> session create <title>'"""

        i,o,e = self.session.create(title="hc_test_workspace")

        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))
        self.assertTrue(session_number > 0,
            "output = %s\ninvalid session number: %s" % \
            (output,session_number))
        self._session_number = session_number


    def test_session_create_3(self):
        """test issuing 'ssh user@<hub> session create <title> <toolname>'"""

        i,o,e = self.session.create(title="hc_test_workspace_create",toolname="workspace")

        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))
        self.assertTrue(session_number > 0,
            "output = %s\ninvalid session number: %s" % \
            (output,session_number))
        self._session_number = session_number


    def test_session_start(self):
        """test issuing 'ssh -t user@<hub> session start'"""
        shell = self.session.start()
        output,es = shell.execute('echo $SESSION')
        self.assertTrue(int(output) > 0,"output = %s" % (output))
        shell.close()


    def test_session_stop(self):
        """test issuing 'ssh -t user@<hub> session stop <session #>'"""

        # start up a session so we can get the session number
        i,o,e = self.session.create()
        session_number = int(re.search('(\d+)',o.read(1024)).group(0))
        self.assertTrue(session_number > 0,
            "session_number = %s" % (session_number))

        self._session_number = session_number

        # stop the session
        i,o,e = self.session.stop(session_number=session_number)
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

        self._session_number = -1


    def test_get_open_session_detail_1(self):
        """test that get_open_session_detail, a wrapper for 'session list', returns a dict"""
        data = self.session.get_open_session_detail()


    def test_get_open_session_detail_2(self):
        """test that opening a new session shows up in get_open_session_detail"""

        shell = self.session.start()
        session_number = int(shell.execute('echo $SESSION')[0])
        self.assertTrue(session_number > 0,
            "invalid session number: %s" % (session_number))
        shell.close()

        data = self.session.get_open_session_detail()

        self.session.stop(session_number)

        has_session = False
        for session_info in data.values():
            if int(session_info['session_number']) == session_number:
                has_session = True
                break

        self.assertTrue(has_session,
            "newly opened session number %d does not appear in %s" % \
            (session_number,data))


    def test_get_session_number_by_title_1(self):
        """test searching the 'session list' command for a session by title
           when there is a matching title.
        """

        title = 'tstest1'

        # start a test session with a title
        i,o,e = self.session.create(title)
        output = o.read(1024)
        session_number = int(re.search('(\d+)',output).group(0))

        self.assertTrue(session_number > 0,
            "invalid session number: %s\noutput = '%s'" % \
            (session_number,output))

        self._session_number = session_number

        # account for the 5 seconds it takes between when the
        # session is created to when the 'session list' command
        # is updated
        import time
        time.sleep(5)

        test_sn = int(self.session.get_session_number_by_title(title))

        self.assertTrue(session_number == test_sn,
            "session_number = '%s', test_sn = '%s', output = '%s'" % \
            (session_number,test_sn,output))


    def test_get_session_number_by_title_2(self):
        """test searching the 'session list' command for a session by title
           when there is no matching title.
        """

        title = 'tstest2'

        test_sn = int(self.session.get_session_number_by_title(title))

        self.assertTrue(test_sn == -1, "test_sn = '%s'" % (test_sn))


    def tearDown(self):
        if self._session_number > 0:
            self.session.stop(self._session_number)


if __name__ == '__main__':
    tr = unittest.TextTestRunner(stream=sys.stdout,verbosity=0)
    unittest.main(testRunner=tr,exit=False)
