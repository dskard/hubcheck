from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class TicketListSearchForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketListSearchForm,self).__init__(owner,locatordict)

        # load hub's classes
        TicketListSearchForm_Locators = self.load_class('TicketListSearchForm_Locators')
        TicketListFilterOptions = self.load_class('TicketListFilterOptions')
        self.TicketListSearchResultRow = self.load_class('TicketListSearchResultRow')
        ListPageNav = self.load_class('ListPageNav')

        # update this object's locator
        self.locators.update(TicketListSearchForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.rowlocid = 0

        self.filteroptions   = TicketListFilterOptions(self,{'base':'filteroptions'})
        self.footer          = ListPageNav(self,{'base':'footer'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        if self.ticket_rows_displayed() > 0:
            row = self.ticket_row_by_index(1)
            row._checkLocatorsNonAdmin()
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        if self.ticket_rows_displayed() > 0:
            row = self.ticket_row_by_index(1)
            row._checkLocatorsAdmin()
        self._checkLocators(widgets,cltype)

    def filter_by_keyword(self,value):

        return self.filteroptions.filter_by_keyword(value)


    def filter_by_dropdown(self,value):

        return self.filteroptions.filter_by_dropdown(value)


    def ticket_rows_displayed(self):

        return len(self.find_elements(self.locators['row']))


    def ticket_row_by_index(self,index):

        maxindex = self.ticket_rows_displayed()
        if maxindex == 0:
            raise ValueError("no rows available in table")
        if index < 1 or index > maxindex:
            err = "provided row index (%d) outside of available range (1-%d)"
            raise ValueError(err % (index,maxindex))

        # store a new rowlocator in the locators dictionary
        rowlocator = self.locators['rowindex'].format(row_num=index)
        self.rowlocid += 1
        locid = "rowbyindex%d" % self.rowlocid
        self.locators[locid] = rowlocator

        # return the row
        return self.TicketListSearchResultRow(self,{'base':locid})


    def goto_page_number(self,pagenumber):

        return self.footer.goto_page_number(pagenumber)


    def goto_page_relative(self,relation):

        return self.footer.goto_page_relative(relation)


    def get_pagination_counts(self):

        return self.footer.get_pagination_counts()

    def display_limit(self,limit=None):

        return self.footer.display_limit(limit)


class TicketListSearchForm_Locators_Base(object):
    """locators for TicketListSearchForm object"""

    locators = {
        'base'           : "css=#main form",
        'filteroptions'  : "css=.filters",
        'footer'         : "css=.list-footer",
        'row'            : "css=#tktlist tbody tr",
        'rowindex'       : "css=#tktlist tbody tr:nth-of-type({row_num})",
    }
