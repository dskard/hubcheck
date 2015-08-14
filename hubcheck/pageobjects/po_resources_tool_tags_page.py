from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesToolTagsPage(GenericPage):
    """tool resource contributor page"""

    def __init__(self,browser,catalog,toolname=None):
        super(ResourcesToolTagsPage,self).__init__(browser,catalog)
        if toolname is not None:
            self.path = "/tools/%s/resources?step=4" % (toolname)
        else:
            self.path = ""

        # load hub's classes
        ResourcesToolTagsPage_Locators = \
            self.load_class('ResourcesToolTagsPage_Locators')
        ResourcesToolTagsForm = \
            self.load_class('ResourcesToolTagsForm')

        # update this object's locator
        self.locators.update(ResourcesToolTagsPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesToolTagsForm(self,{'base':'form'})


class ResourcesToolTagsPage_Locators_Base(object):
    """locators for ResourcesToolTagsPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
