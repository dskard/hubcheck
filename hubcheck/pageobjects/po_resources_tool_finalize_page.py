from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesToolFinalizePage(GenericPage):
    """tool resource finalize page"""

    def __init__(self,browser,catalog,toolname=None):
        super(ResourcesToolFinalizePage,self).__init__(browser,catalog)
        if toolname is not None:
            self.path = "/tools/%s/index.php" % (toolname)
        else:
            self.path = ""

        # load hub's classes
        ResourcesToolFinalizePage_Locators = \
            self.load_class('ResourcesToolFinalizePage_Locators')
        ResourcesToolFinalizeForm = \
            self.load_class('ResourcesToolFinalizeForm')

        # update this object's locator
        self.locators.update(ResourcesToolFinalizePage_Locators.locators)

        # setup page object's components
        self.form = ResourcesToolFinalizeForm(self,{'base':'form'})


class ResourcesToolFinalizePage_Locators_Base(object):
    """locators for ResourcesToolFinalizePage object"""

    locators = {
        'form' : "css=#hubForm",
    }
