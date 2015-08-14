from hubcheck.pageobjects.po_groups_wiki_base_page import GroupsWikiBasePage

class GroupsWikiDeletePage(GroupsWikiBasePage):
    """groups wiki new page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiDeletePage,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?task=delete" % (groupid,articleid)

        # load hub's classes
        GroupsWikiDeletePage_Locators = self.load_class('GroupsWikiDeletePage_Locators')
        GroupsWikiDeleteForm          = self.load_class('GroupsWikiDeleteForm')

        # update this object's locator
        self.locators.update(GroupsWikiDeletePage_Locators.locators)

        # setup page object's components
        self.form = GroupsWikiDeleteForm(self,{'base':'form'})

    def confirm_delete(self):
        return self.form.confirm_delete()

    def submit_form(self):
        return self.form.submit_form()

    def delete_wiki_page(self):
        return self.form.delete_wiki_page()

class GroupsWikiDeletePage2(GroupsWikiDeletePage):
    """groups wiki new page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiDeletePage2,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?action=delete" % (groupid,articleid)

class GroupsWikiDeletePage_Locators_Base(object):
    """locators for GroupsWikiDeletePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
