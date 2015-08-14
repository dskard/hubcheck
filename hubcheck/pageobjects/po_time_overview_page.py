from hubcheck.pageobjects.po_time_base_page import TimeBasePage
from hubcheck.pageobjects.basepageelement import Link

class TimeOverviewPage(TimeBasePage):
    """time overview page"""

    def __init__(self,browser,catalog,groupid=None):
        super(TimeOverviewPage,self).__init__(browser,catalog)
        self.path = "/time/overview"

        # load hub's classes
        TimeOverviewPage_Locators = self.load_class('TimeOverviewPage_Locators')
        TimeOverview = self.load_class('TimeOverview')

        # update this object's locator
        self.locators.update(TimeOverviewPage_Locators.locators)

        # setup page object's components
        self.overview     = TimeOverview(self,{'base':'overview'})

    def get_active_hubs_count(self):
        return self.overview.get_active_hubs_count()

    def get_active_tasks_count(self):
        return self.overview.get_active_tasks_count()

    def get_total_hours_count(self):
        return self.overview.get_total_hours_count()

    def goto_hubs(self):
        self.overview.goto_hubs()

    def goto_tasks(self):
        self.overview.goto_tasks()

    def goto_records(self):
        self.overview.goto_records()


class TimeOverviewPage_Locators_Base(object):
    """locators for TimeOverviewPage object"""

    locators = {
        'overview' : "css=#plg_time_overview",
    }
