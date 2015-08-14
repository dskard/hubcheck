from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class GroupsBasePage(GenericPage):
    """groups page"""

    def __init__(self,browser,catalog,groupid=None):
        super(GroupsBasePage,self).__init__(browser,catalog)
        self.groupid = groupid
        if groupid != None:
            self.path = "/groups/%s" % groupid
        else:
            self.path = "/groups/"

        # load hub's classes
        GroupsBasePage_Locators = self.load_class('GroupsBasePage_Locators')
        GroupsOptions           = self.load_class('GroupsOptions')
        GroupsMenu              = self.load_class('GroupsMenu')
        GroupsTitle             = self.load_class('GroupsTitle')
        GroupsInfo              = self.load_class('GroupsInfo')

        # update this object's locator
        self.locators.update(GroupsBasePage_Locators.locators)

        # setup page object's components
        self.options = GroupsOptions(self,{'base':'options'})
        self.menu    = GroupsMenu(self,{'base':'menu'})
        self.info    = GroupsInfo(self,{'base':'info'})
        self.title   = GroupsTitle(self,{'base':'title'})
        self.create  = Link(self,{'base':'create'})

    def get_menu_items(self):
        return self.menu.get_menu_items()

    def get_options_items(self):
        return self.options.get_options_items()

    def get_title(self):
        return self.title.get_title()

    def goto_group_page(self):
        return self.title.goto_title()

    def goto_options_item(self,item):
        return self.options.goto_options_item(item)

    def goto_menu_item(self,item):
        return self.menu.goto_menu_item(item)

    def is_menu_item_protected(self,item):
        return self.menu.is_menu_item_protected(item)

    def get_privacy(self):
        return self.info.get_privacy()

    def get_join_policy(self):
        return self.info.get_join_policy()

    def get_create_date(self):
        return self.info.get_create_date()

    def group_exists(self):
        return (self.create.is_displayed() == False) \
               and (self.page_title() != '')

class GroupsBasePage_Locators_Base(object):
    """locators for GroupsBasePage object"""

    locators = {
        'options'     : "css=#group_options",
        'menu'        : "css=#page_menu",
        'info'        : "css=#page_info",
        'title'       : "css=#page_header",
        'create'      : "css=.warning a",
    }
