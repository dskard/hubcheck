from hubcheck.pageobjects.po_groups_base import GroupsBasePage

class GroupsDeletePage(GroupsBasePage):
    """groups overview page"""

    def __init__(self,browser,catalog,groupid=None):
        super(GroupsDeletePage,self).__init__(browser,catalog,groupid)
        self.path += '/delete'

        # load hub's classes
        GroupsDeletePage_Locators = self.load_class('GroupsDeletePage_Locators')
        GroupsDeleteForm          = self.load_class('GroupsDeleteForm')

        # update this object's locator
        self.locators.update(GroupsDeletePage_Locators.locators)

        # setup page object's components
        self.form = GroupsDeleteForm(self,{'base':'form'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data={}):
        return self.form.submit_form(data)

class GroupsDeletePage_Locators_Base(object):
    """locators for GroupsDeletePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
