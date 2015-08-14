from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.widgets.trouble_report_form import TroubleReportForm

class NeedHelpForm(TroubleReportForm):
    def __init__(self, owner, locatordict={}, refreshCaptchaCB=None):
        super(NeedHelpForm,self).__init__(owner,locatordict,refreshCaptchaCB)

        # load hub's classes
        NeedHelpForm_Locators = self.load_class('NeedHelpForm_Locators')

        # update this object's locator
        self.locators.update(NeedHelpForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.kb       = Link(self,{'base':'kb'})
        self.qa       = Link(self,{'base':'qa'})
        self.wishlist = Link(self,{'base':'wishlist'})
        self.tickets  = Link(self,{'base':'tickets'})
        self.close    = Link(self,{'base':'close'},self._onCloseClick)

        # update the component's locators with this objects overrides
        self._updateLocators()


    def is_open(self):
        """check if the need help form/slide is being displayed"""

        e = self.find_element(self.locators['close'])
        return e.is_displayed()


    def _onCloseClick(self):
        """callback function for closing Need Help Form"""

        self._po.wait_for_page_element_displayed(
            loc=self.locators['close'],displayed=False)


class NeedHelpForm_Locators_Base(object):
    """locators for NeedHelpForm object"""

    locators = {
        'base'     : "css=#help-pane",
        'trform'   : "css=#troublereport",
        'kb'       : "css=.help-kb a",
        'qa'       : "css=.help-qa a",
        'wishlist' : "css=.help-wish a",
        'tickets'  : "css=.help-tickets a",
        'close'    : "css=#help-btn-close",
    }

