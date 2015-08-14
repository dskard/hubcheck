from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Link

class HubUCourseMembershipListingMemberRow(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseMembershipListingMemberRow,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseMembershipListingMemberRow_Locators = \
            self.load_class('HubUCourseMembershipListingMemberRow_Locators')

        # update this object's locator
        self.locators.update(HubUCourseMembershipListingMemberRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.cb_email        = Checkbox(self,{'base':'cb_email'})
        self.name            = Link(self,{'base':'name'})

        # update the component's locators with this objects overrides
        self._updateLocators()

class HubUCourseMembershipListingMemberRow_Locators_Base(object):
    """locators for HubUCoursMembershipListingMemberRow object"""

    locators = {
        'base'       : "css=.member-details",
        'cb_email'   : "css=input[name='enrollee[]']",
        'name'       : "css=td.fLink strong",
    }

