from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class WishlistNewWishPage(GenericPage):
    """wishlist search"""

    def __init__(self,browser,catalog,listid='1'):
        super(WishlistNewWishPage,self).__init__(browser,catalog)
        self.listid = listid
        self.path = "/wishlist/general/%s/add" % (self.listid)

        # load hub's classes
        WishlistNewWishPage_Locators = self.load_class('WishlistNewWishPage_Locators')
        WishlistNewWishForm = self.load_class('WishlistNewWishForm')

        # update this object's locator
        self.locators.update(WishlistNewWishPage_Locators.locators)

        # setup page object's components
        self.wishform     = WishlistNewWishForm(self,{'base':'wishform'})
        self.allwishes    = Link(self,{'base':'allwishes'})

    def submit_wish(self,data):
        return self.wishform.submit_wish(data)

class WishlistNewWishPage_Locators_Base(object):
    """locators for WishlistNewWishPage object"""

    locators = {
        'wishform'  : "css=#hubForm",
        'allwishes' : "css=.nav_wishlist",
    }
