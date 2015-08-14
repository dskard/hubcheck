from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class WishlistSearchForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistSearchForm,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistSearchForm_Locators = self.load_class('WishlistSearchForm_Locators')
        TagSearchBox = self.load_class('TagSearchBox')
        WishlistFilterOptions = self.load_class('WishlistFilterOptions')
        WishlistOrderOptions = self.load_class('WishlistOrderOptions')
        ListPageNav = self.load_class('ListPageNav')

        # update this object's locator
        self.locators.update(WishlistSearchForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.searchbox       = TagSearchBox(self,{'base':'searchbox'})
        self.filteroptions   = WishlistFilterOptions(self,{'base':'filteroptions'})
        self.sortoptions     = WishlistOrderOptions(self,{'base':'sortoptions'})
        self.footer          = ListPageNav(self,{'base':'footer'})
        self.topcounts       = TextReadOnly(self,{'base':'topcounts'})

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

        countstxt = self.topcounts.value
        pattern = re.compile("\((\d+) - (\d+) of (\d+)\)")
        (beginshown,endshown,total) = pattern.match(countstxt).groups()
        return (beginshown,endshown,total)


    def get_pagination_counts(self):

        return self.footer.get_pagination_counts()


class WishlistSearchForm_Locators_Base(object):
    """locators for WishlistSearchForm object"""

    locators = {
        'base'           : "css=#main form",
        'searchbox'      : "css=.data-entry",
        'filteroptions'  : "css=.filter-options",
        'sortoptions'    : "css=.order-options",
        'footer'         : "css=.list-footer",
        'topcounts'      : "css=caption span",
    }


class WishlistSearchForm_Locators_Base_2(object):
    """locators for WishlistSearchForm object"""

    locators = {
        'base'           : "css=.main form",
        'searchbox'      : "css=.data-entry",
        'filteroptions'  : "css=.filter-options",
        'sortoptions'    : "css=.order-options",
        'footer'         : "css=.list-footer",
        'topcounts'      : "css=caption span",
    }
