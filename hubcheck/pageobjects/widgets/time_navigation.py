from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class TimeNavigation(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TimeNavigation,self).__init__(owner,locatordict)

        # load hub's classes
        TimeNavigation_Locators = self.load_class('TimeNavigation_Locators')

        # update this object's locator
        self.locators.update(TimeNavigation_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.overview        = Link(self,{'base':'overview'})
        self.records         = Link(self,{'base':'records'})
        self.tasks           = Link(self,{'base':'tasks'})
        self.hubs            = Link(self,{'base':'hubs'})
        self.reports         = Link(self,{'base':'reports'})
        self.new_record      = Link(self,{'base':'new_record'})
        self.new_task        = Link(self,{'base':'new_task'})
        self.new_hub         = Link(self,{'base':'new_hub'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_overview(self):

        self.overview.click()


    def goto_records(self):

        self.records.click()


    def goto_tasks(self):

        self.tasks.click()


    def goto_hubs(self):

        self.hubs.click()


    def goto_reports(self):

        self.reports.click()


    def goto_new_record(self):

        self.new_record.click()


    def goto_new_task(self):

        self.new_task.click()


    def goto_new_hub(self):

        self.new_hub.click()


class TimeNavigation_Locators_Base(object):
    """locators for TimeNavigation object"""

    locators = {
        'base'           : "css=#time_sidebar",
        'overview'       : "xpath=//a[text()='Overview']",
        'records'        : "xpath=//a[text()='Records']",
        'tasks'          : "xpath=//a[text()='Tasks']",
        'hubs'           : "xpath=//a[text()='Hubs']",
        'reports'        : "xpath=//a[text()='Reports']",
        'new_record'     : "xpath=//a[text()='New records']",
        'new_task'       : "xpath=//a[text()='New Task']",
        'new_hub'        : "xpath=//a[text()='New hub']",
    }
