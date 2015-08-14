from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Link

class Captcha1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Captcha1,self).__init__(owner,locatordict)

        # load hub's classes
        Captcha1_Locators = self.load_class('Captcha1_Locators')

        # update this object's locator defaults
        self.locators.update(Captcha1_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.renew    = Link(self,{'base':'renew'})
        self.imagetxt = Text(self,{'base':'imagetxt'})
        # self.image   = Image(self,{'base':'image'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    @property
    def value(self):
        return None

    @value.setter
    def value(self, val):
        if val:
            solve()

    def refresh(self):
        self.refreshlink.click()

    def solve(self):
        pass

class Captcha1_Locators_Base(object):
    """locators for Captcha1 object"""

    locators = {
        'base'      : "css=.captcha-block",
        'renew'     : "css=.captcha-block a",
        'imagetxt'  : "css=#imgCatchaTxt0",
        'image'     : "css=#captchaCode0",
    }

