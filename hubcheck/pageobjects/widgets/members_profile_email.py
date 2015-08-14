from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileEmail(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileEmail,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileEmail_Locators = self.load_class('MembersProfileEmail_Locators')

        # update this object's locator
        self.locators.update(MembersProfileEmail_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.email          = Text(self,{'base':'email'})
        self.confirmemail   = Text(self,{'base':'confirmemail'})
        self.access         = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of email, confirmemail, and access values"""

        return {'email'         : self.email.value(),
                'confirmemail'  : self.confirmemail.value(),
                'access'        : self.access.value()}


    def update(self,email=None,confirmemail=None,access=None):
        """update values for email, confirmemail, and access values"""

        if email != None:
            self.email.value = email
        if confirmemail != None:
            self.confirmemail.value = confirmemail
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileEmail_Locators_Base(object):
    """locators for MembersProfileEmail object"""

    locators = {
        'base'          : "css=.profile-email",
        'email'         : "css=#profile-email",
        'confirmemail'  : "css=#profile-email2",
        'access'        : "css=.profile-email select[name='access[email]']",
        'sectionkey'    : "css=.profile-email .key",
        'sectionvalue'  : "css=.profile-email .value",
        'open'          : "css=.profile-email .edit-profile-section",
        'close'         : "css=.profile-email .edit-profile-section",
        'save'          : "css=.profile-email .section-edit-submit",
        'cancel'        : "css=.profile-email .section-edit-cancel",
    }
