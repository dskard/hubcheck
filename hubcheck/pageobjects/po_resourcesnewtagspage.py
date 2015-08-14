from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewTagsPage(GenericPage):
    """resources new compose page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewTagsPage,self).__init__(browser,catalog)
        self.path = "/resources/draft"

        # load hub's classes
        ResourcesNewTagsPage_Locators = self.load_class('ResourcesNewTagsPage_Locators')
        ResourcesNewTagsForm = self.load_class('ResourcesNewTagsForm')

        # update this object's locator
        self.locators.update(ResourcesNewTagsPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesNewTagsForm(self,{'base':'form'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data):
        return self.form.submit_form(data)

class ResourcesNewTagsPage_Locators_Base(object):
    """locators for ResourcesNewTagsPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
