from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class TimeBasePage(GenericPage):
    """time page"""

    def __init__(self,browser,catalog,groupid=None):
        super(TimeBasePage,self).__init__(browser,catalog)
        self.path = "/time"

        # load hub's classes
        TimeBasePage_Locators = self.load_class('TimeBasePage_Locators')
        TimeNavigation        = self.load_class('TimeNavigation')

        # update this object's locator
        self.locators.update(TimeBasePage_Locators.locators)

        # setup page object's components
        self.navigation = TimeNavigation(self,{'base':'navigation'})

    def goto_overview(self):
        self.navigation.goto_overview()

    def goto_records(self):
        self.navigation.goto_records()

    def goto_tasks(self):
        self.navigation.goto_tasks()

    def goto_hubs(self):
        self.navigation.goto_hubs()

    def goto_reports(self):
        self.navigation.goto_reports()

    def goto_new_record(self):
        self.navigation.goto_new_record()

    def goto_new_task(self):
        self.navigation.goto_new_task()

    def goto_new_hub(self):
        self.navigation.goto_new_hub()


class TimeBasePage_Locators_Base(object):
    """locators for TimeBasePage object"""

    locators = {
        'navigation' : "css=#time_sidebar",
    }
