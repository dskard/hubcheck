from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text

class TimeNewHubForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TimeNewHubForm,self).__init__(owner,locatordict)

        # load hub's classes
        TimeNewHubForm_Locators = self.load_class('TimeNewHubForm_Locators')
        WikiTextArea = self.load_class('WikiTextArea')

        # update this object's locator
        self.locators.update(TimeNewHubForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.hubname         = Text(self,{'base':'hubname'})
        self.contact_name    = Text(self,{'base':'contact_name'})
        self.contact_phone   = Text(self,{'base':'contact_phone'})
        self.contact_email   = Text(self,{'base':'contact_email'})
        self.contact_role    = Text(self,{'base':'contact_role'})
        self.liaison         = Text(self,{'base':'liaison'})
        self.anniversary     = Text(self,{'base':'anniversary'})
        self.support         = Select(self,{'base':'support'})
        self.notes           = WikiTextArea(self,{'base':'notes'})
        self.submit          = Button(self,{'base':'submit'})
        self.cancel          = Link(self,{'base':'cancel'})

        self.fields = ['hubname','contact_name','contact_phone',
                       'contact_email','contact_role','liaison',
                       'anniversary','support','notes']

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


class TimeNewHubForm_Locators_Base(object):
    """locators for TimeNewHubForm object"""

    locators = {
        'base'           : "css=#plg_time_hubs",
        'hubname'        : "css=#name",
        'contact_name'   : "css=#new_name",
        'contact_phone'  : "css=#new_phone",
        'contact_email'  : "css=#new_email",
        'contact_role'   : "css=#new_role",
        'liaison'        : "css=#liaison",
        'anniversary'    : "css=#anniversary_date",
        'support'        : "css=#support_level",
        'notes'          : "css=.wykiwyg",
        'submit'         : "css=#plg_time_hubs [type='submit']",
        'cancel'         : "css=.cancel-button",
    }
