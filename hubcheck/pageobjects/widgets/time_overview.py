from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class TimeOverview(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TimeOverview,self).__init__(owner,locatordict)

        # load hub's classes
        TimeOverview_Locators = self.load_class('TimeOverview_Locators')

        # update this object's locator
        self.locators.update(TimeOverview_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.active_hubs     = Link(self,{'base':'active_hubs'})
        self.active_tasks    = Link(self,{'base':'active_tasks'})
        self.total_hours     = Link(self,{'base':'total_hours'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_active_hubs_count(self):

        return self.active_hubs.value


    def get_active_tasks_count(self):

        return self.active_tasks.value


    def get_total_hours_count(self):

        return self.total_hours.value


    def goto_hubs(self):

        self.active_hubs.click()


    def goto_tasks(self):

        self.active_tasks.click()


    def goto_records(self):

        self.total_hours.click()


class TimeOverview_Locators_Base(object):
    """locators for TimeOverview object"""

    locators = {
        'base'           : "css=#plg_time_overview",
        'overview'       : "xpath=//a[text()='Overview']",
        'records'        : "xpath=//a[text()='Records']",
        'tasks'          : "xpath=//a[text()='Tasks']",
        'hubs'           : "xpath=//a[text()='Hubs']",
        'reports'        : "xpath=//a[text()='Reports']",
        'new_record'     : "xpath=//a[text()='New records']",
        'new_task'       : "xpath=//a[text()='New Task']",
        'new_hub'        : "xpath=//a[text()='New hub']",
    }
