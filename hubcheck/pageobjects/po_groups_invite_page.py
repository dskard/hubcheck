from hubcheck.pageobjects.po_groups_base import GroupsBasePage

class GroupsInvitePage(GroupsBasePage):
    """groups overview page"""

    def __init__(self,browser,catalog,groupid=None):
        super(GroupsInvitePage,self).__init__(browser,catalog,groupid)
        self.path += '/invite'

        # load hub's classes
        GroupsInvitePage_Locators = self.load_class('GroupsInvitePage_Locators')
        GroupsInviteForm          = self.load_class('GroupsInviteForm')

        # update this object's locator
        self.locators.update(GroupsInvitePage_Locators.locators)

        # setup page object's components
        self.form = GroupsInviteForm(self,{'base':'form'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data={}):
        return self.form.submit_form(data)

class GroupsInvitePage_Locators_Base(object):
    """locators for GroupsInvitePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
