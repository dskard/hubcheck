from hubcheck.pageobjects.po_time_base_page import TimeBasePage

class TimeNewTaskPage(TimeBasePage):
    """time new task page"""

    def __init__(self,browser,catalog,groupid=None):
        super(TimeNewTaskPage,self).__init__(browser,catalog)
        self.path = "/time/tasks/new"

        # load hub's classes
        TimeNewTaskPage_Locators = self.load_class('TimeNewTaskPage_Locators')
        TimeNewTaskForm = self.load_class('TimeNewTaskForm')

        # update this object's locator
        self.locators.update(TimeNewTaskPage_Locators.locators)

        # setup page object's components
        self.form = TimeNewTaskForm(self,{'base':'form'})

    def submit_form(self,data):
        return self.form.submit_form(data)

    def cancel_form(self):
        return self.form.cancel_form()

    def populate_form(self,data):
        return self.form.populate_form(data)

class TimeNewTaskPage_Locators_Base(object):
    """locators for TimeNewTaskPage object"""

    locators = {
        'form' : "css=#plg_time_tasks",
    }
