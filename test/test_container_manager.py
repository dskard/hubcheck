import paramiko
import pytest
import tempfile
import os
import re
import time

import hubcheck
from hubcheck.shell import SSHShell, ToolSession, ContainerManager
from hubcheck.exceptions import ExitCodeError

pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_shell,
             ]

HOST = ''
USERNAME = ''
PASSWORD = ''
KEY_FNAME = None


cm = ContainerManager()

@pytest.mark.sshshell
class TestHCUnitContainerManager(object):

    def test_get_buffer_3(self,ssh_shell):
        """check for empty buffer after retrieving prompt
        """

        p = ssh_shell.get_prompt()
        buf = ssh_shell.get_buffer()
        assert buf == '', "buf = '%s', expected ''" % (buf)



    def setUp(self):

        self.cm = ContainerManager()

        self.host1 = ''
        self.user11 = ''
        self.pass11 = ''
        self.user12 = ''
        self.pass12 = ''

        self.host2 = ''
        self.user21 = ''
        self.pass21 = ''
        self.user22 = ''
        self.pass22 = ''

    def tearDown(self):

        self.cm.stop_all()
        self.cm.clear()


    def test_access_new_session(self,cm):
        """
        """

        ws = cm.access(self.host1,self.user11,self.pass11)
        session_number,es = ws.execute('echo $SESSION')
        self.assertTrue(int(session_number) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number)
        ws.close()


    def test_access_previously_opened_session(self):
        """
        """

        # open the first tool session container
        ws1 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number1,es = ws1.execute('echo $SESSION')
        # exit the container
        ws1.close()

        # make sure we got into the container
        self.assertTrue(int(session_number1) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number1)

        # open the second tool session container
        ws2 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number2,es = ws2.execute('echo $SESSION')
        ws2.close()

        # make sure we got into the second container
        self.assertTrue(int(session_number2) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number2)

        # check that the first and second containers were the same
        # by comparing the session number

        self.assertTrue(int(session_number1) == int(session_number2),
            "connecting twice to the same session failed: session_number1 = %s, session_number2 = %s" \
            % (session_number1,session_number2))


    def test_access_sessions_for_different_users_same_host(self):
        """
        """

        # open tool session container for user1
        ws1 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number1,es = ws1.execute('echo $SESSION')
        # exit the container
        ws1.close()

        # make sure we got into the container
        self.assertTrue(int(session_number1) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number1)

        # open tool session container for user2
        ws2 = self.cm.access(self.host1,self.user12,self.pass12)
        session_number2,es = ws2.execute('echo $SESSION')
        ws2.close()

        # make sure we got into the second container
        self.assertTrue(int(session_number2) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number2)

        # check that the first and second containers are different
        # by comparing the session number

        self.assertTrue(int(session_number1) != int(session_number2),
            "trying to connect to two different containers, as different users failed: session_number1 = %s, session_number2 = %s" \
            % (session_number1,session_number2))


    def test_access_sessions_for_different_users_different_host(self):
        """
        """

        # open tool session container for user1
        ws1 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number1,es = ws1.execute('echo $SESSION')
        # exit the container
        ws1.close()

        # make sure we got into the container
        self.assertTrue(int(session_number1) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number1)

        # open tool session container for user2
        ws2 = self.cm.access(self.host2,self.user21,self.pass21)
        session_number2,es = ws2.execute('echo $SESSION')
        ws2.close()

        # make sure we got into the second container
        self.assertTrue(int(session_number2) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number2)

        # check that the first and second containers are different
        # by comparing the session number

        self.assertTrue(int(session_number1) != int(session_number2),
            "trying to connect to two different containers, as different users failed: session_number1 = %s, session_number2 = %s" \
            % (session_number1,session_number2))


    def test_stop_session_1(self):
        """
        close a session that is open
        """

        # open a session
        ws1 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number1,es = ws1.execute('echo $SESSION')
        self.assertTrue(int(session_number1) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number1)
        ws1.close()

        # stop the tool session container
        self.cm.stop(self.host1,self.user11,session_number1)

        session = ToolSession(host=self.host1,
                              username=self.user11,
                              password=self.pass11)

        data = session.get_open_session_detail()
        for k,v in data.items():
            if v['session_number'] == session_number1:
                self.assertTrue(v['session_number'] == session_number1,
                    "session %s still open, after calling stop()" \
                    % (session_number1))


    def test_stop_session_2(self):
        """
        try to close a session that is not open
        """

        # open a temporary session
        # so we can get a session in the stop() method
        ws1 = self.cm.access(self.host1,self.user11,self.pass11)
        session_number1,es = ws1.execute('echo $SESSION')
        self.assertTrue(int(session_number1) > 0,
            "session_number = %s, i don't think we are in a workspace" \
            % session_number1)
        ws1.close()


        try:
            # stop the tool session container
            session_number2 = 1234
            self.cm.stop(self.host1,self.user11,session_number2)
        finally:
            # close the temporary session
            self.cm.stop(self.host1,self.user11,session_number1)

