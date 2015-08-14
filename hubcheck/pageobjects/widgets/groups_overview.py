from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class GroupsOverview1(BasePageWidget):
    """
    Groups Overview widget for hub versions 1.0 to 1.1.2
    """
    def __init__(self, owner, locatordict={}):
        super(GroupsOverview1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsOverview_Locators = self.load_class('GroupsOverview_Locators')
        GroupsMemberBrowser = self.load_class('GroupsMemberBrowser')

        # update this object's locator
        self.locators.update(GroupsOverview_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.toggledesc     = Link(self,{'base':'toggledesc'})
        self.publicdesc     = TextReadOnly(self,{'base':'publicdesc'})
        self.privatedesc    = TextReadOnly(self,{'base':'privatedesc'})
        self.viewallmembers = Link(self,{'base':'viewallmembers'})
        self.memberbrowser  = GroupsMemberBrowser(self,{'base':'memberbrowser'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_member_names(self):
        """return the names of group members"""

        return self.memberbrowser.get_member_names()


    def goto_member_profile(self,membername):
        """click on a group member's profile link"""

        return self.memberbrowser.goto_member_profile(membername)


class GroupsOverview1_Locators_Base(object):
    """locators for GroupsOverview object"""

    locators = {
        'base'              : "css=.group_overview",
        'toggledesc'        : "css=#toggle_description",
        'publicdesc'        : "css=#description #public",
        'privatedesc'       : "css=#description #private",
        'viewallmembers'    : "xpath=//a[contains(text(), 'View all members')]",
        'memberbrowser'     : "css=#member_browser",
    }

class GroupsOverview2(BasePageWidget):
    """
    Groups Overview widget for hub version 1.1.5
    """
    def __init__(self, owner, locatordict={}):
        super(GroupsOverview2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsOverview_Locators = self.load_class('GroupsOverview_Locators')
        GroupsMemberBrowser = self.load_class('GroupsMemberBrowser')

        # update this object's locator
        self.locators.update(GroupsOverview_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.description    = TextReadOnly(self,{'base':'description'})
        self.viewallmembers = Link(self,{'base':'viewallmembers'})
        self.memberbrowser  = GroupsMemberBrowser(self,{'base':'memberbrowser'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_member_names(self):
        """return the names of group members"""

        return self.memberbrowser.get_member_names()


    def goto_member_profile(self,membername):
        """click on a group member's profile link"""

        return self.memberbrowser.goto_member_profile(membername)


class GroupsOverview2_Locators_Base(object):
    """
    locators for GroupsOverview object
    removed public and private description.
    addded generic description
    """

    locators = {
        'base'              : "css=.group_overview",
        'description'       : "css=#description",
        'viewallmembers'    : "css=.group-content-header-extra a",
        'memberbrowser'     : "css=#member_browser",
    }

