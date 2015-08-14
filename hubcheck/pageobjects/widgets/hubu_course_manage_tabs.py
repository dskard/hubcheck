from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class HubUCourseManageTabs(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseManageTabs,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseManageTabs_Locators = self.load_class('HubUCourseManageTabs_Locators')

        # update this object's locator
        self.locators.update(HubUCourseManageTabs_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.dashboard      = Link(self,{'base':'dashboard'})
        self.calendar       = Link(self,{'base':'calendar'})
        self.announcements  = Link(self,{'base':'announcements'})
        self.membership     = Link(self,{'base':'membership'})
        self.templates      = Link(self,{'base':'templates'})
        self.email          = Link(self,{'base':'email'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_dashboard(self):
        """click the hubu course dashboard link"""

        self.dashboard.click()


    def goto_calendar(self):
        """click the hubu course calendar link"""

        self.calendar.click()


    def goto_announcements(self):
        """click the hubu course announcements link"""

        self.announcements.click()


    def goto_membership(self):
        """click the hubu course membership link"""

        self.membership.click()


    def goto_templates(self):
        """click the hubu course templates link"""

        self.templates.click()


    def goto_email(self):
        """click the hubu course email link"""

        self.email.click()


class HubUCourseManageTabs_Locators_Base(object):
    """locators for HubUCourseManageTabs object"""

    locators = {
        'base'          : "css=#tabbed-content",
        'dashboard'     : "css=a[title='Manager Dashboard']",
        'calendar'      : "css=a[title='Calendar']",
        'announcements' : "css=a[title='Announcements']",
        'membership'    : "css=a[title='Membership']",
        'templates'     : "css=a[title='Email Templates']",
        'email'         : "css=a[title='Send Invites']",
    }

