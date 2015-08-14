from hubcheck.pageobjects.po_generic_page import GenericPage

class RegisterPage(GenericPage):
    """hub registration form"""

    def __init__(self,browser,catalog):
        super(RegisterPage,self).__init__(browser,catalog)
        self.path = "/register"

        # load hub's classes
        RegisterPage_Locators = self.load_class('RegisterPage_Locators')
        RegisterForm          = self.load_class('RegisterForm')

        # update this object's locator
        self.locators.update(RegisterPage_Locators.locators)

        # setup page object's components
        self.registerform = RegisterForm(self,{'base':'registerform'})

    def register_account(self,data):
        return self.registerform.register_account(data)

    def populate_form(self,data):
        return self.registerform.populate_form(data)

    def submit_form(self,data={}):
        return self.registerform.submit_form(data)

class RegisterPage_Locators_Base(object):
    """locators for RegisterPage object"""

    locators = {
        'registerform' : "css=#hubForm",
    }
