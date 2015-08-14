from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text

class LoginRemindForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(LoginRemindForm,self).__init__(owner,locatordict)

        # load hub's classes
        LoginRemindForm_Locators = self.load_class('LoginRemindForm_Locators')

        # update this object's locator
        self.locators.update(LoginRemindForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.email     = Text(self,{'base':'email'})

        self.fields += ['email']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def recover_username(self,email):
        """fill in the recovery form and submit"""

        return self.submit_form(data={'email':email})


class LoginRemindForm_Locators_Base(object):
    """locators for LoginRemindForm object"""

    locators = {
        'base'      : "css=#hubForm",
        'email'     : "css=#email",
        'submit'    : "css=#hubForm .validate",
    }

