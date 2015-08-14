import unittest
import pytest
import sys
import hubcheck
import logging


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.pageobjects,
             ]


@pytest.mark.hcunit_generic_page
class TestGenericPage(hubcheck.testcase.TestCase2):


    def setup_method(self,method):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('registeredworkspace')

        self.po = self.catalog.load_pageobject('GenericPage')


    def testLoggedInHeaderLocators(self):
        """
        check header locators for a generic page
        while logged in
        """

        self.utils.account.login_as(self.username,self.password)
        self.po.header._checkLocatorsLoggedIn()


    def testLoggedOutHeaderLocators(self):
        """
        check header locators for a generic page
        while logged out
        """

        self.po.header._checkLocatorsLoggedOut()


    def testGotoLoginFunction(self):
        """
        click the login link
        """

        startpageurl = self.po.current_url()
        self.po.set_page_load_marker()
        self.po.goto_login()
        self.po.wait_for_page_to_load()
        endpageurl = self.po.current_url()
        assert startpageurl != endpageurl, \
            "User was not taken to the login webpage, url == %s\n" % endpageurl


    def testGotoRegisterFunction(self):
        """
        click the register link
        """

        startpageurl = self.po.current_url()
        self.po.set_page_load_marker()
        self.po.goto_register()
        self.po.wait_for_page_to_load()
        endpageurl = self.po.current_url()
        assert startpageurl != endpageurl, \
            "User was not taken to the register webpage, url == %s\n" % endpageurl


    def testGotoLogoutFunction(self):
        """
        click the logout link
        """

        self.utils.account.login_as(self.username,self.password)
        startpageurl = self.po.current_url()
        self.po.set_page_load_marker()
        self.po.goto_logout()
        self.po.wait_for_page_to_load()
        endpageurl = self.po.current_url()
        assert startpageurl != endpageurl, \
            "User was not taken to the logout webpage, url == %s\n" % endpageurl


    def testGotoMyAccountFunction(self):
        """
        click the my account link
        """

        self.utils.account.login_as(self.username,self.password)
        self.po.goto_page()
        startpageurl = self.po.current_url()
        self.po.set_page_load_marker()
        self.po.goto_myaccount()
        self.po.wait_for_page_to_load()
        endpageurl = self.po.current_url()
        assert startpageurl != endpageurl, \
            "User was not taken to the myaccount webpage, url == %s\n" % endpageurl


    def testGotoProfileFunction(self):
        """
        click the profile link
        """

        self.utils.account.login_as(self.username,self.password)
        self.po.goto_page()
        startpageurl = self.po.current_url()
        self.po.set_page_load_marker()
        self.po.goto_profile()
        self.po.wait_for_page_to_load()
        endpageurl = self.po.current_url()
        assert startpageurl != endpageurl, \
            "User was not taken to the profile webpage, url == %s\n" % endpageurl


    def testIsLoggedInFunction(self):
        """
        login and check if the user is logged in using is_logged_in()
        """

        self.utils.account.login_as(self.username,self.password)
        flag = self.po.is_logged_in()
        assert flag is True, \
            "is_logged_in() returned %s, expected True" % (flag)


    def testIsLoggedInFunction2(self):
        """
        try the is_logged_in() function while not logged in.
        """

        flag = self.po.is_logged_in()
        assert flag is False, \
            "is_logged_in() returned %s, expected False" % (flag)


    def testGetErrorInfoFunction(self):
        """
        try the get_error_info() function, no error
        """

        errorinfo = self.po.get_error_info()
        assert len(errorinfo) == 0, \
            "get_error_info() returned %s, expected []" % (errorinfo)


    def testGetErrorInfoFunction2(self):
        """
        try the get_error_info() function, with error
        """

        po = self.catalog.load_pageobject('RegisterPage')
        po.goto_page()
        po.register_account({})
        errorinfo = po.get_error_info()
        assert len(errorinfo) > 0, \
            "get_error_info() returned %s, expected an error" % (errorinfo)


    def testGetErrorBoxInfoFunction(self):
        """
        try the get_errorbox_info() function, no error
        """

        errorinfo = self.po.get_errorbox_info()
        assert len(errorinfo) == 0, \
            "get_errorbox_info() returned %s, expected []" % (errorinfo)


    def testGetErrorBoxInfoFunction2(self):
        """
        try the get_errorbox_info() function, with error
        """

        self.po.goto_page('/hubcheck_page_that_should_never_ever_exist')
        errorinfo = self.po.get_errorbox_info()
        assert len(errorinfo) > 0, \
            "get_errorbox_info() returned %s, expected an error" % (errorinfo)


