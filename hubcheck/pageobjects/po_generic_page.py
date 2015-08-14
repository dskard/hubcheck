from hubcheck.pageobjects.basepageobject import BasePageObject
from hubcheck.pageobjects.basepageelement import Link
from selenium.common.exceptions import NoSuchElementException

class GenericPage(BasePageObject):
    """Generic Page with just a header and footer"""

    def __init__(self,browser,catalog):
        super(GenericPage,self).__init__(browser,catalog)
        self.path = '/'

        # load hub's classes
        GenericPage_Locators = self.load_class('GenericPage_Locators')
        NeedHelpForm = self.load_class('NeedHelpForm')
        Header = self.load_class('Header')
        Footer = self.load_class('Footer')

        # update this object's locator
        self.locators     = GenericPage_Locators.locators

        # setup page object's components
        self.needhelpform = NeedHelpForm(self,{},self.__refreshCaptchaCB)
        self.needhelplink = Link(self,{'base':'needhelplink'})
        self.header        = Header(self)
        # self.footer       = Footer(self)


    def __refreshCaptchaCB(self):
        self._browser.refresh()
        self.needhelplink.click()


    def goto_login(self):
        return self.header.goto_login()


    def goto_register(self):
        return self.header.goto_register()


    def goto_logout(self):
        return self.header.goto_logout()


    def goto_myaccount(self):
        return self.header.goto_myaccount()


    def goto_profile(self):
        return self.header.goto_profile()


    def toggle_needhelp(self):
        return self.needhelplink.click()


    def is_logged_in(self):
        """check if user is logged in, returns True or False"""
        return self.header.is_logged_in()


    def get_account_number(self):
        """return the account number of a logged in user based on urls"""

        if not self.is_logged_in():
            raise RuntimeError("user is not logged in")

        return self.header.get_account_number()


    def get_debug_info(self):
        rtxt = []
        for e in self.find_elements(self.locators['debug']):
            if e.is_displayed():
                rtxt.append(e.text)
        return rtxt


    def get_notification_info(self):
        rtxt = []
        for e in self.find_elements(self.locators['notification']):
            if e.is_displayed():
                rtxt.append(e.text)
        return rtxt


    def get_success_info(self):
        rtxt = []
        for e in self.find_elements(self.locators['success']):
            if e.is_displayed():
                rtxt.append(e.text)
        return rtxt


    def get_error_info(self):
        rtxt = []
        for e in self.find_elements(self.locators['error']):
            if e.is_displayed():
                rtxt.append(e.text)
        return rtxt


    def get_errorbox_info(self):
        rtxt = []
        for e in self.find_elements(self.locators['errorbox1']):
            if e.is_displayed():
                rtxt.append(e.text)
        for e in self.find_elements(self.locators['errorbox2']):
            if e.is_displayed():
                rtxt.append(e.text)
        return rtxt


class GenericPage_Locators_Base_1(object):
    """
    locators for GenericPage object
    """

    locators = {
        'needhelplink'  : "css=#tab",
        'debug'         : "css=#system-debug",
        'error'         : "css=.error",
        'success'       : "css=.passed",
        'notification'  : "css=#page_notifications",
        'errorbox1'     : "css=#errorbox",
        'errorbox2'     : "css=#error-box",
    }
