from hubcheck.pageobjects.po_groups_wiki_base_page import GroupsWikiBasePage

class GroupsWikiRenamePage(GroupsWikiBasePage):
    """groups wiki rename page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiRenamePage,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?task=rename" % (groupid,articleid)

        # load hub's classes
        GroupsWikiRenamePage_Locators = self.load_class('GroupsWikiRenamePage_Locators')
        GroupsWikiRenameForm          = self.load_class('GroupsWikiRenameForm')

        # update this object's locator
        self.locators.update(GroupsWikiRenamePage_Locators.locators)

        # setup page object's components
        self.form = GroupsWikiRenameForm(self,{'base':'form'})

    def rename_page(self, name):
        return self.form.rename_page(name)

    def submit_form(self):
        return self.form.submit_form()

class GroupsWikiRenamePage2(GroupsWikiRenamePage):
    """groups wiki rename page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiRenamePage2,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?action=rename" % (groupid,articleid)

class GroupsWikiRenamePage_Locators_Base(object):
    """locators for GroupsWikiRenamePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
