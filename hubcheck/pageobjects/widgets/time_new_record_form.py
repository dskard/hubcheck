from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Link
import re

class TimeNewRecordForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TimeNewRecordForm,self).__init__(owner,locatordict)

        # load hub's classes
        TimeNewRecordForm_Locators = self.load_class('TimeNewRecordForm_Locators')

        # update this object's locator
        self.locators.update(TimeNewRecordForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name            = TextReadOnly(self,{'base':'name'})
        self.hours           = Select(self,{'base':'hours'})
        self.minutes         = Select(self,{'base':'minutes'})
        self.date            = Text(self,{'base':'date'})
        self.hub             = Select(self,{'base':'hub'})
        self.task            = Select(self,{'base':'task'})
        self.description     = TextArea(self,{'base':'description'})
        self.submit          = Button(self,{'base':'submit'})
        self.cancel          = Link(self,{'base':'cancel'})

        self.fields = ['hours','minutes','date','hub','task','description']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def submit_form(self,data):

        self.populate_form(data)
        self.submit.click()


    def cancel_form(self):

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

    def get_name(self):
        return re.sub('User: ','',self.name.value)


class TimeNewRecordForm_Locators_Base(object):
    """locators for TimeNewRecordForm object"""

    locators = {
        'base'           : "css=#plg_time_records",
        'name'           : "css=#uname-group",
        'hours'          : "css=#htime",
        'minutes'        : "css=#mtime",
        'date'           : "css=#datepicker",
        'hub'            : "css=#hub_id",
        'task'           : "css=#task",
        'description'    : "css=#description",
        'submit'         : "css=#plg_time_records [type='submit']",
        'cancel'         : "css=.cancel-button",
    }
