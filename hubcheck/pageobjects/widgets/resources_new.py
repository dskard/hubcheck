from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class ResourcesNew(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNew,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNew_Locators = self.load_class('ResourcesNew_Locators')
        ResourcesCategoryBrowser = self.load_class('ResourcesCategoryBrowser')

        # update this object's locator
        self.locators.update(ResourcesNew_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.create         = Link(self,{'base':'create'})
        self.legal_cc       = Link(self,{'base':'legal_cc'})
        self.legal_license  = Link(self,{'base':'legal_license'})
        self.file_ticket    = Link(self,{'base':'file_ticket'})
        self.catbrowser     = ResourcesCategoryBrowser(self,{'base':'catbrowser'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_create(self):
        """click the resource create link"""

        return self.create.click()


    def goto_legal_cc(self):
        """click on the legal creative commons link"""

        return self.legal_cc.click()


    def goto_legal_license(self):
        """click on the legal license link"""

        return self.legal_license.click()


    def goto_file_ticket(self):
        """click on the file ticket link"""

        return self.file_ticket.click()


    def goto_category_by_title(self,category):
        """click on a category title"""

        return self.catbrowser.goto_category_by_title(category)


    def get_category_titles(self):
        """return a list of category titles"""

        return self.catbrowser.get_category_titles()


    def get_category_classes(self):
        """return a list of category classes"""

        return self.catbrowser.get_category_classes()


class ResourcesNew_Locators_Base(object):
    """locators for ResourcesNew object"""

    locators = {
        'base'          : "css=#content",
        'create'        : "css=#getstarted a",
        'legal_cc'      : "xpath=//a[contains(text(),'Creative Commons 3')]",
        'legal_license' : "xpath=//a[contains(text(),'more details')]",
        'file_ticket'   : "xpath=//a[contains(text(),'file a trouble report')]",
        'catbrowser'    : "css=#content",
    }
