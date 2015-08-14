from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

class DashboardMembership(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(DashboardMembership,self).__init__(owner,locatordict)

        # load hub's classes
        DashboardMembership_Locators = self.load_class('DashboardMembership_Locators')

        # update this object's locator
        self.locators.update(DashboardMembership_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.active_members   = TextReadOnly(self,{'base':'active'})
        self.pending_invitees = TextReadOnly(self,{'base':'pending'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def active_members_count(self):
        """get the number of active members"""

        return self.active_members.value


    def pending_invitees_count(self):
        """get the number of pending invitees"""

        return self.pending_invitees.value

class DashboardMembership_Locators_Base(object):
    """locators for DashboardMembership object"""

    locators = {
        'base'     : "css=#dashboard .membership",
        'active'   : "css=.active-members .count",
        'pending'  : "css=.pending-invitees .count",
    }
