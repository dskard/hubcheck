from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsPipelineSearchForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsPipelineSearchForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsPipelineSearchForm_Locators = self.load_class('ToolsPipelineSearchForm_Locators')
        TextSearchBox = self.load_class('TextSearchBox')
        ToolsPipelineFilterOptions = self.load_class('ToolsPipelineFilterOptions')
        ToolsPipelineSortOptions = self.load_class('ToolsPipelineSortOptions')
        SearchResults = self.load_class('SearchResults')
        ToolsPipelineSearchResultRow = self.load_class('ToolsPipelineSearchResultRow')
        ListPageNav = self.load_class('ListPageNav')
        ListTopCounts = self.load_class('ListTopCounts')

        # update this object's locator
        self.locators.update(ToolsPipelineSearchForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.searchbox       = TextSearchBox(self,
                                    {'base'   : 'searchbox',
                                     'text'   : 'searchbox_text',
                                     'submit' : 'searchbox_submit'})
        self.filteroptions   = ToolsPipelineFilterOptions(self,{'base':'filteroptions'})
        self.sortoptions     = ToolsPipelineSortOptions(self,{'base':'sortoptions'})
        self.footer          = ListPageNav(self,{'base':'footer'})
        self.topcounts       = ListTopCounts(self,{'base':'topcounts'})
        self.search_results  = SearchResults(self,
                                 {
                                    'base'      : 'searchresults',
                                    'counts'    : 'sr_counts',
                                    'row'       : 'sr_row',
                                    'substrow'  : 'sr_substrow',
                                 }, ToolsPipelineSearchResultRow,
                                 {
                                    'title'    : 'src_title',
                                    'details'  : 'src_details',
                                    'alias'    : 'src_alias',
                                    'status'   : 'src_status',
                                    'time'     : 'src_time',
                                    'resource' : 'src_resource',
                                    'history'  : 'src_history',
                                    'wiki'     : 'src_wiki',
                                 })


        # update the component's locators with this objects overrides
        self._updateLocators()


    def search_for(self,terms):

        return self.searchbox.search_for(terms)


    def goto_page_number(self,pagenumber):

        return self.footer.goto_page_number(pagenumber)


    def goto_page_relative(self,relation):

        return self.footer.goto_page_relative(relation)


    def get_pagination_counts(self):

        return self.footer.get_pagination_counts()


    def get_current_page_number(self):

        return self.footer.get_current_page_number()


    def get_link_page_numbers(self):

        return self.footer.get_link_page_numbers()


    def search_result_rows(self):

        return iter(self.search_results)


    def get_caption(self):

        return self.topcounts.get_caption()


    def get_caption_description(self):

        return self.topcounts.get_caption_description()


    def get_caption_counts(self):

        return self.topcounts.get_caption_counts()


    def get_aliases_by_status(self,statuses):
        aliases = {}
        lstatuses = []

        for status in statuses:
            lstatuses.append(status.lower())
            aliases[status.lower()] = []

        for item in self.search_results:
            iv = item.value()
            status = iv['status'].lower()
            if status in lstatuses:
                aliases[status].append(iv['alias'])

        return aliases


class ToolsPipelineSearchForm_Locators_Base(object):
    """locators for ToolsPipelineSearchForm object"""

    locators = {
        'base'             : "css=#main form",
        'searchbox'        : "css=.data-entry",
        'searchbox_text'   : "css=#entry-search-text",
        'searchbox_submit' : "css=.entry-search-submit",
        'filteroptions'    : "css=.filter-options",
        'sortoptions'      : "css=.order-options",
        'footer'           : "css=.list-footer",
        'topcounts'        : "css=.entries",
        'searchresults'    : "css=.tools",
        'sr_substrow'      : "css=.tools tbody tr:nth-of-type({row_num})",
        'sr_row'           : "css=.tools tbody tr",
        'sr_counts'        : "css=.tools caption span",
        'src_title'        : "css=.tools tbody tr:nth-of-type({row_num}) .entry-title",
        'src_details'      : "css=.tools tbody tr:nth-of-type({row_num}) .entry-details",
        'src_alias'        : "css=.tools tbody tr:nth-of-type({row_num}) .entry-alias",
        'src_status'       : "css=.tools tbody tr:nth-of-type({row_num}) .entry-status",
        'src_time'         : "css=.tools tbody tr:nth-of-type({row_num}) .entry-time",
        'src_resource'     : "css=.tools tbody tr:nth-of-type({row_num}) .entry-page",
        'src_history'      : "css=.tools tbody tr:nth-of-type({row_num}) .entry-history",
        'src_wiki'         : "css=.tools tbody tr:nth-of-type({row_num}) .entry-wiki",
    }
