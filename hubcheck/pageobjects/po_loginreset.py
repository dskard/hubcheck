from hubcheck.pageobjects.po_generic_page import GenericPage

class LoginResetPage(GenericPage):
    """login remind page"""

    def __init__(self,browser,catalog):
        super(LoginResetPage,self).__init__(browser,catalog)
        self.path = "/login/reset"

        # load hub's classes
        LoginResetPage_Locators = self.load_class('LoginResetPage_Locators')
        LoginResetForm          = self.load_class('LoginResetForm')

        # update this object's locator
        self.locators.update(LoginResetPage_Locators.locators)

        # setup page object's components
        self.form         = LoginResetForm(self,{'base':'form'})

    def email_verification_token(self,username):
        return self.form.email_verification_token(username)

class LoginResetPage_Locators_Base(object):
    """locators for LoginResetPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
