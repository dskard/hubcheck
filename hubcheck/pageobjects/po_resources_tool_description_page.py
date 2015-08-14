from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesToolDescriptionPage(GenericPage):
    """tools resource description page"""

    def __init__(self,browser,catalog,toolname=None):
        super(ResourcesToolDescriptionPage,self).__init__(browser,catalog)
        if toolname is not None:
            self.path = "/tools/%s/resources?step=1" % (toolname)
        else:
            self.path = ""

        # load hub's classes
        ResourcesToolDescriptionPage_Locators = \
            self.load_class('ResourcesToolDescriptionPage_Locators')
        ResourcesToolDescriptionForm = \
            self.load_class('ResourcesToolDescriptionForm')

        # update this object's locator
        self.locators.update(ResourcesToolDescriptionPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesToolDescriptionForm(self,{'base':'form'})


class ResourcesToolDescriptionPage_Locators_Base(object):
    """locators for ResourcesToolDescriptionPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
