from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewPage(GenericPage):
    """groups page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewPage,self).__init__(browser,catalog)
        self.path = "/resources/new"

        # load hub's classes
        ResourcesNewPage_Locators = self.load_class('ResourcesNewPage_Locators')
        ResourcesNew = self.load_class('ResourcesNew')

        # update this object's locator
        self.locators.update(ResourcesNewPage_Locators.locators)

        # setup page object's components
        self.resourcesnew = ResourcesNew(self,{'base':'resourcesnew'})

    def goto_create(self):
        return self.resourcesnew.goto_create()

    def goto_legal_cc(self):
        return self.resourcesnew.goto_legal_cc()

    def goto_legal_license(self):
        return self.resourcesnew.goto_legal_license()

    def goto_file_ticket(self):
        return self.resourcesnew.goto_file_ticket()

    def goto_category_by_title(self,category):
        return self.resourcesnew.goto_category_by_title(category)

    def get_category_titles(self):
        return self.resourcesnew.get_category_titles()

    def get_category_classes(self):
        return self.resourcesnew.get_category_classes()

class ResourcesNewPage_Locators_Base(object):
    """locators for ResourcesNewPage object"""

    locators = {
        'resourcesnew' : "css=#content",
    }
