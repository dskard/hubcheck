from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextArea

class ToolsStatusAdministratorForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusAdministratorForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusAdministratorForm_Locators = self.load_class('ToolsStatusAdministratorForm_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusAdministratorForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.status     = Select(self,{'base':'status'})
        self.priority   = Select(self,{'base':'priority'})
        self.message    = TextArea(self,{'base':'message'})
        self.submit     = Button(self,{'base':'submit'})

        self.fields = ['status','priority','message']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ToolsStatusAdministratorForm_Locators_Base(object):
    """locators for ToolsStatusAdministratorForm object"""

    locators = {
        'base'          : "css=#adminForm",
        'status'        : "css=[name='newstate']",
        'priority'      : "css=[name='priority']",
        'message'       : "css=#comment",
        'submit'        : "css=#adminForm input[type='submit']",
    }

