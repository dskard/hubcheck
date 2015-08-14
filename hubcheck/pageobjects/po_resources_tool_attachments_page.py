from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesToolAttachmentsPage(GenericPage):
    """tool resource contributor page"""

    def __init__(self,browser,catalog,toolname=None):
        super(ResourcesToolAttachmentsPage,self).__init__(browser,catalog)
        if toolname is not None:
            self.path = "/tools/%s/resources?step=2" % (toolname)
        else:
            self.path = ""

        # load hub's classes
        ResourcesToolAttachmentsPage_Locators = \
            self.load_class('ResourcesToolAttachmentsPage_Locators')
        ResourcesToolAttachmentsForm = \
            self.load_class('ResourcesToolAttachmentsForm')

        # update this object's locator
        self.locators.update(ResourcesToolAttachmentsPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesToolAttachmentsForm(self,{'base':'form'})


class ResourcesToolAttachmentsPage_Locators_Base(object):
    """locators for ResourcesToolAttachmentsPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
