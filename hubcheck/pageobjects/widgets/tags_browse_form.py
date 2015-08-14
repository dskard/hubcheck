from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class TagsBrowseForm(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(TagsBrowseForm,self).__init__(owner,locatordict)

        # load hub's classes
        TagsBrowseForm_Locators = self.load_class('TagsBrowseForm_Locators')
        TextSearchBox           = self.load_class('TextSearchBox')
        TagsBrowseOrderOptions  = self.load_class('TagsBrowseOrderOptions')
        SearchResults           = self.load_class('SearchResults')
        TagsBrowseResultsRow    = self.load_class('TagsBrowseResultsRow')
        ListPageNav             = self.load_class('ListPageNav')

        # update this object's locator
        self.locators.update(TagsBrowseForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.searchbox       = TextSearchBox(self,
                                 {
                                    'base'   : 'searchbox',
                                    'text'   : 'searchtext',
                                    'submit' : 'searchbutton'
                                 })
        self.sortoptions     = TagsBrowseOrderOptions(self,
                                 {'base':'sortoptions'})
        self.footer          = ListPageNav(self,{'base':'footer'})
        self.search_results  = SearchResults(self,
                                 {
                                    'base'      : 'searchresults',
                                    'counts'    : 'sr_counts',
                                    'row'       : 'sr_row',
                                    'substrow'  : 'sr_substrow',
                                 }, TagsBrowseResultsRow,
                                 {
                                    'name'  : 'src_name',
                                    'count' : 'src_count',
                                 })

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        self._checkLocators(widgets,cltype)


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        self._checkLocators(widgets,cltype)


    def search_for(self,terms):

        return self.searchbox.search_for(terms)


    def goto_page_number(self,pagenumber):

        return self.footer.goto_page_number(pagenumber)


    def goto_page_relative(self,relation):

        return self.footer.goto_page_relative(relation)


    def get_caption_counts(self):

        return self.search_results.header_counts()


    def get_pagination_counts(self):

        return self.footer.get_pagination_counts()


    def get_current_page_number(self):

        return self.footer.get_current_page_number()


    def get_link_page_numbers(self):

        return self.footer.get_link_page_numbers()


    def search_result_rows(self):

        return iter(self.search_results)

class TagsBrowseForm_Locators_Base(object):
    """locators for TagsBrowseForm object"""

    locators = {
        'base'           : "css=#main form",
        'searchbox'      : "css=.data-entry",
        'searchtext'     : "css=#entry-search-text",
        'searchbutton'   : "css=.entry-search-submit",
        'sortoptions'    : "css=.entries-menu",
        'footer'         : "css=.list-footer",
        'searchresults'  : "css=#taglist",
        'sr_substrow'    : "css=#taglist tbody tr:nth-of-type({row_num})",
        'sr_row'         : "css=#taglist tbody tr",
        'sr_counts'      : "css=#taglist thead th span",
        'src_name'       : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(1) a",
        'src_count'      : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
    }

class TagsBrowseForm_Locators_Base_2(object):
    """locators for TagsBrowseForm object"""

    locators = {
        'base'           : "css=.main",
        'searchbox'      : "css=.data-entry",
        'searchtext'     : "css=#entry-search-text",
        'searchbutton'   : "css=.entry-search-submit",
        'sortoptions'    : "css=.entries-menu",
        'footer'         : "css=.list-footer",
        'searchresults'  : "css=#taglist",
        'sr_substrow'    : "css=#taglist tbody tr:nth-of-type({row_num})",
        'sr_row'         : "css=#taglist tbody tr",
        'sr_counts'      : "css=#taglist thead th span",
        'src_name'       : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(1) a",
        'src_count'      : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
    }
