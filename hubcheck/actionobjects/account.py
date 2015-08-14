import re
import urlparse


class Account(object):

    def __init__(self, browser, catalog):

        self.browser = browser
        self.catalog = catalog
        self.logger = self.browser.logger
        self.__my_account_url = '/members/myaccount'


    def login_as(self,username,password,remember=False):

        self.logger.info("logging in as %s" % (username))

        LoginPage = self.catalog.load('LoginPage')
        po = LoginPage(self.browser,self.catalog)
        po.goto_page()
        po.login_as(username,password,remember)


    def logout(self):

        self.logger.info("logging out of website")

        self.goto_dashboard()

        MembersDashboardPage = self.catalog.load('MembersDashboardPage')
        po = MembersDashboardPage(self.browser,self.catalog)
        po.goto_logout()


    def goto_dashboard(self):

        self.logger.info("navigating to the dashboard page")

        GenericPage = self.catalog.load('GenericPage')
        po = GenericPage(self.browser,self.catalog)
        po.goto_page(self.__my_account_url)

        MembersDashboardPage = self.catalog.load('MembersDashboardPage')
        po = MembersDashboardPage(self.browser,self.catalog)
        po.menu.dashboard()


    def get_account_number(self):

        self.logger.info("retrieving account number")

        self.goto_dashboard()

        MembersDashboardPage = self.catalog.load('MembersDashboardPage')
        po = MembersDashboardPage(self.browser,self.catalog)
        url = po.current_url()

        path = urlparse.urlsplit(url)[2]
        if not path:
            raise RuntimeError("url '%s' has no path" % (url))

        matches = re.search("/members/(\d+)",path)
        if matches is None:
            raise RuntimeError("path '%s' does not contain an account number" % (path))

        account_number = matches.group(1)

        return account_number



