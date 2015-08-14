import sys
import logging
import hubcheck
import unittest
import paramiko

class ssh_shell_tests(unittest.TestCase):

    def setUp(self):

        host = ''
        username = None
        password = None
        key_filename = None

        host = ''
        key_filename = ''

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(host,username=username,password=password,
            key_filename=key_filename)

        channel = client.invoke_shell()

        self.c = SSHShell(client,channel,debug=False,log_user=False)

    def test_get_buffer_3(self):
        """test retrieving the internal buffer after retrieving the prompt"""
        p = self.c.get_prompt()
        buf = self.c.get_buffer()
        self.assertTrue(buf == '',"buf = '%s', expected ''" % (buf))

    def test_get_buffer_4(self):
        """test retrieving the internal buffer"""
        self.c.send('echo hi')
        buf = self.c.get_buffer()
        self.assertFalse(buf == '',"buf = %s" % (buf))

    def test_execute_1(self):
        """test executing one a single command in a list"""
        output,es = self.c.execute(['echo hi'])
        self.assertTrue(output == 'hi')

    def test_execute_2(self):
        """test executing one a single command as a string"""
        output,es = self.c.execute('echo hi')
        self.assertTrue(output == 'hi')

    def test_execute_3(self):
        """test executing multiple commands"""
        output,es = self.c.execute(['echo hi','date','echo bye'])
        self.assertTrue(output == 'bye')

    def test_execute_4(self):
        """test executing a single command that fails"""
        self.assertRaises(hubcheck.exceptions.ExitCodeError,self.c.execute,
            ['badcommand'])

    def test_execute_5(self):
        """test executing multiple commands that fails at start"""
        self.assertRaises(hubcheck.exceptions.ExitCodeError,self.c.execute,
            ['badcommand','echo hi','echo bye'])

    def test_execute_6(self):
        """test executing multiple commands that fails in the middle"""
        self.assertRaises(hubcheck.exceptions.ExitCodeError,self.c.execute,
            ['echo hi','badcommand','echo bye'])

    def test_execute_7(self):
        """test executing multiple commands that fails at the end"""
        self.assertRaises(hubcheck.exceptions.ExitCodeError,self.c.execute,
            ['echo hi','echo bye','badcommand'])

    def test_log_user(self):
        """test turning on log_user"""
        fname = 'sshshell.out'
        self.c.log_user = True
        fd = open(fname,'w')

        # try connecting to the machine, and write a log file
        try:
            # start logging
            self.c.log_file(fd)

            self.c.execute(['echo hi'])

            # stop logging
            self.c.log_file()
        finally:
            fd.close()

        # read the log data from the file
        with open(fname,'r') as f:
            data = f.read()

        # check if we wrote anything
        self.assertTrue(len(data) > 0,
            'failed to write log file')

    def test_debug(self):
        """test putting object into debug mode"""
        fname = 'sshshell.debug'
        self.c.debug = True
        fd = open(fname,'w')

        # try connecting to the machine, and write a log file
        try:
            # start logging
            self.c.log_file(fd)

            self.c.execute(['echo hi'])

            # stop logging
            self.c.log_file()
        finally:
            fd.close()

        # read the log data from the file
        with open(fname,'r') as f:
            data = f.read()

        # check if we wrote anything
        self.assertTrue(len(data) > 0,
            'failed to write log file')

    def tearDown(self):
        self.c.close()

# TODO:
# need a test for the execute() fxn where a command times out, should print timeout message to screen
# need a test for update_search_prompt()
# need a test for read_file()
# need a test for execute_script()
#   -> echo hi\necho bye
#   -> echok hi\necho bye
#   -> echo hi\nechok bye

if __name__ == '__main__':
    tr = unittest.TextTestRunner(stream=sys.stdout,verbosity=0)
    unittest.main(testRunner=tr,exit=False)
