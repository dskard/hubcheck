import pytest
import hubcheck
import datetime


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.pageobjects,
               pytest.mark.hcunit_members_dashboard_page,
               pytest.mark.hcunit_members_dashboard_my_sessions
             ]

#@pytest.mark.registereduser
class TestHcunitMembersDashboardMySession(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        # start up a tool session container
        self.username,self.userpass = \
            self.testdata.find_account_for('registeredworkspace')

        cm = hubcheck.shell.ContainerManager()
        self.ws = cm.access(host=self.https_uri,
                            username=self.username,
                            password=self.userpass)

        self.session_number,es = self.ws.execute('echo $SESSION')

        # setup a web browser
        self.browser.get(self.https_authority)

        self.utils.account.login_as(self.username,self.userpass)

        self.po = self.catalog.load_pageobject('GenericPage')
        self.po.header.goto_myaccount()

        self.po = self.catalog.load_pageobject('MembersDashboardPage')

        self.my_sessions_module = self.po.modules.my_sessions


    def teardown_method(self,method):

        # get out of the workspace
        # shut down the ssh connection
        self.ws.close()


    def test_session_items(self):
        """
        iterate through all session items, with no open sessions
        """

        for session_item in self.my_sessions_module.session_items():
            assert session_item is not None, \
                "while iterating through session list, session_item is None"


    def test_count_sessions(self):
        """
        count the number of open sessions
        """

        session = hubcheck.shell.ToolSession(host=self.https_uri,
                                       username=self.username,
                                       password=self.userpass)
        details = session.get_open_session_detail()
        expected = len(details.keys())
        del(session)
        count = self.my_sessions_module.count_sessions()
        assert count == expected, \
            "while counting the number of open sessions,"\
            + " received: %s, expected: %d" % (count,expected)


    def test_get_session_titles(self):
        """
        retrieve the session titles
        """

        titles = self.my_sessions_module.get_session_titles()
        assert len(titles) != 0, \
            "retrieving the session titles returned an empty list"


    def test_get_session_numbers(self):
        """
        retrieve a list of open sessions
        """

        session_nums = self.my_sessions_module.get_session_numbers()

        assert len(session_nums) != 0, \
            "retrieving a list of open session numbers produced an empty list"


    def test_get_session_by_position(self):
        """
        retrieve a session item object by position
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        assert session_item is not None, \
            "retrieving a session item object by position returned None"


    def test_get_session_by_session_number(self):
        """
        retrieve a session item object by session_number
        """

        session_item = self.my_sessions_module.get_session_by_session_number(
                        self.session_number)

        assert session_item is not None, \
            "retrieving a session item object by valid" \
            + " session_number returned None"

        snum = session_item.get_session_number()

        assert int(self.session_number) == snum, \
            "retrieving a session item object by valid" \
            + " session_number returned the wrong session" \
            + " self.session_number = %d, session_item's session number = %d" \
            % (int(self.session_number),snum)


    def test_get_session_by_session_number_invalid_session(self):
        """
        retrieve a session item object by session_number
        """

        invalid_session_number = 0
        session_item = self.my_sessions_module.get_session_by_session_number(
                        invalid_session_number)

        if session_item is not None:
            snum = session_item.get_session_number()
        else:
            snum = None

        assert session_item is None, \
            "retrieving a session item object by invalid" \
            + " session_number returned a session_item with session number: %s" \
            % (snum)


    def test_manage_storage(self):
        """
        click the link to navigate to storage management page
        """

        pageurl1 = self.po.current_url()

        self.my_sessions_module.manage_storage()

        pageurl2 = self.po.current_url()

        assert pageurl1 != pageurl2, \
            "after clicking the manage storage link on %s," % (pageurl1) \
            + " url did not change: pageurl1 = %s, pageurl2 = '%s'" \
            % (pageurl1,pageurl2)


    def test_storage_amount(self):
        """
        retrieve the free storage amount
        """

        storage_amount = self.my_sessions_module.storage_amount()

        assert storage_amount != '', \
            "invalid storage amount returned: %s" % (storage_amount)


#@pytest.mark.registereduser
class TestHcunitMembersDashboadMySessionItem(hubcheck.testcase.TestCase2):


    def setup_method(self,method):

        # start up a tool session container
        self.username,self.userpass = \
            self.testdata.find_account_for('registeredworkspace')

        cm = hubcheck.shell.ContainerManager()
        self.ws = cm.access(host=self.https_uri,
                            username=self.username,
                            password=self.userpass)

        # setup a web browser
        self.browser.get(self.https_authority)

        self.utils.account.login_as(self.username,self.userpass)

        self.po = self.catalog.load_pageobject('GenericPage')
        self.po.header.goto_myaccount()

        self.po = self.catalog.load_pageobject('MembersDashboardPage')

        self.my_sessions_module = self.po.modules.my_sessions


    def teardown_method(self,method):

        # get out of the workspace
        # shut down the ssh connection
        self.ws.close()


    def test_value(self):
        """
        retrieve the "value" of a my_session_item object
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        v = session_item.value()

        assert len(v['title']) != 0, "session item title is empty"
        assert type(v['access_time']) == datetime.datetime, \
            "session item access_time datetime object of type: %s" % \
            (type(v['access_time']))
        assert v['session_owner'] is None or v['session_owner'] != '', \
            "session item session_owner is %s, expected None or not blank" % \
            (v['session_owner'])
        assert v['session_number'] > 0, \
            "invalid session item session_number: %d" % \
            (v['session_number'])


    def test_quick_launch(self):
        """
        click the quick launch link
        """

        pageurl1 = self.po.current_url()

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_item.quick_launch_session()

        pageurl2 = self.po.current_url()
        assert pageurl1 != pageurl2, \
            "after quick launch link for session," \
            + " url did not change: pageurl1 = %s, pageurl2 = '%s'" \
            % (pageurl1,pageurl2)



    def test_get_title(self):
        """
        retrieve the title of the session
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        title = session_item.get_title()

        assert title is not None and title != '', \
            "invalid title returned: %s" % (title)


    def test_toggle_slide(self):
        """
        open or close the slide down window
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_item.toggle_slide()


    def test_is_slide_open(self):
        """
        check if the slid down window is open
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        is_open_1 = session_item.is_slide_open()
        session_item.toggle_slide()
        is_open_2 = session_item.is_slide_open()

        assert is_open_1 is not is_open_2, \
            "after toggling the slide down window is_open_1 == is_open_2:" \
            + " is_open_1 = %s, is_open_2 = %s" \
            % (is_open_1,is_open_2)


    def test_get_last_accessed(self):
        """
        retrieve the last accessed date time stamp
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        (dt1,dt2) = session_item.get_last_accessed()

        assert dt1 is not None and dt1 != '', \
            "invalid text date time stamp: dt1 = %s" % (dt1)
        assert type(dt2) == datetime.datetime, \
            "invalid text date time stamp type: type(dt2) = %s" % (type(dt2))


    def test_get_session_owner(self):
        """
        retrieve the session owner if it exists (should not for sessions we own)
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_owner = session_item.get_session_owner()

        assert session_owner is None or session_owner != '', \
            "session_owner is %s, expected None or not blank" % (session_owner)


    def test_get_session_number(self):
        """
        retrieve the session number
        """

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_number = session_item.get_session_number()

        assert session_number is None or session_number > 0, \
            "session_number is %s, expected None or a positive integer" \
            % (session_number)


    def test_resume(self):
        """
        click the resume session link
        """

        pageurl1 = self.po.current_url()

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_item.resume_session()

        pageurl2 = self.po.current_url()
        assert pageurl1 != pageurl2, \
            "after clicking the resume link for session," \
            + " url did not change: pageurl1 = %s, pageurl2 = '%s'" \
            % (pageurl1,pageurl2)



    def test_terminate(self):
        """
        click the terminate session link
        """

        pageurl1 = self.po.current_url()

        session_item = self.my_sessions_module.get_session_by_position(0)
        session_item.terminate_session()


#    def test_disconnect(self):
#        """
#        click the disconnect session link for a shared session
#        """
#
#        pageurl1 = self.po.current_url()
#
#        session_item = self.my_sessions_module.get_session_by_position(0)
#        session_item.disconnect_session()


#@pytest.mark.registereduser
class TestHcunitMembersDashboardMySessionStorage(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        self.username,self.userpass = \
            self.testdata.find_account_for('registeredworkspace')

        # setup a web browser
        self.browser.get(self.https_authority)

        # navigate to the member dashboard page
        self.utils.account.login_as(self.username,self.userpass)

        self.po = self.catalog.load_pageobject('GenericPage')
        self.po.header.goto_myaccount()

        self.po = self.catalog.load_pageobject('MembersDashboardPage')

        self.my_sessions_module = self.po.modules.my_sessions


    def test_goto_manage(self):
        """
        click the link to navigate to storage management page
        """

        pageurl1 = self.po.current_url()

        self.my_sessions_module.storage.goto_manage()

        pageurl2 = self.po.current_url()

        assert pageurl1 != pageurl2, \
            "after clicking the manage storage link," \
            + " url did not change: pageurl1 = %s, pageurl2 = '%s'" \
            % (pageurl1,pageurl2)


    def test_storage_meter(self):
        """
        retrieve the free storage amount
        """

        storage_amount = self.my_sessions_module.storage.storage_meter()

        assert storage_amount != '', \
            "invalid storage amount returned: %s" % (storage_amount)
