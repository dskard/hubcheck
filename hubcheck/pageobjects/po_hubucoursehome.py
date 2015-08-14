from hubcheck.pageobjects.po_hubucoursebase import HubUCourseBasePage

class HubUCourseHomePage(HubUCourseBasePage):
    """home page for hubu course"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseHomePage,self).__init__(browser,catalog)
        self.groupid = groupid
        self.path = "/groups/%s" % (self.groupid)

        # load hub's classes
        HubUCourseHomePage_Locators = self.load_class('HubUCourseHomePage_Locators')
        HubUCourseLogin             = self.load_class('HubUCourseLogin')

        # update this object's locator
        self.locators.update(HubUCourseHomePage_Locators.locators)

        # setup page object's components
        self.login  = HubUCourseLogin(self,{'base':'login'})

    def login_as(self,username,password,remember=False):
        return self.login.login_as(username,password,remember)

class HubUCourseHomePage_Locators_Base(object):
    """locators for HubUCourseHomePage object"""

    locators = {
        'login' : "css=#course-login",
    }

