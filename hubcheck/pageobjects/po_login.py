from hubcheck.pageobjects.po_generic_page import GenericPage

class LoginPage1(GenericPage):
    def __init__(self,browser,catalog):
        super(LoginPage1,self).__init__(browser,catalog)
        self.path = '/login'

        # load hub's classes
        LoginPage_Locators = self.load_class('LoginPage_Locators')
        Login              = self.load_class('Login')

        # update this object's locator
        self.locators.update(LoginPage_Locators.locators)

        # setup page object's components
        self.auth         = Login(self,{'base':'auth'})

    def login_as(self,username,password,remember=False):
        self.auth.login_as(username,password,remember)


class LoginPage1_Locators_Base_1(object):
    """locators for LoginPage object"""

    locators = {
        'auth' : "css=#hubForm",
    }

class LoginPage1_Locators_Base_2(object):
    """locators for Login object"""

    locators = {
        'auth' : "css=#authentication",
    }

class LoginPage1_Locators_Base_3(object):
    """locators for Login object"""

    locators = {
        'auth' : "css=#login_form",
    }

class LoginPage1_Locators_Base_4(object):
    """locators for Login object"""

    locators = {
        'auth' : "css=.login_form",
    }

