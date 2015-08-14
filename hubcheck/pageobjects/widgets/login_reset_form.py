from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text

class LoginResetForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(LoginResetForm,self).__init__(owner,locatordict)

        # load hub's classes
        LoginResetForm_Locators = self.load_class('LoginResetForm_Locators')

        # update this object's locator
        self.locators.update(LoginResetForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username  = Text(self,{'base':'username'})

        self.fields += ['username']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def email_verification_token(self,username):
        """fill in the email verification form"""

        return self.submit_form(data={'username':username})


class LoginResetForm_Locators_Base(object):
    """locators for LoginResetForm object"""

    locators = {
        'base'      : "css=#hubForm",
        'username'  : "css=#username",
        'submit'    : "css=#hubForm .validate",
    }

