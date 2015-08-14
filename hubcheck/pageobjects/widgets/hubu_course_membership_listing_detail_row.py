from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Link

class HubUCourseMembershipListingDetailRow(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseMembershipListingDetailRow,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseMembershipListingDetailRow_Locators = \
            self.load_class('HubUCourseMembershipListingDetailRow_Locators')

        # update this object's locator
        self.locators.update(HubUCourseMembershipListingDetailRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.enroll_id       = TextReadOnly(self,{'base':'enroll_id'})
        self.enroll_date     = TextReadOnly(self,{'base':'enroll_date'})
        self.import_date     = TextReadOnly(self,{'base':'import_date'})
        self.invite_sent     = TextReadOnly(self,{'base':'invite_sent'})
        self.invite_accept   = TextReadOnly(self,{'base':'invite_accept'})
    #    self.invite_token    = TextReadOnly(self,{'base':'invite_token'})
        self.email           = Link(self,{'base':'email'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    #def _checkLocators(self,widgets=None,cltype=''):
    #    widgets = [self.enroll_id,self.enroll_date,self.import_date,
    #               self.invite_sent,self.invite_accept,self.email]
    #    super(HubUCourseMembershipListingDetailRow,self)._checkLocators(widgets,cltype)


class HubUCourseMembershipListingDetailRow_Locators_Base(object):
    """locators for HubUCoursMembershipListingDetailRow object"""

    locators = {
        'base'          : "css=tr.listing-details",
        'enroll_id'     : "css=table.important tr:nth-of-type(1) td:nth-of-type(1) span.value",
        'enroll_date'   : "css=table.important tr:nth-of-type(1) td:nth-of-type(2) span.value",
        'import_date'   : "css=table.important tr:nth-of-type(1) td:nth-of-type(3) span.value",
        'invite_sent'   : "css=table.important tr:nth-of-type(1) td:nth-of-type(4) span.value",
        'invite_accept' : "css=table.important tr:nth-of-type(1) td:nth-of-type(5) span.value",
        'invite_token'  : "css=.invite-link-with-token",
        'email'         : "css=a.email",
        'emails_sent'   : "css=div.emails",
        'emails_sent_row' : "css=tr",
    }

