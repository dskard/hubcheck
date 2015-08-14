from hubcheck.pageobjects.po_hubucoursemanage import HubUCourseManagePage

class HubUCourseManageInvitesPage(HubUCourseManagePage):
    """hub u course manager invites"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseManageInvitesPage,self).__init__(browser,catalog,groupid)

        # load hub's classes
        HubUCourseManageInvitesPage_Locators = self.load_class('HubUCourseManageInvitesPage_Locators')
        HubUCourseManageInvitesForm = self.load_class('HubUCourseManageInvitesForm')

        # update this object's locator
        self.locators.update(HubUCourseManageInvitesPage_Locators.locators)

        # setup page object's components
        self.form = HubUCourseManageInvitesForm(self,{'base':'emailform'})

    def goto_page(self):
        super(HubUCourseManageInvitesPage,self).goto_page()
        self.tabs.email.click()

    def send_email(self,tolist,templateName):
        self.form.send_email(tolist,templateName)

class HubUCourseManageInvitesPage_Locators_Base(object):
    """locators for HubUCourseManageInvitesPage object"""

    locators = {
        'emailform' : "css=#send-invite",
    }
