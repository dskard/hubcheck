from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewComposePage(GenericPage):
    """resources new compose page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewComposePage,self).__init__(browser,catalog)
        self.path = "/resources/draft"

        # load hub's classes
        ResourcesNewComposePage_Locators = self.load_class('ResourcesNewComposePage_Locators')
        ResourcesNewComposeForm = self.load_class('ResourcesNewComposeForm')

        # update this object's locator
        self.locators.update(ResourcesNewComposePage_Locators.locators)

        # setup page object's components
        self.form = ResourcesNewComposeForm(self,{'base':'form'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data):
        return self.form.submit_form(data)

class ResourcesNewComposePage_Locators_Base(object):
    """locators for ResourcesNewComposePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
