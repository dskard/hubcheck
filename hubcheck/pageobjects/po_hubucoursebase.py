from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class HubUCourseBasePage(GenericPage):
    """home page for hubu course"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseBasePage,self).__init__(browser,catalog)
        self.groupid = groupid
        self.path = "/groups/%s" % (self.groupid)

        # load hub's classes
        HubUCourseBasePage_Locators = self.load_class('HubUCourseBasePage_Locators')
        HubUCourseMenu              = self.load_class('HubUCourseMenu')

        # update this object's locator
        self.locators.update(HubUCourseBasePage_Locators.locators)

        # setup page object's components
        self.menu   = HubUCourseMenu(self,{'base':'menu'})
        self.logout = Link(self,{'base':'logout'})

    def goto_home(self):
        return self.menu.goto_home()

    def goto_syllabus(self):
        return self.menu.goto_syllabus()

    def goto_calendar(self):
        return self.menu.goto_calendar()

    def goto_discussions(self):
        return self.menu.goto_discussions()

    def goto_faqs(self):
        return self.menu.goto_faqs()

    def goto_support(self):
        return self.menu.goto_support()

    def goto_manage(self):
        return self.menu.goto_manage()

class HubUCourseBasePage_Locators_Base(object):
    """locators for HubUCourseBasePage object"""

    locators = {
        'menu'   : "css=#course-menu",
        'logout' : "css=div#logout a",
    }

