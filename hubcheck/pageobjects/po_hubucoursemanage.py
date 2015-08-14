from hubcheck.pageobjects.po_hubucoursebase import HubUCourseBasePage

class HubUCourseManagePage(HubUCourseBasePage):
    """home page for hubu course"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseManagePage,self).__init__(browser,catalog)
        self.groupid = groupid
        self.path = "/groups/%s/manage" % (self.groupid)

        # load hub's classes
        HubUCourseManagePage_Locators = self.load_class('HubUCourseManagePage_Locators')
        HubUCourseManageTabs          = self.load_class('HubUCourseManageTabs')

        # update this object's locator
        self.locators.update(HubUCourseManagePage_Locators.locators)

        # setup page object's components
        self.tabs   = HubUCourseManageTabs(self,{'base':'tabs'})

    def goto_dashboard(self):
        return self.tabs.goto_dashboard()

    def goto_calendar(self):
        self.tabs.goto_calendar()

    def goto_announcements(self):
        self.tabs.goto_announcements()

    def goto_membership(self):
        self.tabs.goto_membership()

    def goto_templates(self):
        self.tabs.goto_templates()

    def goto_email(self):
        self.tabs.goto_email()

class HubUCourseManagePage_Locators_Base(object):
    """locators for HubUCourseManagePage object"""

    locators = {
        'tabs' : "css=#tabbed-content",
    }
