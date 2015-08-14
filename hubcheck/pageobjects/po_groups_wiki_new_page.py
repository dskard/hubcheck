from hubcheck.pageobjects.po_groups_base import GroupsBasePage

class GroupsWikiNewPage(GroupsBasePage):
    """groups wiki new page"""

    def __init__(self,browser,catalog,groupid):
        super(GroupsWikiNewPage,self).__init__(browser,catalog,groupid)
        self.path = "/groups/%s/wiki?task=new" % groupid

        # load hub's classes
        GroupsWikiNewPage_Locators = self.load_class('GroupsWikiNewPage_Locators')
        GroupsWikiNewForm          = self.load_class('GroupsWikiNewForm')

        # update this object's locator
        self.locators.update(GroupsWikiNewPage_Locators.locators)

        # setup page object's components
        self.form = GroupsWikiNewForm(self,{'base':'form'})

    def create_wiki_page(self, data):
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


class GroupsWikiNewPage2(GroupsWikiNewPage):
    """groups wiki new page"""

    def __init__(self,browser,catalog,groupid):
        super(GroupsWikiNewPage2,self).__init__(browser,catalog,groupid)
        self.path = "/groups/%s/wiki?action=new" % groupid


class GroupsWikiNewPage_Locators_Base(object):
    """locators for GroupsWikiNewPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
