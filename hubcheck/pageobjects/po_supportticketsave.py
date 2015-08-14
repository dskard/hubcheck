from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class SupportTicketSavePage(GenericPage):
    """support ticket view"""

    def __init__(self,browser,catalog):
        super(SupportTicketSavePage,self).__init__(browser,catalog)
        self.path = "/support/ticket/save"

        # load hub's classes
        SupportTicketSavePage_Locators = self.load_class('SupportTicketSavePage_Locators')
        TicketSave = self.load_class('TicketSave')

        # update this object's locator
        self.locators.update(SupportTicketSavePage_Locators.locators)

        # setup page object's components
        self.save         = TicketSave(self,{'base':'save'})

    def get_ticket_number(self):
        return self.save.get_ticket_number()

    def goto_tracking_system(self):
        return self.save.goto_tracking_system()

class SupportTicketSavePage_Locators_Base(object):
    """locators for SupportTicketSavePage object"""

    locators = {
        'save' : "css=#main",
    }

class SupportTicketSavePage_Locators_Base_2012(object):
    """locators for SupportTicketSavePage object"""

    locators = {
        'save' : "css=#wrap",
    }

class SupportTicketSavePage_Locators_Base_2012b(object):
    """locators for SupportTicketSavePage object"""

    locators = {
        'save' : "css=.main",
    }
