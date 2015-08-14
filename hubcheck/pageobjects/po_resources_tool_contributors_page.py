from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesToolContributorsPage(GenericPage):
    """tool resource contributor page"""

    def __init__(self,browser,catalog,toolname=None):
        super(ResourcesToolContributorsPage,self).__init__(browser,catalog)
        if toolname is not None:
            self.path = "/tools/%s/resources?step=2" % (toolname)
        else:
            self.path = ""

        # load hub's classes
        ResourcesToolContributorsPage_Locators = \
            self.load_class('ResourcesToolContributorsPage_Locators')
        ResourcesToolContributorsForm = \
            self.load_class('ResourcesToolContributorsForm')

        # update this object's locator
        self.locators.update(ResourcesToolContributorsPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesToolContributorsForm(self,{'base':'form'})


class ResourcesToolContributorsPage_Locators_Base(object):
    """locators for ResourcesToolContributorsPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
