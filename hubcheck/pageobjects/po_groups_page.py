from hubcheck.pageobjects.po_generic_page import GenericPage

class GroupsPage(GenericPage):
    """groups page"""

    def __init__(self,browser,catalog):
        super(GroupsPage,self).__init__(browser,catalog)
        self.path = "/groups"

        # load hub's classes
        GroupsPage_Locators = self.load_class('GroupsPage_Locators')
        Groups              = self.load_class('Groups')

        # update this object's locator
        self.locators.update(GroupsPage_Locators.locators)

        # setup page object's components
        self.groups       = Groups(self,{'base':'groups'})

#    def goto_faq(self):
#        return self.groups.goto_faq()
#
#    def goto_guidelines(self):
#        return self.groups.goto_guidelines()
#
#    def goto_create_group(self):
#        return self.groups.goto_create_group()
#
#    def goto_browse_list(self):
#        return self.groups.goto_browse_list()
#
#    def search_groups(self,searchtext):
#        return self.groups.search_groups(searchtext)
#
#    def get_popular_groups(self):
#        return self.groups.get_popular_groups()
#
#    def goto_popular_group(self,group_name):
#        return self.groups.goto_popular_group(group_name)
#
#    def has_info_no_popular_groups(self):
#        return self.groups.has_info_no_popular_groups()


class GroupsPage_Locators_Base(object):
    """locators for GroupsPage object"""

    locators = {
        'groups' : "css=#content",
    }
