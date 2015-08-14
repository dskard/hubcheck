from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class AdminHeader1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminHeader1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminHeader_Locators = self.load_class('AdminHeader_Locators')

        # update this object's locator defaults
        self.locators.update(AdminHeader_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.logout = Link(self,{'base':'logout'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_logout(self):
        self.logout.click()
        self.logout.wait_until_invisible()


class AdminHeader1_Locators_Base_1(object):
    """locators for AdminHeader1 object"""

    locators = {
        'base'    : "css=#header",
        'logout'  : "css=.logout",
    }
