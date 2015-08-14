from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import TextArea

class GroupsDeleteForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsDeleteForm,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsDeleteForm_Locators = self.load_class('GroupsDeleteForm_Locators')

        # update this object's locator defaults
        self.locators.update(GroupsDeleteForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.message = TextArea(self,{'base':'message'})
        self.confirm = Checkbox(self,{'base':'confirm'})

        self.fields += ['message','confirm']

        # update the component's locators with this objects overrides
        self._updateLocators()

class GroupsDeleteForm_Locators_Base(object):
    """locators for GroupsDeleteForm object"""

    locators = {
        'base'    : "css=#hubForm",
        'message' : "css=#msg",
        'confirm' : "css=#confirmdel",
        'submit'  : "css=#hubForm [type='submit']",
    }
