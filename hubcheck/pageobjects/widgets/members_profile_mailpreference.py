from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileMailPreference1(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileMailPreference1,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileMailPreference_Locators = self.load_class('MembersProfileMailPreference_Locators')

        # update this object's locator
        self.locators.update(MembersProfileMailPreference_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.mailpreference = Radio(self,{'Yes':'mail_yes','No':'mail_no'})
        self.access         = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the mailpreference and access values"""

        return {'mailpreference' : self.mailpreference.value(),
                'access'         : self.access.value()}


    def update(self,mailpreference=None,access=None):
        """update the mailpreference and access values"""

        if mailpreference != None:
            self.mailpreference.value = mailpreference
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileMailPreference1_Locators_Base(object):
    """locators for MembersProfileMailPreference2 object"""

    locators = {
        'base'          : "css=.profile-optin",
        'mail_yes'      : "css=#mailPreferenceOptionYes",
        'mail_no'       : "css=#mailPreferenceOptionNo",
        'access'        : "css=.profile-optin select[name='access[optin]']",
        'sectionkey'    : "css=.profile-optin .key",
        'sectionvalue'  : "css=.profile-optin .value",
        'open'          : "css=.profile-optin .edit-profile-section",
        'close'         : "css=.profile-optin .edit-profile-section",
        'save'          : "css=.profile-optin .section-edit-submit",
        'cancel'        : "css=.profile-optin .section-edit-cancel",
    }


class MembersProfileMailPreference2(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileMailPreference2,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileMailPreference_Locators = self.load_class('MembersProfileMailPreference_Locators')

        # update this object's locator
        self.locators.update(MembersProfileMailPreference_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.mailpreference = Select(self,{'base':'mailpref'})
        self.access         = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the mailpreference and access values"""

        return {'mailpreference' : self.mailpreference.value(),
                'access'         : self.access.value()}


    def update(self,mailpreference=None,access=None):
        """update the mailpreference and access values"""

        if mailpreference != None:
            self.mailpreference.value = mailpreference
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileMailPreference2_Locators_Base(object):
    """locators for MembersProfileMailPreference2 object"""

    locators = {
        'base'          : "css=.profile-optin",
        'mailpref'      : "css=.profile-optin select[name='mailPreferenceOption']",
        'access'        : "css=.profile-optin select[name='access[optin]']",
        'sectionkey'    : "css=.profile-optin .key",
        'sectionvalue'  : "css=.profile-optin .value",
        'open'          : "css=.profile-optin .edit-profile-section",
        'close'         : "css=.profile-optin .edit-profile-section",
        'save'          : "css=.profile-optin .section-edit-submit",
        'cancel'        : "css=.profile-optin .section-edit-cancel",
    }
