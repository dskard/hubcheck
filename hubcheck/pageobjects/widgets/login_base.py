from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Text

from selenium.common.exceptions import TimeoutException

class Login(FormBase):
    def __init__(self, owner, locatordict={}):
        super(Login,self).__init__(owner,locatordict)

        # load hub's classes
        Login_Locators = self.load_class('Login_Locators')

        # update this object's locator
        self.locators.update(Login_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username  = Text(self,{'base':'username'})
        self.password  = Text(self,{'base':'password'})
        self.remember  = Checkbox(self,{'base':'remember'})
        self.remind    = Link(self,{'base':'remind'})
        self.reset     = Link(self,{'base':'reset'})
        self.register  = Link(self,{'base':'register'})

        self.fields += ['username','password','remember']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def login_as(self,username,password,remember=False):
        """login to the website using the provided credentials"""

        self.logger.debug("browser logging in as user \"%s\"" % (username))
        data = {
            'username'  : username,
            'password'  : password,
        }

        # handle login forms that don't have remember links
        # like purduehubu
        if self.remember.is_present():
            data['remember'] = remember

        self.submit_form(data)

        # we use the presence of the username and password fields
        # as a hint that are still logging in. check the password
        # field first because whatever page we land on after login
        # probably won't have a password field, but if it does
        # we then check for the username field. different hubs
        # land on different pages, and these pages may use the same
        # locator as the username or password field. hopefully the
        # probability of the landing page having both is low.
        # another solution is to just let the login_as function perform
        # the login, and let another function go to the myaccount
        # or dashboard page and check for the logout link.
        # we user the username and password fields because some hubs
        # seem to hide the logout link (manufacturinghub)
        try:
            message = 'while verifying login: password field still present'
            self.password.wait_until_not_present(message)
        except TimeoutException:
            message = 'while verifying login: username and' \
                    + ' password fields still present'
            self.username.wait_until_not_present(message)


class Login_Locators_Base(object):
    """locators for Login object"""
    # nobody seems to be using this one anymore

    locators = {
        'base'      : "css=form[id='hubForm']",
        'username'  : "css=input[id='username']",
        'password'  : "css=input[id='passwd']",
        'remember'  : "css=input[id='remember']",
        'submit'    : "css=input[name='Submit']",
        'remind'    : "css=fieldset p:nth-child(1) a",
        'reset'     : "css=fieldset p:nth-child(2) a ",
        'register'  : "css=div.explanation p:nth-child(1) a",
    }


class Login_Locators_Base_2(object):
    """locators for Login object"""
    # nobody seems to be using this one anymore

    locators = {
        'base'      : "css=#login_form",
        'username'  : "css=#usernm",
        'password'  : "css=#password",
        'remember'  : "css=#remember",
        'submit'    : "css=p.submission input[type='submit']",
        'remind'    : "css=p.forgots a:nth-child(1)",
        'reset'     : "css=p.forgots a:nth-child(2)",
        'register'  : "css=p.callToAction a",
    }

class Login_Locators_Base_3(object):
    """locators for Login object"""
    # https://core.hubzero.org/login
    # https://stage.neeshub.org/login
    # https://ccehub.org/login
    # https://drinet.hubzero.org/login
    # https://manufacturinghub.org/login
    # https://courses.purduenext.purdue.edu/login

    locators = {
        'base'      : "css=#login_form",
        'username'  : "css=#username",
        'password'  : "css=#password",
        'remember'  : "css=#remember",
        'submit'    : "css=#login-submit",
        'remind'    : "css=.forgot-username",
        'reset'     : "css=.forgot-password",
        'register'  : "css=p.callToAction a",
    }


class Login_Locators_Base_4(object):
    """locators for HubUHubLogin object"""
    # https://c3bio.org/login

    locators = {
        'base'      : "css=#hubForm",
        'username'  : "css=#username",
        'password'  : "css=#passwd",
        'remember'  : "css=#remember",
        'submit'    : "css=#hubForm input[type='submit']",
        'remind'    : "xpath=//a[contains(text(), 'Forgot your Username?')]",
        'reset'     : "xpath=//a[contains(text(), 'Forgot your Password?')]",
        'register'  : "xpath=//a[contains(text(),'Register')]",
    }


class Login2(FormBase):
    """
    login page found on nanohub.org where the user must choose their login
    method before filling out the login form. This object works for local
    HUB login.
    """

    def __init__(self, owner, locatordict={}):
        super(Login2,self).__init__(owner,locatordict)

        # load hub's classes
        Login_Locators = self.load_class('Login_Locators')

        # update this object's locator
        self.locators.update(Login_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.change_account = Link(self,{'base':'change_account'})
        self.hub_signin = Link(self,{'base':'hub_signin'})
        self.username  = Text(self,{'base':'username'})
        self.password  = Text(self,{'base':'password'})
        self.remember  = Checkbox(self,{'base':'remember'})
        self.remind    = Link(self,{'base':'remind'})
        self.reset     = Link(self,{'base':'reset'})
        self.register  = Link(self,{'base':'register'})

        self.fields += ['username','password','remember']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def login_as(self,username,password,remember=False):
        """login to the website using the provided credentials"""

        self.logger.debug("browser logging in as user \"%s\"" % (username))
        data = {
            'username'  : username,
            'password'  : password,
        }

        # handle login forms that don't have remember links
        # like purduehubu
        if self.remember.is_present():
            data['remember'] = remember


        # reset the login user if necessary
        # if a user has previously logged in,
        # their username/email is hard coded in the form.
        # this clicks the "sign in with a different account" link
        if self.change_account.is_displayed():
            self.change_account.click()
            message = 'while changing hub account'
            self.change_account.wait_until_invisible(message)

        # enable the hidden hub login form
        if self.hub_signin.is_displayed():
            self.hub_signin.click()
            message = 'while choosing local hub login'
            self.hub_signin.wait_until_invisible(message)

        # populate the hub login form
        self.submit_form(data)

        # we use the presence of the username and password fields
        # as a hint that are still logging in. check the password
        # field first because whatever page we land on after login
        # probably won't have a password field, but if it does
        # we then check for the username field. different hubs
        # land on different pages, and these pages may use the same
        # locator as the username or password field. hopefully the
        # probability of the landing page having both is low.
        # another solution is to just let the login_as function perform
        # the login, and let another function go to the myaccount
        # or dashboard page and check for the logout link.
        # we user the username and password fields because some hubs
        # seem to hide the logout link (manufacturinghub)
        try:
            message = 'while verifying login: password field still present'
            self.password.wait_until_not_present(message)
        except TimeoutException:
            message = 'while verifying login: username and' \
                    + ' password fields still present'
            self.username.wait_until_not_present(message)


class Login2_Locators_Base_1(object):
    """locators for Login object"""
    # https://nanohub.org/login

    locators = {
        'base'      : "css=.login_form",
        'change_account' : "css=.others a",
        'hub_signin' : "css=.local a",
        'username'  : "css=#username",
        'password'  : "css=#password",
        'remember'  : "css=#remember",
        'submit'    : "css=.login-submit",
        'remind'    : "css=.forgot-username",
        'reset'     : "css=.forgot-password",
        'register'  : "css=.create .register",
    }

