from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class TicketListSortOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketListSortOptions,self).__init__(owner,locatordict)

        # load hub's classes
        TicketListSortOptions_Locators = self.load_class('TicketListSortOptions_Locators')

        # update this object's locator
        self.locators.update(TicketListSortOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.age            = Link(self,{'base':'age'})
        self.status         = Link(self,{'base':'status'})
        self.severity       = Link(self,{'base':'severity'})
        self.summary        = Link(self,{'base':'summary'})
        self.group          = Link(self,{'base':'group'})
        self.assignee       = Link(self,{'base':'assignee'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def sort_by_age(self):

        self.age.click()


    def sort_by_status(self):

        self.status.click()


    def sort_by_severity(self):

        self.severity.click()


    def sort_by_summary(self):

        self.summary.click()


    def sort_by_group(self):

        self.group.click()


    def sort_by_assignee(self):

        self.assignee.click()


class TicketListSortOptions_Locators_Base(object):
    """locators for TicketListSortOptions object"""

    locators = {
        'base'       : "css=#tktlist",
        'age'        : "css=.sort-age",
        'status'     : "css=.sort-status",
        'severity'   : "css=.sort-severity",
        'summary'    : "css=.sort-summary",
        'group'      : "css=.sort-group",
        'assignee'   : "css=.sort-owner",
    }
