from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextArea

class GroupsInviteForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsInviteForm,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsInviteForm_Locators = self.load_class('GroupsInviteForm_Locators')

        # update this object's locator
        self.locators.update(GroupsInviteForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name    = TextAC(self,{'base':'name',
                                    'aclocatorid':'nameac',
                                    'choicelocatorid':'nameacchoices',
                                    'tokenlocatorid':'nameactoken',
                                    'deletelocatorid':'nameacdelete'})
        self.message = TextArea(self,{'base':'message'})

        self.fields += ['name','message']

        # update the component's locators with this objects overrides
        self._updateLocators()

class GroupsInviteForm_Locators_Base(object):
    """locators for GroupsInviteForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'name'              : "css=#acmembers",
        'nameac'            : "css=#token-input-acmembers",
        'nameacchoices'     : "css=.token-input-dropdown-acm",
        'nameactoken'       : "css=.token-input-token-acm",
        'nameacdelete'      : "css=.token-input-delete-token-acm",
        'message'           : "css=#msg",
        'submit'            : "css=#hubForm [type='submit']",
    }
