from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class SupportTicketSearchPage2011(GenericPage):
    """support ticket search"""

    def __init__(self,browser,catalog):
        super(SupportTicketSearchPage2011,self).__init__(browser,catalog)
        self.path = "/support/tickets"

        # load hub's classes
        SupportTicketSearchPage2011_Locators = self.load_class('SupportTicketSearchPage2011_Locators')
        TicketListSearchForm = self.load_class('TicketListSearchForm')

        # update this object's locator
        self.locators.update(AdminLoginPage_Locators.locators)

        # setup page object's components
        self.stats             = Link(self,{'base':'stats'})
        self.newticket         = Link(self,{'base':'newticket'})
        self.ticketlistsearch  = TicketListSearchForm(self,{'base':'ticketlistsearch'})

    def filter_by_keyword(self,value):
        return self.ticketlistsearch.filter_by_keyword(value)

    def filter_by_dropdown(self,value):
        return self.ticketlistsearch.filter_by_dropdown(value)

    def ticket_rows_displayed(self):
        return self.ticketlistsearch.ticket_rows_displayed()

    def ticket_row_by_index(self,index):
        return self.ticketlistsearch.ticket_row_by_index(index)

    def goto_page_number(self,pagenumber):
        return self.ticketlistsearch.goto_page_number(pagenumber)

    def goto_page_relative(self,relation):
        return self.ticketlistsearch.goto_page_relative(relation)

    def get_pagination_counts(self):
        return self.ticketlistsearch.get_pagination_counts()

    def display_limit(self,limit=None):
        return self.ticketlistsearch.display_limit(limit)

class SupportTicketSearchPage2011_Locators_Base(object):
    """locators for SupportTicketSearchPage2011 object"""

    locators = {
        'ticketlistsearch' : "css=[name='adminForm']",
        'stats'            : "css=.stats",
        'newticket'        : "css=.new-ticket",
    }

class SupportTicketSearchPage2011_Locators_Base_2(object):
    """locators for SupportTicketSearchPage2011 object"""

    locators = {
        'ticketlistsearch' : "css=#ticketForm",
        'stats'            : "css=.stats",
        'newticket'        : "css=.new-ticket",
    }

class SupportTicketSearchPage2012(GenericPage):
    """support ticket search"""

    def __init__(self,browser,catalog):
        super(SupportTicketSearchPage2012,self).__init__(browser,catalog)
        self.path = "/support/tickets"

        # load hub's classes
        SupportTicketSearchPage2012_Locators = self.load_class('SupportTicketSearchPage2012_Locators')
        TicketListSearchForm = self.load_class('TicketListSearchForm')

        # update this object's locator
        self.locators.update(SupportTicketSearchPage2012_Locators.locators)

        # setup page object's components
        self.stats             = Link(self,{'base':'stats'})
        self.newticket         = Link(self,{'base':'newticket'})
        self.ticketlistsearch  = TicketListSearchForm(self,{'base':'ticketlistsearch'})

    def filter_by_keyword(self,value):
        return self.ticketlistsearch.filter_by_keyword(value)

    def ticket_rows_displayed(self):
        return self.ticketlistsearch.ticket_rows_displayed()

    def ticket_row_by_index(self,index):
        return self.ticketlistsearch.ticket_row_by_index(index)

    def goto_page_number(self,pagenumber):
        return self.ticketlistsearch.goto_page_number(pagenumber)

    def goto_page_relative(self,relation):
        return self.ticketlistsearch.goto_page_relative(relation)

    def get_pagination_counts(self):
        return self.ticketlistsearch.get_pagination_counts()

    def display_limit(self,limit=None):
        return self.ticketlistsearch.display_limit(limit)

class SupportTicketSearchPage2012_Locators_Base(object):
    """locators for SupportTicketSearchPage2012 object"""

    locators = {
        'ticketlistsearch' : "css=#main form",
        'stats'            : "css=.stats",
        'newticket'        : "css=.add",
    }
