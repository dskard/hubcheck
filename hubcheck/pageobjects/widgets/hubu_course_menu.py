from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class HubUCourseMenu(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseMenu,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseMenu_Locators = self.load_class('HubUCourseMenu_Locators')

        # update this object's locator
        self.locators.update(HubUCourseMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.home        = Link(self,{'base':'home'})
        self.syllabus    = Link(self,{'base':'syllabus'})
        self.calendar    = Link(self,{'base':'calendar'})
        self.discussions = Link(self,{'base':'discussions'})
        self.faqs        = Link(self,{'base':'faqs'})
        self.support     = Link(self,{'base':'support'})
        self.manage      = Link(self,{'base':'manage'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        widgets = [self.home,self.support]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        widgets = [self.home,self.syllabus,self.calendar,self.discussions,
                   self.faqs,self.support,self.manage]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        widgets = [self.home,self.syllabus,self.calendar,self.discussions,
                   self.faqs,self.support]
        self._checkLocators(widgets,cltype)


    def goto_home(self):
        """click on the course menu's home link"""
        self.home.click()


    def goto_syllabus(self):
        """click on the course menu's syllabus link"""

        self.syllabus.click()


    def goto_calendar(self):
        """click on the course menu's calendar link"""

        self.calendar.click()


    def goto_discussions(self):
        """click on the course menu's discussions link"""

        self.discussions.click()


    def goto_faqs(self):
        """click on the course menu's faq link"""

        self.faqs.click()


    def goto_support(self):
        """click on the course menu's support link"""

        self.support.click()


    def goto_manage(self):
        """click on the course menu's manage link"""

        self.manage.click()


class HubUCourseMenu_Locators_Base(object):
    """locators for HubUCourseMenu object"""

    locators = {
        'base'          : "css=#course-menu",
        'home'          : "css=.course-home",
        'syllabus'      : "css=.course-syllabus",
        'calendar'      : "css=.course-calendar",
        'discussions'   : "css=.course-discussions",
        'faqs'          : "css=.course-faqs",
        'support'       : "css=.course-support",
        'manage'        : "css=.course-manage",
    }

