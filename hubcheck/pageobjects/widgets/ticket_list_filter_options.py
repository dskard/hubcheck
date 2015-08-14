from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text

class TicketListFilterOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketListFilterOptions,self).__init__(owner,locatordict)

        # load hub's classes
        TicketListFilterOptions_Locators = self.load_class('TicketListFilterOptions_Locators')

        # update this object's locator
        self.locators.update(TicketListFilterOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.find           = Text(self,{'base':'find'})
        self.help           = Link(self,{'base':'help'})
        self.show           = Select(self,{'base':'show'})
        self.submit         = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsNonAdmin(self, widgets=None, cltype='NonAdmin'):

        widgets = [self.show, self.submit]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self, widgets=None, cltype='Admin'):

        self._checkLocators(widgets,cltype)


    def filter_by_keyword(self,value):

        self.find.value = value
        self.submit.click()


    def filter_by_dropdown(self,value):

        self.show.value = value
        self.submit.click()

class TicketListFilterOptions_Locators_Base(object):
    """locators for TicketListFilterOptions object"""

    locators = {
        'base'          : "css=.filters",
        'find'          : "css=#find",
        'help'          : "css=.fixedImgTip",
        'show'          : "css=[name='show']",
        'submit'        : "css=[type='submit']",
    }

class TicketListFilterOptions2(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketListFilterOptions2,self).__init__(owner,locatordict)

        # load hub's classes
        TicketListFilterOptions_Locators = self.load_class('TicketListFilterOptions_Locators')

        # update this object's locator
        self.locators.update(TicketListFilterOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.find           = Text(self,{'base':'find'})
        self.submit         = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsAdmin(self, widgets=None, cltype='Admin'):

        self._checkLocators(widgets,cltype)


    def filter_by_keyword(self,value):

        self.find.value = value
        self.submit.click()


class TicketListFilterOptions2_Locators_Base(object):
    """locators for TicketListFilterOptions2 object"""

    locators = {
        'base'          : "css=.filters",
        'find'          : "css=#filter-search",
        'submit'        : "css=[type='submit']",
    }
