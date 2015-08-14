from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Link

class AdminLogin1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminLogin1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminLogin_Locators = self.load_class('AdminLogin_Locators')

        # update this object's locator defaults
        self.locators.update(AdminLogin_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username  = Text(self,{'base':'username'})
        self.password  = Text(self,{'base':'password'})
        self.submit    = Link(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def login_as(self,username,password):
        self.username.value = username
        self.password.value = password
        self.submit.click()

class AdminLogin1_Locators_Base_1(object):
    """locators for AdminLogin1 object"""

    locators = {
        'base'      : "css=#form-login",
        'username'  : "css=#modlgn_username",
        'password'  : "css=#modlgn_passwd",
        'submit'    : "css=.next a",
    }

class AdminLogin1_Locators_Base_2(object):
    """locators for AdminLogin1 object hub version 1.2.0"""

    locators = {
        'base'      : "css=#form-login",
        'username'  : "css=#mod-login-username",
        'password'  : "css=#mod-login-password",
        'submit'    : "css=.next a",
    }

