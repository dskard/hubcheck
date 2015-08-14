from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewAttachPage(GenericPage):
    """resources new attach page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewAttachPage,self).__init__(browser,catalog)
        self.path = "/resources/draft"

        # load hub's classes
        ResourcesNewAttachPage_Locators = self.load_class('ResourcesNewAttachPage_Locators')
        ResourcesNewAttachForm = self.load_class('ResourcesNewAttachForm')

        # update this object's locator
        self.locators.update(ResourcesNewAttachPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesNewAttachForm(self,{'base':'form'})

    def upload_files(self, flist):
        return self.form.upload_files(flist)

    def get_uploaded_files(self):
        return self.form.get_uploaded_files()

    def delete_file(self,filename):
        return self.form.delete_file(filename)

    def submit_form(self,flist):
        return self.form.submit_form(flist)

class ResourcesNewAttachPage_Locators_Base(object):
    """locators for ResourcesNewAttachPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
