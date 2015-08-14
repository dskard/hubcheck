from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class MembersPageMenu(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersPageMenu,self).__init__(owner,locatordict)

        # load hub's classes
        MembersPageMenu_Locators = self.load_class('MembersPageMenu_Locators')

        # update this object's locator
        self.locators.update(MembersPageMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.dashboardlink      = Link(self,{'base':'dashboard'})
        self.profilelink        = Link(self,{'base':'profile'})
        self.contributionslink  = Link(self,{'base':'contributions'})
        self.groupslink         = Link(self,{'base':'groups'})
        self.favoriteslink      = Link(self,{'base':'favorites'})
        self.messageslink       = Link(self,{'base':'messages'})
        self.resumelink         = Link(self,{'base':'resume'})
        self.bloglink           = Link(self,{'base':'blog'})
        self.projectslink       = Link(self,{'base':'projects'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def dashboard(self):
        """click the account dashboard link"""

        self.dashboardlink.click()


    def profile(self):
        """click the account profile link"""

        self.profilelink.click()


    def contributions(self):
        """click the account contributions link"""

        self.contributionslink.click()


    def groups(self):
        """click the account groups link"""

        self.groupslink.click()


    def favorites(self):
        """click the account favorites link"""

        self.favoriteslink.click()


    def messages(self):
        """click the account messages link"""

        self.messageslink.click()


    def resume(self):
        """click the account resume link"""

        self.resumelink.click()


    def blog(self):
        """click the account blog link"""

        self.bloglink.click()


    def projects(self):
        """click the account projects link"""

        self.projectslink.click()


class MembersPageMenu_Locators_Base(object):
    """locators for MembersPageMenu object"""

    locators = {
        'base'          : "css=#page_menu",
        'dashboard'     : "css=#page_menu .dashboard",
        'profile'       : "css=#page_menu .profile",
        'contributions' : "css=#page_menu .contributions",
        'groups'        : "css=#page_menu .groups",
        'favorites'     : "css=#page_menu .favorites",
        'messages'      : "css=#page_menu .messages",
        'resume'        : "css=#page_menu .resume",
        'blog'          : "css=#page_menu .blog",
        'projects'      : "css=#page_menu .projects",
    }
