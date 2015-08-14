from hubcheck.pageobjects.po_time_base_page import TimeBasePage

class TimeNewHubPage(TimeBasePage):
    """time new task page"""

    def __init__(self,browser,catalog,groupid=None):
        super(TimeNewHubPage,self).__init__(browser,catalog)
        self.path = "/time/hubs/new"

        # load hub's classes
        TimeNewHubPage_Locators = self.load_class('TimeNewHubPage_Locators')
        TimeNewHubForm = self.load_class('TimeNewHubForm')

        # update this object's locator
        self.locators.update(TimeNewHubPage_Locators.locators)

        # setup page object's components
        self.form     = TimeNewHubForm(self,{'base':'form'})

    def submit_form(self,data):
        return self.form.submit_form(data)

    def cancel_form(self):
        return self.form.cancel_form()

    def populate_form(self,data):
        return self.form.populate_form(data)

class TimeNewHubPage_Locators_Base(object):
    """locators for TimeNewHubPage object"""

    locators = {
        'form' : "css=#plg_time_hubs",
    }
