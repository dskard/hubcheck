import re
import urlparse

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from selenium.webdriver.common.action_chains import ActionChains

# from hubcheck.pageobjects.widgets.search import Search

class Header(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Header,self).__init__(owner,locatordict)

        # load hub's classes
        Header_Locators = self.load_class('Header_Locators')

        # update this object's locator
        self.locators.update(Header_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.login          = Link(self,{'base':'login'})
        self.register       = Link(self,{'base':'register'})
        self.logout         = Link(self,{'base':'logout'})
        self.myaccount      = Link(self,{'base':'myaccount'})

        # self.search    = Search(self,{'base':'search'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self):

        widgets = [self.login,self.register]
        self._checkLocators(widgets=widgets,cltype='LoggedOut')


    def _checkLocatorsLoggedIn(self):

        widgets = [self.logout,self.myaccount]
        self._checkLocators(widgets=widgets,cltype='LoggedIn')


    def goto_login(self):
        """click the login link"""

        return self.login.click()


    def goto_register(self):
        """click the register link"""

        return self.register.click()


    def goto_logout(self):
        """click the logout link"""

        self.logout.click()
        message = 'logout button visible while trying to logout'
        self.logout.wait_until_invisible(message)
        return


    def goto_myaccount(self):
        """click the link to go to the member's myaccount page"""

        return self.myaccount.click()


    def is_logged_in(self):
        """check if user is logged in, returns True or False"""

        return self.logout.is_displayed()


    def get_account_number(self):
        """return the user's account number based on the "My Account" url"""

        url = self.myaccount.get_attribute('href')
        if not url:
            raise RuntimeError("link '%s' has no href" % (self.myaccount.locator))

        path = urlparse.urlsplit(url)[2]
        if not path:
            raise RuntimeError("url '%s' has no path" % (url))

        matches = re.search("/members/(\d+)",path)
        if matches is None:
            raise RuntimeError("path '%s' does not contain an account number" % (path))

        account_number = matches.group(1)

        return account_number


class Header_Locators_Base(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a",
        'myaccount'     : "css=#myaccount a",
        'search'        : "css=#searchform",
    }


class Header_Locators_Base_2(object):
    """locators for Header object"""
    # https://manufacturinghub.org/login

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a:nth-child(1)",
        'myaccount'     : "css=#logout a:nth-child(2)",
        'search'        : "css=#searchform",
    }


class Header_Locators_Base_3(object):
    """
    locators for Header object

    used on polytechhub
    """

    locators = {
        'base'          : "css=#top",
        'login'         : "css=#account-login",
        'register'      : "css=#account-login",
        'logout'        : "css=#account-logout",
        'myaccount'     : "css=#account-info",
        'search'        : "css=#searchword",
    }


class Header_Locators_Base_4(object):
    """
    locators for Header object

    used on nanohub
    """

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login",
        'register'      : "css=#register",
        'logout'        : "css=#logout",
        'myaccount'     : "css=#usersname",
        'search'        : "css=#searchword",
    }


