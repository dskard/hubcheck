from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewReviewPage(GenericPage):
    """resources new compose page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewReviewPage,self).__init__(browser,catalog)
        self.path = "/resources/draft"

        # load hub's classes
        ResourcesNewReviewPage_Locators = self.load_class('ResourcesNewReviewPage_Locators')
        ResourcesNewReviewForm = self.load_class('ResourcesNewReviewForm')

        # update this object's locator
        self.locators.update(ResourcesNewReviewPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesNewReviewForm(self,{'base':'form'})

    def populate_form(self,data):
        return self.form.populate_form(data)

    def submit_form(self,data):
        return self.form.submit_form(data)

    def get_license_types(self):
        return self.form.get_license_types()

    def get_license_preview(self):
        return self.form.get_license_preview()

class ResourcesNewReviewPage_Locators_Base(object):
    """locators for ResourcesNewReviewPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
