from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class WishlistVote(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistVote,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistVote_Locators = self.load_class('WishlistVote_Locators')

        # update this object's locator
        self.locators.update(WishlistVote_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.vote = Link(self,{'base':'votebutton'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def click(self):

        self.vote.click()


    #def can_vote(self):
    #
    #    retval = True
    #    e = self.find_element(self.locators['votebutton'])
    #    title = e.get_attribute('title')
    #


class WishlistVote_Locators_Base(object):
    """locators for WishlistVote object"""

    locators = {
        'base'           : "css=.vote-like",
        'votebutton'     : "css=.vote-button",
        'votelink'       : "css=a",
    }
