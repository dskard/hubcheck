from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Checkbox, Button

class GroupsWikiDeleteForm(FormBase):
    def __init__(self, owner, locatordict=None):
        super(GroupsWikiDeleteForm,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiDeleteForm_Locators = self.load_class('GroupsWikiDeleteForm_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiDeleteForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.confirm = Checkbox(self,{'base':'confirm'})

        self.fields += ['confirm']

        # update the component's locators with this objects overrides
        self._updateLocators()

    def confirm_delete(self):

        self.confirm.value = True


    def delete_wiki_page(self):

        self.submit_form(data={'confirm':True})


class GroupsWikiDeleteForm_Locators_Base(object):
    """locators for GroupsWikiDeleteForm object"""

    locators = {
        'base'    : "css=#hubForm",
        'confirm' : "css=#hubForm [name='confirm']",
        'submit'  : "css=#hubForm [type='submit']",
    }

