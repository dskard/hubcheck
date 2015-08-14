from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class ToolsCreatePage(GenericPage):
    """page to create a new tool resource"""

    def __init__(self,browser,catalog):
        super(ToolsCreatePage,self).__init__(browser,catalog)
        self.path = "/tools/create"

        # load hub's classes
        ToolsCreatePage_Locators = self.load_class('ToolsCreatePage_Locators')
        ToolsCreateForm = self.load_class('ToolsCreateForm')

        # update this object's locator
        self.locators.update(ToolsCreatePage_Locators.locators)

        # setup page object's components
        self.form           = ToolsCreateForm(self,{'base':'form'})
        self.alltools       = Link(self,{'base':'alltools'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data={}):
        return self.form.submit_form(data)

    def goto_all_tools(self):
        return self.alltools.click()

class ToolsCreatePage_Locators_Base(object):
    """locators for ToolsCreatePage object"""

    locators = {
        'form'      : "css=#hubForm",
        'alltools'  : "css=.main-page",
    }


class ContribtoolCreatePage(ToolsCreatePage):
    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolCreatePage,self).__init__(browser,catalog)
        self.path = "/contribtool/create"


class ContribtoolCreatePage_Locators_Base(object):
    """locators for ContribtoolCreatePage object"""

    locators = {
        'form'      : "css=#hubForm",
        'alltools'  : "css=#useroptions .last a",
    }


