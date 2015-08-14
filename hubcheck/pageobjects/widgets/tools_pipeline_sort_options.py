from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class ToolsPipelineSortOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsPipelineSortOptions,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsPipelineSortOptions_Locators = self.load_class('ToolsPipelineSortOptions_Locators')

        # update this object's locator
        self.locators.update(ToolsPipelineSortOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.status_change  = Link(self,{'base':'status_change'})
        self.priority       = Link(self,{'base':'priority'})
        self.name           = Link(self,{'base':'name'})
        self.date           = Link(self,{'base':'date'})
        self.status         = Link(self,{'base':'status'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def order_by_status_change(self):

        self.status_change.click()


    def order_by_priority(self):

        self.order_by_priority.click()


    def order_by_name(self):

        self.name.click()


    def order_by_date(self):

        self.date.click()


    def order_by_status(self):

        self.status.click()


class ToolsPipelineSortOptions_Locators_Base(object):
    """locators for ToolsPipelineSortOptions object"""

    locators = {
        'base'          : "css=.order-options",
        'status_change' : "css=a[title='Status change']",
        'priority'      : "css=a[title='Priority']",
        'name'          : "css=a[title='Name']",
        'date'          : "css=a[title='Date']",
        'status'        : "css=a[title='Status (default)']",
    }

class ToolsPipelineSortOptions_Locators_Base_2(object):
    """locators for ToolsPipelineSortOptions object"""

    locators = {
        'base'          : "css=.order-options",
        'status_change' : "css=.sort-change",
        'priority'      : "css=.sort-priority",
        'name'          : "css=.sort-name",
        'date'          : "css=.sort-date",
        'status'        : "css=.sort-status",
    }
