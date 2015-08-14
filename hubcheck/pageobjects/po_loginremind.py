from hubcheck.pageobjects.po_generic_page import GenericPage

class LoginRemindPage(GenericPage):
    """login remind page"""

    def __init__(self,browser,catalog):
        super(LoginRemindPage,self).__init__(browser,catalog)
        self.path = "/login/remind"

        # load hub's classes
        LoginRemindPage_Locators = self.load_class('LoginRemindPage_Locators')
        LoginRemindForm          = self.load_class('LoginRemindForm')

        # update this object's locator
        self.locators.update(LoginRemindPage_Locators.locators)

        # setup page object's components
        self.form = LoginRemindForm(self,{'base':'form'})

    def recover_username(self,email):
        return self.form.recover_username(email)

class LoginRemindPage_Locators_Base(object):
    """locators for LoginRemindPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
