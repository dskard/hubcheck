from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class GroupsMenu1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsMenu1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsMenu_Locators = self.load_class('GroupsMenu_Locators')

        # update this object's locator
        self.locators.update(GroupsMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.overview       = Link(self,{'base':'overview'})
        self.members        = Link(self,{'base':'members'})
        self.nmembers       = TextReadOnly(self,{'base':'nmembers'})
        self.wiki           = Link(self,{'base':'wiki'})
        self.nwikis         = TextReadOnly(self,{'base':'nwikis'})
        self.resources      = Link(self,{'base':'resources'})
        self.nresources     = TextReadOnly(self,{'base':'nresources'})
        self.messages       = Link(self,{'base':'messages'})
        self.discussion     = Link(self,{'base':'discussion'})
        self.ndiscussions   = TextReadOnly(self,{'base':'ndiscussions'})
        self.blog           = Link(self,{'base':'blog'})
        self.wishlist       = Link(self,{'base':'wishlist'})
        self.calendar       = Link(self,{'base':'calendar'})

        self._menu_items = ['overview','members','wiki',
                            'resources','messages','discussion',
                            'blog','wishlist','calendar']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_menu_items(self):
        """return the menu link names"""

        return self._menu_items


    def goto_menu_item(self,menuitem):
        """click on a menu item"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        w.click()


    def is_menu_item_protected(self,menuitem):
        """check to see if the menu item is accessible by the user"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        return 'protected' in w.get_attribute('class')


class GroupsMenu1_Locators_Base(object):
    """locators for GroupsMenu object"""

    locators = {
        'base'              : "css=#page_menu",
        'overview'          : "css=.group-overview-tab",
        'members'           : "css=.group-members-tab",
        'nmembers'          : "css=.group-members-tab .count",
        'wiki'              : "css=.group-wiki-tab",
        'nwikis'            : "css=.group-wiki-tab .count",
        'resources'         : "css=.group-resources-tab",
        'nresources'        : "css=.group-resources-tab .count",
        'messages'          : "css=.group-messages-tab",
        'discussion'        : "css=.group-forum-tab",
        'ndiscussions'      : "css=.group-forum-tab .count",
        'blog'              : "css=.group-blog-tab",
        'wishlist'          : "css=.group-wishlist-tab",
        'calendar'          : "css=.group-calendar-tab",
    }


class GroupsMenu2(BasePageWidget):
    """
    Groups Menu for nees.org
    Adds datasharing and announcements links
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsMenu2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsMenu_Locators = self.load_class('GroupsMenu_Locators')

        # update this object's locator
        self.locators.update(GroupsMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.overview       = Link(self,{'base':'overview'})
        self.members        = Link(self,{'base':'members'})
        self.nmembers       = TextReadOnly(self,{'base':'nmembers'})
        self.wiki           = Link(self,{'base':'wiki'})
        self.nwikis         = TextReadOnly(self,{'base':'nwikis'})
        self.resources      = Link(self,{'base':'resources'})
        self.nresources     = TextReadOnly(self,{'base':'nresources'})
        self.messages       = Link(self,{'base':'messages'})
        self.discussion     = Link(self,{'base':'discussion'})
        self.ndiscussions   = TextReadOnly(self,{'base':'ndiscussions'})
        self.blog           = Link(self,{'base':'blog'})
        self.wishlist       = Link(self,{'base':'wishlist'})
        self.datasharing    = Link(self,{'base':'datasharing'})
        self.calendar       = Link(self,{'base':'calendar'})
        self.announcements  = Link(self,{'base':'announcements'})

        self._menu_items = ['overview','members','wiki',
                            'resources','messages','discussion',
                            'blog','wishlist','calendar',
                            'datasharing','announcements']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_menu_items(self):
        """return the menu link names"""

        return self._menu_items


    def goto_menu_item(self,menuitem):
        """click on a menu item"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        w.click()


    def is_menu_item_protected(self,menuitem):
        """check to see if the menu item is accessible by the user"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        return 'protected' in w.get_attribute('class')


class GroupsMenu2_Locators_Base(object):
    """locators for GroupsMenu object"""

    locators = {
        'base'              : "css=#page_menu",
        'overview'          : "css=.group-overview-tab",
        'members'           : "css=.group-members-tab",
        'nmembers'          : "css=.group-members-tab .count",
        'wiki'              : "css=.group-wiki-tab",
        'nwikis'            : "css=.group-wiki-tab .count",
        'resources'         : "css=.group-resources-tab",
        'nresources'        : "css=.group-resources-tab .count",
        'messages'          : "css=.group-messages-tab",
        'discussion'        : "css=.group-forum-tab",
        'ndiscussions'      : "css=.group-forum-tab .count",
        'blog'              : "css=.group-blog-tab",
        'wishlist'          : "css=.group-wishlist-tab",
        'datasharing'       : "css=.group-datasharing-tab",
        'calendar'          : "css=.group-calendar-tab",
        'announcements'     : "css=.group-announcements-tab",
    }


class GroupsMenu3(BasePageWidget):
    """
    Groups Menu for hub version 1.1.5
    Adds projects, announcements, collections
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsMenu3,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsMenu_Locators = self.load_class('GroupsMenu_Locators')

        # update this object's locator
        self.locators.update(GroupsMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.overview       = Link(self,{'base':'overview'})
        self.members        = Link(self,{'base':'members'})
        self.nmembers       = TextReadOnly(self,{'base':'nmembers'})
        self.wiki           = Link(self,{'base':'wiki'})
        self.nwikis         = TextReadOnly(self,{'base':'nwikis'})
        self.resources      = Link(self,{'base':'resources'})
        self.nresources     = TextReadOnly(self,{'base':'nresources'})
        self.discussion     = Link(self,{'base':'discussion'})
        self.ndiscussions   = TextReadOnly(self,{'base':'ndiscussions'})
        self.blog           = Link(self,{'base':'blog'})
        self.nblogs         = TextReadOnly(self,{'base':'nblogs'})
        self.wishlist       = Link(self,{'base':'wishlist'})
        self.usage          = Link(self,{'base':'usage'})
        self.projects       = Link(self,{'base':'projects'})
        self.nprojects      = TextReadOnly(self,{'base':'nprojects'})
        self.calendar       = Link(self,{'base':'calendar'})
        self.ncalendars     = TextReadOnly(self,{'base':'ncalendars'})
        self.announcements  = Link(self,{'base':'announcements'})
        self.collections    = Link(self,{'base':'collections'})

        self._menu_items = ['overview','members',
                            'wiki','resources','discussion',
                            'blog','wishlist','usage','projects',
                            'calendar','announcements','collections']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_menu_items(self):
        """return the menu link names"""

        return self._menu_items


    def goto_menu_item(self,menuitem):
        """click on a menu item"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        w.click()


    def is_menu_item_protected(self,menuitem):
        """check to see if the menu item is accessible by the user"""

        if not menuitem in self._menu_items:
            raise ValueError("invalid menu item: '%s'" % menuitem)
        w = getattr(self,menuitem)
        return 'protected' in w.get_attribute('class')


class GroupsMenu3_Locators_Base(object):
    """locators for GroupsMenu object"""

    locators = {
        'base'              : "css=#page_menu",
        'overview'          : "css=.group-overview-tab",
        'members'           : "css=.group-members-tab",
        'nmembers'          : "css=.group-members-tab .count",
        'wiki'              : "css=.group-wiki-tab",
        'nwikis'            : "css=.group-wiki-tab .count",
        'resources'         : "css=.group-resources-tab",
        'nresources'        : "css=.group-resources-tab .count",
        'discussion'        : "css=.group-forum-tab",
        'ndiscussions'      : "css=.group-forum-tab .count",
        'blog'              : "css=.group-blog-tab",
        'nblogs'            : "css=.group-blog-tab .count",
        'wishlist'          : "css=.group-wishlist-tab",
        'usage'             : "css=.group-usage-tab",
        'projects'          : "css=.group-projects-tab",
        'nprojects'         : "css=.group-projects-tab .count",
        'calendar'          : "css=.group-calendar-tab",
        'ncalendars'        : "css=.group-calendar-tab .count",
        'announcements'     : "css=.group-announcements-tab",
        'collections'       : "css=.group-collections-tab",
    }

