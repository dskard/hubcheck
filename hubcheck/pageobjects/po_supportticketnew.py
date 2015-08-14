from selenium.common.exceptions import NoSuchElementException
from hubcheck.exceptions import NoSuchFileAttachmentError

from hubcheck.pageobjects.po_generic_page import GenericPage

class SupportTicketNewPage(GenericPage):
    """create a new support ticket"""

    def __init__(self,browser,catalog):
        super(SupportTicketNewPage,self).__init__(browser,catalog)
        self.path = "/support/ticket/new"

        # load hub's classes
        SupportTicketNewPage_Locators = self.load_class('SupportTicketNewPage_Locators')
        TicketNewForm = self.load_class('TicketNewForm')

        # update this object's locator
        self.locators.update(SupportTicketNewPage_Locators.locators)

        # setup page object's components
        self.ticketform   = TicketNewForm(self,{'base':'ticketform'})

    def get_attachment_type(self):
        return self.ticketform.get_attachment_type()

    def submit_ticket(self,data):
        return self.ticketform.submit_ticket(data)

    def submit_form(self,data):
        return self.ticketform.submit_form(data)

    def populate_form(self,data):
        return self.ticketform.populate_form(data)

class SupportTicketNewPage_Locators_Base(object):
    """locators for SupportTicketNewPage object"""

    locators = {
        'ticketform' : "css=#hubForm",
    }

