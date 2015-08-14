from hubcheck.pageobjects.basepagewidget import BasePageWidget

import re

class TagsViewForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TagsViewForm,self).__init__(owner,locatordict)

        # load hub's classes
        TagsViewForm_Locators   = self.load_class('TagsViewForm_Locators')
        TagSearchBox            = self.load_class('TagSearchBox')
        SortOrderOptions        = self.load_class('SortOrderOptions')
        SearchResults           = self.load_class('SearchResults')
        TagsViewResultsRow      = self.load_class('TagsViewResultsRow')
        ListPageNav             = self.load_class('ListPageNav')

        # update this object's locator
        self.locators.update(TagsViewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.searchbox       = TagSearchBox(self,
                                 {
                                    'base'           : 'searchbox',
                                    'tags'           : 'tags',
                                    'tagsac'         : 'tagsac',
                                    'tagsacchoices'  : 'tagsacchoices',
                                    'tagsactoken'    : 'tagsactoken',
                                    'tagsacdelete'   : 'tagsacdelete',
                                    'submit'         : 'submit',
                                 })
        self.sortoptions     = SortOrderOptions(self,
                                 {
                                    'base'  : 'sortoptions',
                                    'date'  : 'sortbydate',
                                    'title' : 'sortbytitle',
                                 })
        self.footer          = ListPageNav(self,{'base':'footer'})
        self.search_results  = SearchResults(self,
                                 {
                                    'base'      : 'searchresults',
                                    'counts'    : 'sr_counts',
                                    'row'       : 'sr_row',
                                    'substrow'  : 'sr_substrow',
                                 }, TagsViewResultsRow,
                                 {
                                    'src_title' : 'title',
                                    'src_text'  : 'text',
                                    'src_href'  : 'href',
                                 })

        # update the component's locators with this objects overrides
        self._updateLocators()


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

class TagsViewForm_Locators_Base(object):
    """locators for TagsViewForm object"""

    locators = {
        'base'           : "css=#main form",
        'searchbox'      : "css=.data-entry",
        'tags'           : "css=#actags",
        'tagsac'         : "css=#token-input-actags",
        'tagsacchoices'  : "css=.token-input-dropdown-act",
        'tagsactoken'    : "css=.token-input-token-act",
        'tagsacdelete'   : "css=.token-input-delete-token-act",
        'submit'         : "css=.entry-search-submit",
        'sortoptions'    : "css=.entries-menu",
        'sortbytitle'    : "css=.entries-menu a[title='Sort by title']",
        'sortbydate'     : "css=.entries-menu a[title='Sort by newest to oldest']",
        'footer'         : "css=.list-footer",
        # 'searchresults'  : "css=#search .results",
        'searchresults'  : "css=.container-block",
        'sr_substrow'    : "css=#search .results li:nth-of-type({row_num})",
        'sr_row'         : "css=#search .results li",
        'sr_counts'      : "css=#rel-search span",
        'src_title'      : "css=#search .results li:nth-of-type({row_num}) .title",
        'src_text'       : "css=#search .results li:nth-of-type({row_num}) p:nth-of-type(2)",
        'src_href'       : "css=#search .results li:nth-of-type({row_num}) .href",
    }
