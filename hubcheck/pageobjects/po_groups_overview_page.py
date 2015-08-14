from hubcheck.pageobjects.po_groups_base import GroupsBasePage

class GroupsOverviewPage(GroupsBasePage):
    """groups overview page"""

    def __init__(self,browser,catalog,groupid=None):
        super(GroupsOverviewPage,self).__init__(browser,catalog,groupid)

        # load hub's classes
        GroupsOverviewPage_Locators = self.load_class('GroupsOverviewPage_Locators')
        TagsList                    = self.load_class('TagsList')
        GroupsOverview              = self.load_class('GroupsOverview')

        # update this object's locator
        self.locators.update(GroupsOverviewPage_Locators.locators)

        # setup page object's components
        self.tags     = TagsList(self,{'base':'tags'})
        self.overview = GroupsOverview(self,{'base':'overview'})

    def get_tags(self):
        return self.tags.get_tags()

    def click_tag(self,tagname):
        return self.tags.click_tag(tagname)

    def get_member_names(self):
        return self.overview.get_member_names()

    def goto_member_profile(self,membername):
        return self.overview.goto_member_profile(membername)

class GroupsOverviewPage_Locators_Base(object):
    """locators for GroupsOverviewPage object"""

    locators = {
        'overview' : "css=.group_overview",
        'tags'     : "css=.tags",
    }
