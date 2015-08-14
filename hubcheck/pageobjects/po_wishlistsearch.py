from hubcheck.pageobjects.po_generic_page import GenericPage

class WishlistSearchPage(GenericPage):
    """wishlist search"""

    def __init__(self,browser,catalog,listid='1'):
        super(WishlistSearchPage,self).__init__(browser,catalog)
        self.listid = listid
        self.path = "/wishlist/general/%s" % (self.listid)

        # load hub's classes
        WishlistSearchPage_Locators = self.load_class('WishlistSearchPage_Locators')
        WishlistSearchForm = self.load_class('WishlistSearchForm')

        # update this object's locator
        self.locators.update(WishlistSearchPage_Locators.locators)

        # setup page object's components
        self.wishlistsearch = WishlistSearchForm(self,{'base':'wishlistsearch'})

    def search_for(self,terms):
        return self.wishlistsearch.search_for(terms)

    def goto_page_number(self,pagenumber):
        return self.wishlistsearch.goto_page_number(pagenumber)

    def goto_page_relative(self,relation):
        return self.wishlistsearch.goto_page_relative(relation)

    def get_caption_counts(self):
        return self.wishlistsearch.get_caption_counts()

    def get_pagination_counts(self):
        return self.wishlistsearch.get_pagination_counts()

class WishlistSearchPage_Locators_Base(object):
    """locators for WishlistSearchPage object"""

    locators = {
        'wishlistsearch' : "css=#main form",
    }

class WishlistSearchPage_Locators_Base_2(object):
    """locators for WishlistSearchPage object"""

    locators = {
        'wishlistsearch' : "css=.main form",
    }
