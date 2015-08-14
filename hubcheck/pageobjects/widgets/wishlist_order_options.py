from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class WishlistOrderOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistOrderOptions,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistOrderOptions_Locators = self.load_class('WishlistOrderOptions_Locators')

        # update this object's locator
        self.locators.update(WishlistOrderOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.date         = Link(self,{'base':'date'})
        self.submitter    = Link(self,{'base':'submitter'})
        self.feedback     = Link(self,{'base':'feedback'})
        self.ranking      = Link(self,{'base':'ranking'})

        self.fields = ['date','submitter','feedback','ranking']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        widgets = [self.date, self.submitter, self.feedback]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        widgets = [self.date, self.submitter, self.feedback]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        self._checkLocators(widgets,cltype)


    def select(self,option):

        if not option in self.fields:
            raise ValueError("invalid button: %s" % (option))
        link = getattr(self,option)
        link.click()


class WishlistOrderOptions_Locators_Base(object):
    """locators for WishlistOrderOptions object"""

    locators = {
        'base'          : "css=.order-options",
        'ranking'       : "css=li:nth-child(4) a",
        'feedback'      : "css=li:nth-child(3) a",
        'submitter'     : "css=li:nth-child(2) a",
        'date'          : "css=li:nth-child(1) a",
    }
