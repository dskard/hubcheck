from hubcheck.pageobjects.po_generic_page import GenericPage

class GroupsNewPage(GenericPage):
    """groups page"""

    def __init__(self,browser,catalog):
        super(GroupsNewPage,self).__init__(browser,catalog)
        self.path = "/groups/new"

        # load hub's classes
        GroupsNewPage_Locators = self.load_class('GroupsNewPage_Locators')
        GroupsNewForm          = self.load_class('GroupsNewForm')

        # update this object's locator
        self.locators.update(GroupsNewPage_Locators.locators)

        # setup page object's components
        self.form         = GroupsNewForm(self,{'base':'form'})

    def create_group(self,data):
        return self.form.create_group(data)


class GroupsNewPage_Locators_Base(object):
    """locators for GroupsNewPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
