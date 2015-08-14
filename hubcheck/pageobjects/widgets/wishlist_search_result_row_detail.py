from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class WishlistSearchResultRowDetail(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistSearchResultRowDetail,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistSearchResultRowDetail_Locators = \
            self.load_class('WishlistSearchResultRowDetail_Locators')

        # update this object's locator
        self.locators.update(WishlistSearchResultRowDetail_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.proposedby   = Link(self,{'base':'proposedby'})
        self.time         = TextReadOnly(self,{'base':'time'})
        self.date         = TextReadOnly(self,{'base':'date'})
        self.comments     = Link(self,{'base':'comments'})

        # update the component's locators with this objects overrides
        self._updateLocators()

class WishlistSearchResultRowDetail_Locators_Base(object):
    """locators for WishlistSearchResultRowDetail object"""

    locators = {
        'base'           : "css=.entry-details",
        'proposedby'     : "css=a",
        'time'           : "css=.entry-time",
        'date'           : "css=.entry-date",
        'comments'       : "css=.entry-comments a",
    }
