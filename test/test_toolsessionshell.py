import unittest
import re
import os
import sys
import hubcheck
import tempfile
import logging


LOGFILE = './toolsessionshell.log'
CONTAINER_NAME = 'tool_session_shell_tests'

HOST = None
USERNAME = None
PASSWORD = None
KEY_FILENAME = None


def pretest_setup():
    """
    open a tool session container for tests to run in
    """

    session = hubcheck.shell.ToolSession(
        host=HOST, username=USERNAME,
        password=PASSWORD, key_filename=KEY_FILENAME)

    # start up a session so we can get the session number
    i,o,e = session.create(title=CONTAINER_NAME)
    output = o.read(1024)
    session_number = int(re.search('(\d+)',output).group(0))

    if session_number <= 0:
        raise RuntimeError('invalid session number: %s' % (session_number))

    return session_number

def posttest_teardown(session_number):
    """
    close the tool session container the tests were running in
    """

    session = hubcheck.shell.ToolSession(
        host=HOST, username=USERNAME,
        password=PASSWORD, key_filename=KEY_FILENAME)

    # start up a session so we can get the session number
    session.stop(session_number)


class tool_session_shell_tests(unittest.TestCase):

    def setUp(self):

        self.session = hubcheck.shell.ToolSession(
            host=HOST, username=USERNAME,
            password=PASSWORD, key_filename=KEY_FILENAME)

        self.shell = self.session.access(session_number=CONTAINER_NAME)


    def tearDown(self):

        del self.shell
        del self.session


    def test_importfile_valid_remotepath_valid_localpath(self):
        """
        test importfile (sftp put)
        """

        # create a temporary file
        handle,remotepath = tempfile.mkstemp()
        indata = "hubcheck\ntool session shell test\n%s" % (remotepath)
        os.write(handle,indata)
        os.close(handle)

        # perform the transfer
        localpath,es = self.shell.execute('echo ${PWD}/$RANDOM.tmp')
        size = self.shell.importfile(remotepath,localpath)

        outdata = self.shell.read_file(localpath)

        # clean up the files
        self.shell.execute("rm -f %s" % (localpath))
        os.remove(remotepath)

        # check the transfer
        self.assertTrue(size == len(indata),
            "size mismatch: wrote %s bytes, expected %s bytes" \
            % (size,len(indata)))

        self.assertTrue(indata == outdata,
            "file data mismatch: wrote '%s', expected '%s'" \
            % (repr(outdata),repr(indata)))



    def test_exportfile_valid_remotepath_valid_localpath(self):
        """
        test exportfile (sftp get)
        """

        # create a temporary file
        localpath,es = self.shell.execute('echo ${PWD}/$RANDOM.tmp')
        indata = "hubcheck\ntool session shell test\n%s" % (localpath)
        self.shell.write_file(localpath,indata)


        # perform the transfer
        handle,remotepath = tempfile.mkstemp()
        os.close(handle)
        rv = self.shell.exportfile(localpath,remotepath)

        outdata = self.shell.read_file(localpath)

        # clean up the files
        self.shell.execute("rm -f %s" % (localpath))
        os.remove(remotepath)

        # check the transfer
        self.assertTrue(rv == None,
            "wrong return value: received %s, expected None" \
            % (rv))

        self.assertTrue(indata == outdata,
            "file data mismatch: wrote '%s', expected '%s'" \
            % (repr(outdata),repr(indata)))


    def test_nanovis_hosts_1(self):
        """
        test get_nanovis_hosts
        """

        hosts = self.shell.get_nanovis_hosts()

        self.assertTrue(len(hosts) != 0, 'returned an empty list')


    def test_molvis_hosts_1(self):
        """
        test get_molvis_hosts
        """

        hosts = self.shell.get_molvis_hosts()

        self.assertTrue(len(hosts) != 0, 'returned an empty list')


    def test_vtkvis_hosts_1(self):
        """
        test get_vtkvis_hosts
        """

        hosts = self.shell.get_vtkvis_hosts()

        self.assertTrue(len(hosts) != 0, 'returned an empty list')


    def test_submit_hosts_1(self):
        """
        test get_submit_hosts
        """

        hosts = self.shell.get_submit_hosts()

        self.assertTrue(len(hosts) != 0, 'returned an empty list')


if __name__ == '__main__':
    logpath = os.path.abspath(os.path.expanduser(os.path.expandvars(LOGFILE)))
    logging.basicConfig(filename=logpath,
                        format="%(asctime)s: %(message)s",
                        loglevel='DEBUG')

    session_number = pretest_setup()
    tr = unittest.TextTestRunner(stream=sys.stdout,verbosity=0)
    unittest.main(testRunner=tr,exit=False)
    posttest_teardown(session_number)
