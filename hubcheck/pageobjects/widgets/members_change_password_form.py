from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.form_base import FormBase

class MembersChangePasswordForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(MembersChangePasswordForm,self).__init__(owner,locatordict)

        # load hub's classes
        MembersChangePasswordForm_Locators = self.load_class('MembersChangePasswordForm_Locators')

        # update this object's locator
        self.locators.update(MembersChangePasswordForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.currentpassword    = Text(self,{'base':'currentpassword'})
        self.newpassword        = Text(self,{'base':'newpassword'})
        self.confirmpassword    = Text(self,{'base':'confirmpassword'})

        self.fields = ['currentpassword','newpassword','confirmpassword']

        # update the component's locators with this objects overrides
        self._updateLocators()

class MembersChangePasswordForm_Locators_Base(object):
    """locators for MembersChangePasswordForm object"""

    locators = {
        'base'               : "css=#hubForm",
        'currentpassword'    : "css=#oldpass",
        'newpassword'        : "css=#newpass",
        'confirmpassword'    : "css=#newpass2",
        'submit'             : "css=#password-change-save",
    }

class MembersChangePasswordForm_Locators_Base_2(object):
    """locators for MembersChangePasswordForm object"""

    locators = {
        'base'               : "css=#hubForm",
        'currentpassword'    : "css=#oldpass",
        'newpassword'        : "css=#newpass",
        'confirmpassword'    : "css=#newpass2",
        'submit'             : "css=.submit input[name='change']",
    }
