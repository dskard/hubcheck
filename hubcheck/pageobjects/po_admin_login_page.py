from hubcheck.pageobjects.po_generic_page import GenericPage

class AdminLoginPage(GenericPage):
    """login page object"""

    def __init__(self,browser,catalog):
        super(AdminLoginPage,self).__init__(browser,catalog)
        self.path = '/administrator'

        # load hub's classes
        AdminLoginPage_Locators = self.load_class('AdminLoginPage_Locators')
        AdminLogin              = self.load_class('AdminLogin')
        AdminHeader             = self.load_class('AdminHeader')

        # update this object's locator
        self.locators.update(AdminLoginPage_Locators.locators)

        # setup page object's components
        self.auth = AdminLogin(self,{'base':'auth'})
        self.header = AdminHeader(self,{'base':'header'})

    def login_as(self,username,password):
        self.auth.login_as(username,password)
        self.header.logout.wait_until_visible()


class AdminLoginPage_Locators_Base(object):
    """locators for AdminLoginPage object"""

    locators = {
        'auth'  : "css=#form-login",
        'header' : "css=#header",
    }
