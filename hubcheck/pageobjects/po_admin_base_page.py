from hubcheck.pageobjects.po_generic_page import GenericPage

class AdminBasePage(GenericPage):
    """admin base page object"""

    def __init__(self,browser,catalog):
        super(AdminBasePage,self).__init__(browser,catalog)
        self.path = '/administrator'

        # load hub's classes
        AdminBasePage_Locators = self.load_class('AdminBasePage_Locators')
        AdminMenu              = self.load_class('AdminMenu')
        AdminHeader            = self.load_class('AdminHeader')

        # update this object's locator
        self.locators.update(AdminBasePage_Locators.locators)

        # setup page object's components
        self.menu = AdminMenu(self,{'base':'menu'})
        self.header = AdminHeader(self,{'base':'header'})

class AdminBasePage_Locators_Base(object):
    """locators for AdminBasePage object"""

    locators = {
        'menu'      : "css=#menu",
        'header'    : "css=#header",
    }
