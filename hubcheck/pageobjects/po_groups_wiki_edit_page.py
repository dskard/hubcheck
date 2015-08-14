from hubcheck.pageobjects.po_groups_wiki_base_page import GroupsWikiBasePage

class GroupsWikiEditPage(GroupsWikiBasePage):
    """groups wiki edit page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiEditPage,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?task=edit" % (groupid,articleid)

        # load hub's classes
        GroupsWikiEditPage_Locators = self.load_class('GroupsWikiEditPage_Locators')
        GroupsWikiEditForm          = self.load_class('GroupsWikiEditForm')

        # update this object's locator
        self.locators.update(GroupsWikiEditPage_Locators.locators)

        # setup page object's components
        self.form         = GroupsWikiEditForm(self,{'base':'form'})

    def goto_rename(self):
        return self.form.goto_rename()

    def edit_wiki_page(self, data):
        return self.form.create_wiki_page(data)

    def populate_form(self, data):
        return self.form.populate_form(data)

    def preview_page(self):
        return self.form.preview_page()

    def submit_form(self):
        return self.form.submit_form()

    def get_uploaded_files(self):
        return self.form.get_uploaded_files()

    def delete_file(self,filename):
        return self.form.delete_file(filename)

class GroupsWikiEditPage2(GroupsWikiEditPage):
    """groups wiki edit page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiEditPage2,self).__init__(browser,catalog,groupid,articleid)
        self.path = "/groups/%s/wiki/%s?action=edit" % (groupid,articleid)

class GroupsWikiEditPage_Locators_Base(object):
    """locators for GroupsWikiEditPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
