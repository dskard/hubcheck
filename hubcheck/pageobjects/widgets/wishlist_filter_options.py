from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class WishlistFilterOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(WishlistFilterOptions,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistFilterOptions_Locators = self.load_class('WishlistFilterOptions_Locators')

        # update this object's locator
        self.locators.update(WishlistFilterOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.all            = Link(self,{'base':'all'})
        self.active         = Link(self,{'base':'active'})
        self.accepted       = Link(self,{'base':'accepted'})
        self.rejected       = Link(self,{'base':'rejected'})
        self.granted        = Link(self,{'base':'granted'})
        self.submittedbyme  = Link(self,{'base':'submittedbyme'})
        self.public         = Link(self,{'base':'public'})
        self.private        = Link(self,{'base':'private'})
        self.assignedtome   = Link(self,{'base':'assignedtome'})

        self.field = ['all','active','accepted','rejected',
                      'granted','submittedbyme','public',
                      'private','assignedtome']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        widgets = [self.all, self.active, self.accepted, \
                   self.rejected, self.granted]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        widgets = [self.all, self.active, self.accepted, \
                   self.rejected, self.granted, self.submittedbyme]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        self._checkLocators(widgets,cltype)


    def select(self,option):

        if not option in self.fields:
            raise ValueError("invalid button: %s" % (option))
        link = getattr(self,option)
        link.click()


class WishlistFilterOptions_Locators_Base(object):
    """locators for WishlistFilterOptions object"""

    locators = {
        'base'          : "css=.filter-options",
        'all'           : "css=li:nth-child(1) a",
        'active'        : "css=li:nth-child(2) a",
        'accepted'      : "css=li:nth-child(3) a",
        'rejected'      : "css=li:nth-child(4) a",
        'granted'       : "css=li:nth-child(5) a",
        'submittedbyme' : "css=li:nth-child(6) a",
        'public'        : "css=li:nth-child(7) a",
        'private'       : "css=li:nth-child(8) a",
        'assignedtome'  : "css=li:nth-child(9) a",
    }
