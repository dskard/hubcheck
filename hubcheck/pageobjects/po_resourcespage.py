from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesPage(GenericPage):
    """groups page"""

    def __init__(self,browser,catalog):
        super(ResourcesPage,self).__init__(browser,catalog)
        self.path = "/resources"

        # load hub's classes
        ResourcesPage_Locators = self.load_class('ResourcesPage_Locators')
        Resources = self.load_class('Resources')

        # update this object's locator
        self.locators.update(ResourcesPage_Locators.locators)

        # setup page object's components
        self.resources         = Resources(self,{'base':'resources'})

    def goto_create(self):
        return self.resources.goto_create()

    def goto_faq(self):
        return self.resources.goto_faq()

    def search_resources(self,searchtext):
        return self.resources.search_resources(searchtext)

    def goto_browse_list(self):
        return self.resources.goto_browse_list()

    def goto_category_by_browse(self,category):
        return self.resources.goto_category_by_browse(category)

    def goto_category_by_title(self,category):
        return self.resources.goto_category_by_title(category)

    def get_category_titles(self):
        return self.resources.get_category_titles()

    def get_category_classes(self):
        return self.resources.get_category_classes()

class ResourcesPage_Locators_Base(object):
    """locators for ResourcesPage object"""

    locators = {
        'resources' : "css=#content",
    }
