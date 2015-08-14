from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class WishlistSearchResultRow(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistSearchResultRow,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistSearchResultRow_Locators = self.load_class('WishlistSearchResultRow_Locators')
        WishlistSearchResultRowDetail = self.load_class('WishlistSearchResultRowDetail')
        WishlistVote = self.load_class('WishlistVote')

        # update this object's locator
        self.locators.update(WishlistSearchResultRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.ranked       = TextReadOnly(self,{'base':'ranked'})
        self.title        = Link(self,{'base':'title'})
        self.details      = WishlistSearchResultRowDetail(self,{'base':'details'})
        self.vote_like    = WishlistVote(self,{'base':'vote-like'})
        self.vote_dislike = WishlistVote(self,{'base':'vote-dislike'})
        self.rank         = Link(self,{'base':'rank'})

        # update the component's locators with this objects overrides
        self._updateLocators()

class WishlistSearchResultRow_Locators_Base(object):
    """locators for WishlistSearchResultRow object"""

    locators = {
        'base'           : "css=tr",
        'ranked'         : "css=th",
        'title'          : "css=td:nth-child(1) .entry-title",
        'details'        : "css=td:nth-child(1) .entry-details",
        'vote-like'      : "css=.vote-like",
        'vote-dislike'   : "css=.vote-dislike",
        'rank'           : "css=.rankit",
    }
