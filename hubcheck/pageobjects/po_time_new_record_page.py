from hubcheck.pageobjects.po_time_base_page import TimeBasePage

class TimeNewRecordPage(TimeBasePage):
    """time new record page"""

    def __init__(self,browser,catalog,groupid=None):
        super(TimeNewRecordPage,self).__init__(browser,catalog)
        self.path = "/time/records/new"

        # load hub's classes
        TimeNewRecordPage_Locators = self.load_class('TimeNewRecordPage_Locators')
        TimeNewRecordForm = self.load_class('TimeNewRecordForm')

        # update this object's locator
        self.locators.update(TimeNewRecordPage_Locators.locators)

        # setup page object's components
        self.form     = TimeNewRecordForm(self,{'base':'form'})

    def submit_form(self,data):
        return self.form.submit_form(data)

    def cancel_form(self):
        return self.form.cancel_form()

    def populate_form(self,data):
        return self.form.populate_form(data)

    def get_name(self):
        return self.form.get_name()

class TimeNewRecordPage_Locators_Base(object):
    """locators for TimeNewRecordPage object"""

    locators = {
        'form' : "css=#plg_time_records",
    }
