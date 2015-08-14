from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Link

class TimeNewTaskForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TimeNewTaskForm,self).__init__(owner,locatordict)

        # load hub's classes
        TimeNewTaskForm_Locators = self.load_class('TimeNewTaskForm_Locators')

        # update this object's locator
        self.locators.update(TimeNewTaskForm_Locators.locators)

        # setup page object's components
        self.name            = Text(self,{'base':'name'})
        self.active          = Radio(self,{'Yes':'active_yes','No':'active_no'})
        self.hub             = Select(self,{'base':'hub'})
        self.start_date      = Text(self,{'base':'start_date'})
        self.end_date        = Text(self,{'base':'end_date'})
        self.priority        = Select(self,{'base':'priority'})
        self.assignee        = Select(self,{'base':'assignee'})
        self.liaison         = Select(self,{'base':'liaison'})
        self.description     = TextArea(self,{'base':'description'})
        self.submit          = Button(self,{'base':'submit'})
        self.cancel          = Link(self,{'base':'cancel'})

        self.fields = ['name','active','hub','start_date','end_date',
                       'priority','assignee','liaison','description']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def submit_form(self,data):

        self.populate_form(data)
        self.submit.click()


    def cancel_form(self,data):

        self.cancel.click()


    def populate_form(self,data):

        # data is either a dictionary or string
        if isinstance(data,dict):
            for k,v in data.items():
                if v is None:
                    # no value to set
                    continue
                if not k in self.fields:
                    # bail, the key is not a field
                    raise ValueError("invalid form field: %s" % (k))
                # find the widget in the object's dictionary and set its value
                widget = getattr(self,k)
                widget.value = v
        else:
            self.problem.value = data


class TimeNewTaskForm_Locators_Base(object):
    """locators for TimeNewTaskForm object"""

    locators = {
        'base'           : "css=#plg_time_tasks",
        'name'           : "css=#name",
        'active_yes'     : "css=#active_yes",
        'active_no'      : "css=#active_no",
        'hub'            : "css=#hub_id",
        'start_date'     : "css=#startdate",
        'end_date'       : "css=#enddate",
        'priority'       : "css=#priority",
        'assignee'       : "css=#assignee",
        'liaison'        : "css=#liaison",
        'description'    : "css=#description",
        'submit'         : "css=#plg_time_tasks [type='submit']",
        'cancel'         : "css=.cancel-button",
    }
