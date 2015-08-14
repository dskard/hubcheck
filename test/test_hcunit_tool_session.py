import pytest
import hubcheck


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.pageobjects,
               pytest.mark.hcunit_tool_session_page,
             ]

class TestHCUnitToolSessionPage(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        # start up a tool session container
        self.hubname = self.testdata.find_url_for('https')
        self.username,self.userpass = \
            self.testdata.find_account_for('registeredworkspace')

        self.cm = hubcheck.shell.ContainerManager()
        self.ws = self.cm.access(host=self.hubname,
                                 username=self.username,
                                 password=self.userpass)

        self.session_number,es = self.ws.execute('echo $SESSION')
        self.ws.close()

        # setup a web browser
        self.browser.get(self.https_authority)

        self.utils.account.login_as(self.username,self.userpass)

        self.po = self.catalog.load_pageobject('ToolSessionPage',
                    'workspace',int(self.session_number))
        self.po.goto_page()


    def teardown_method(self,method):

        # get out of the workspace
        # shut down the ssh connection
        self.cm.sync_open_sessions(self.hubname,self.username)


    def test_fxn_terminate(self):
        """
        test pressing the terminate button on the app
        """

        self.po.app.do_terminate()


    def test_fxn_keep(self):
        """
        test pressing the keep button on the app
        """

        self.po.app.do_keep()


    def test_fxn_refresh(self):
        """
        test pressing the refresh button on the app
        """

        self.po.app.do_refresh()


    def test_get_session_number(self):
        """
        test retrieving the session number of the app
        """

        app_session_number = self.po.app.get_session_number()

        assert int(self.session_number) == int(app_session_number),\
            "while retrieving the session number:" \
            + "session_number = %d, app_session_number = %d" \
            % (int(self.session_number),int(app_session_number))


    def test_share_session_with_1(self):
        """
        test sharing the session with nobody
        """

        self.po.share.share_session_with()


    def test_share_session_with_2(self):
        """
        test sharing the session with another user
        """

        username2,junk = \
            self.testdata.find_account_for('purdueworkspace')
        self.po.share.share_session_with(username2)


    def test_share_session_with_3(self):
        """
        test sharing the session with a fake user
        """

        self.po.share.share_session_with('fakeuserthatshouldnotexist')


    def test_share_session_with_4(self):
        """
        test sharing the session with a group
        """

        self.po.share.share_session_with(group=0)


    def test_share_session_with_5(self):
        """
        test sharing the session with another user, read only
        """

        username2,junk = \
            self.testdata.find_account_for('purdueworkspace')
        self.po.share.share_session_with(username2,readonly=True)


    def test_get_shared_with_1(self):
        """
        test getting an empty list of people who this session is shared with
        """

        sharedwith = self.po.share.get_shared_with()

        if len(sharedwith) > 0:
            # if the session was previously shared, disconnect everyone
            # so we can test getting an empty list
            for name in sharedwith:
                self.po.share.disconnect(name)

            sharedwith = self.po.share.get_shared_with()

        assert sharedwith == [], "sharedwith contains: %s" % (sharedwith)


    def test_get_shared_with_2(self):
        """
        test getting the list of people who this session is shared with
        """

        # share the session with someone
        username2,junk = \
            self.testdata.find_account_for('purdueworkspace')
        self.po.share.share_session_with(username2)

        # get the list of people the session is shared with
        sharedwith = self.po.share.get_shared_with()

        assert sharedwith != [], \
            "after sharing the session with %s, sharedwith is empty" \
            % (username2)


    def test_disconnect_1(self):
        """
        test disconnecting a connected user from a tool session container
        """

        # share the session with someone
        username2,junk = \
            self.testdata.find_account_for('purdueworkspace')
        self.po.share.share_session_with(username2)

        # get the list of people the session is shared with
        self.po.share.disconnect(username2)


    def test_disconnect_2(self):
        """
        test disconnecting an unconnected user from a tool session container
        """

        with pytest.raises(hubcheck.exceptions.NoSuchUserException):
            self.po.share.disconnect('fakeuserthatshouldnotexist')


    def test_storage_goto_manage(self):
        """
        click the link to navigate to storage management page
        """

        pageurl1 = self.po.current_url()

        self.po.app.storage.goto_manage()

        pageurl2 = self.po.current_url()

        assert pageurl1 != pageurl2, \
            "after clicking the manage storage link," \
            + " url did not change: pageurl1 = %s, pageurl2 = '%s'" \
            % (pageurl1,pageurl2)


    def test_storage_meter(self):
        """
        retrieve the free storage amount
        """

        storage_amount = self.po.app.storage.storage_meter()

        assert storage_amount != '', \
            "invalid storage amount returned: %s" % (storage_amount)