class Header1(Header):
    def __init__(self, owner, locatordict={}):
        super(Header1,self).__init__(owner,locatordict)

        # setup page object's additional components
        self.profile        = Link(self,{'base':'profile'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedIn(self):

        widgets = [self.logout,self.myaccount,self.profile]
        self._checkLocators(widgets=widgets,cltype='LoggedIn')


    def goto_profile(self):
        """click the link to go to the member's profile page"""

        return self.profile.click()



class Header1_Locators_Base(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a",
        'myaccount'     : "css=#myaccount a",
        'profile'       : "css=#username a",
        'search'        : "css=#searchform",
    }

class Header1_Locators_Base_2(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#account-login",
        'register'      : "css=#account-register",
        'logout'        : "css=#account-logout",
        'myaccount'     : "css=#account-dashboard",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header1_Locators_Base_4(object):
    """locators for geoshareproject"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#searchlogin > p > a:nth-child(1)",
        'register'      : "css=#searchlogin > p > a:nth-child(2)",
        'logout'        : "css=#searchlogin > p > a:nth-child(3)",
        'myaccount'     : "css=#searchlogin > p > a:nth-child(2)",
        'profile'       : "css=#searchlogin > p > a:nth-child(1)",
        'search'        : "css=#searchForm",
    }


class Header1_Locators_Base_5(object):
    """locators for Header object
       login and register are the same link
    """

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#register a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a",
        'myaccount'     : "css=#myaccount a",
        'profile'       : "css=#username a",
        'search'        : "css=#searchform",
    }


class Header2(BasePageWidget):
    """
    represents header on hubs that use a javascripty dropdown
    menu to hold account links for dashboard, profile, messages
    and logout.
    """

    def __init__(self, owner, locatordict={}):
        super(Header2,self).__init__(owner,locatordict)

        # load hub's classes
        Header_Locators = self.load_class('Header_Locators')

        # update this object's locator
        self.locators.update(Header_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.login          = Link(self,{'base':'login'})
        self.register       = Link(self,{'base':'register'})
        self.logout         = Link(self,{'base':'logout'})
        self.details        = Link(self,{'base':'details'})
        self.dashboard      = Link(self,{'base':'dashboard'})
        self.messages       = Link(self,{'base':'messages'})
        self.profile        = Link(self,{'base':'profile'})

        # self.search    = Search(self,'search')

        self._links = ['details','dashboard','messages','profile','logout']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype=""):

        widgets = [self.login]
        self._checkLocators(widgets=widgets,cltype='LoggedOut')


    def _checkLocatorsLoggedIn(self,widgets=None,cltype=""):

        widgets = [self.logout,self.dashboard,
                   self.messages,self.profile]

        base = self.owner.find_element(self.locators['acctbase'])

        # hover mouse over the group manager toolbar to expand it
        actionProvider = ActionChains(self.owner._browser)\
                         .move_to_element(base)
        actionProvider.perform()

        # check for locators
        self._checkLocators(widgets=widgets,cltype='LoggedIn')


    def get_options_items(self):

        return self._links


    def goto_options_item(self,link):
        """this function does selenium specific stuff"""

        if not link in self._links:
            raise ValueError("invalid link name: '%s'",link)

        # hover mouse over the account toolbar to expand it
        # move the mouse to the correct link and click it

        menu = self.find_element(self.locators['acctbase'])
        loc = self.locators[link]
        menu_item = self.find_element(loc)

        self.logger.debug("moving mouse over account dropdown")
        self.logger.debug("clicking drowdown menu option '%s': %s" % (link,loc))

        actionProvider = ActionChains(self.owner._browser)\
                         .move_to_element(menu)\
                         .move_to_element(menu_item)\
                         .click()
        actionProvider.perform()


    def goto_login(self):

        return self.login.click()


    def goto_register(self):

        return self.register.click()


    def goto_logout(self):

        lockey = 'logout'
        self.goto_options_item(lockey)
        # wait until the element is no longer visible (ie. the menu has closed)
        # before proceeding to the next task
        loc = self.locators[lockey]
        self.wait_until_not_present(locator=loc)


    def goto_myaccount(self):

        # deprecated function, use goto_dashboard() instead
        return self.goto_options_item('dashboard')


    def goto_dashboard(self):

        return self.goto_options_item('dashboard')


    def goto_messages(self):

        return self.goto_options_item('messages')


    def goto_profile(self):

        return self.goto_options_item('profile')


    def is_logged_in(self):
        """check if user is logged in, returns True or False"""

        # return not self.login.is_displayed()
        return self.logout.is_present()

    def get_account_number(self):
        """return the user's account number based on the "Username" url"""

        url = None

        # use dashboard instead of details because some hubs (like catalyzecare)
        # don't make details a link.
        url = self.dashboard.get_attribute('href')

        if url is None:
            raise RuntimeError("link '%s' has no href" \
                % (self.details.locators['base']))

        path = urlparse.urlsplit(url)[2]
        if not path:
            raise RuntimeError("url '%s' has no path" % (url))

        # the url looks something like:
        # https://hubname.org/members/1234/dashboard
        matches = re.search("/members/(\d+)",path)
        if matches is None:
            raise RuntimeError("path '%s' does not contain an account number" \
                % (path))

        account_number = matches.group(1)

        return account_number


class Header2_Locators_Base(object):
    """locators for Header2 object"""

    locators = {
        'base'          : "css=#header",
        'acctbase'      : "css=#account",
        'login'         : "css=#account-login",
        'register'      : "css=#account-register",
        'logout'        : "css=#account-logout",
        'details'       : "css=#account-details",
        'dashboard'     : "css=#account-dashboard",
        'messages'      : "css=#account-messages",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_2(object):
    """locators for Header2 object"""

    locators = {
        'base'          : "css=#masthead",
        'acctbase'      : "css=#account",
        'login'         : "css=#account-login",
        'register'      : "css=#account-register",
        'logout'        : "css=#account-logout",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard",
        'messages'      : "css=#account-messages",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_3(object):
    """locators for Header2 object
       these are used in afrl
    """

    locators = {
        'base'          : "css=#utilities",
        'acctbase'      : "css=#account",
        'login'         : "css=#account-login",
        'register'      : "css=#account-register",
        'logout'        : "css=#account-logout",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard",
        'messages'      : "css=#account-messages",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_4(object):
    """locators for Header2 object"""

    locators = {
        'base'          : "css=#masthead",
        'acctbase'      : "css=#account",
        'login'         : "css=#login",
        'register'      : "css=#register",
        'logout'        : "css=#account-logout",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard",
        'messages'      : "css=#account-messages",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_5(object):
    """locators for Header2 object
       login and register is one link
    """

    locators = {
        'base'          : "css=#masthead",
        'acctbase'      : "css=#account",
        'login'         : "css=#account-login",
        'register'      : "css=#account-login",
        'logout'        : "css=#account-logout",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard",
        'messages'      : "css=#account-messages",
        'profile'       : "css=#account-profile",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_6(object):
    """locators for Header2 object
       login and register is one link
       updated locators to include anchor
    """

    locators = {
        'base'          : "css=#masthead",
        'acctbase'      : "css=#account",
        'login'         : "css=#account-login",
        'register'      : "css=#account-login",
        'logout'        : "css=#account-logout a",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard a",
        'messages'      : "css=#account-messages a",
        'profile'       : "css=#account-profile a",
        'search'        : "css=#searchform",
    }


class Header2_Locators_Base_7(object):
    """locators for Header2 object
       separate login and register links
       updated locators to include anchor
    """

    locators = {
        'base'          : "css=#masthead",
        'acctbase'      : "css=#account",
        'login'         : "css=#login",
        'register'      : "css=#register",
        'logout'        : "css=#account-logout a",
        'details'       : "css=.account-details",
        'dashboard'     : "css=#account-dashboard a",
        'messages'      : "css=#account-messages a",
        'profile'       : "css=#account-profile a",
        'search'        : "css=#searchform",
    }


class Header3(Header):
    """
    represents header on hubs where the username and my account links
    lead to the my account/dashboard page, and there is no profile link.
    generally found in older templates. here we use the username link
    to get the account number
    """

    def __init__(self, owner, locatordict={}):
        super(Header3,self).__init__(owner,locatordict)

        # setup page object's additional components
        self.username       = Link(self,{'base':'username'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedIn(self):

        widgets = [self.logout,self.myaccount,self.username]
        self._checkLocators(widgets=widgets,cltype='LoggedIn')


    def goto_username(self):
        """click the username link to go to the member's account page"""

        return self.username.click()


    def get_account_number(self):
        """return the user's account number based on the "Username" link"""

        url = self.username.get_attribute('href')
        if not url:
            raise RuntimeError("link '%s' has no href" % (self.username.locator))

        path = urlparse.urlsplit(url)[2]
        if not path:
            raise RuntimeError("url '%s' has no path" % (url))

        matches = re.search("/members/(\d+)",path)
        if matches is None:
            raise RuntimeError("path '%s' does not contain an account number" % (path))

        account_number = matches.group(1)

        return account_number


class Header3_Locators_Base_1(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a",
        'myaccount'     : "css=#myaccount a",
        'username'      : "css=#username a",
        'search'        : "css=#searchform",
    }

class Header3_Locators_Base_2(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#login a",
        'register'      : "css=#register a",
        'logout'        : "css=#logout a",
        'myaccount'     : "css=#myaccount a",
        'username'      : "css=#usersname a",
        'search'        : "css=#searchform",
    }

class Header3_Locators_Base_3(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#who > a:nth-child(1)",
        'register'      : "css=#who > a:nth-child(2)",
        'logout'        : "css=#account > a:nth-child(1)",
        'myaccount'     : "css=#account > a:nth-child(2)",
        'username'      : "css=#who > a:nth-child(1)",
        'search'        : "css=#sitesearch",
    }

class Header3_Locators_Base_4(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#header",
        'login'         : "css=#account-login",
        'register'      : "css=#account-register",
        'logout'        : "css=#account-logout",
        'myaccount'     : "css=#account-dashboard",
        'username'      : "css=#username",
        'search'        : "css=#sitesearch",
    }

