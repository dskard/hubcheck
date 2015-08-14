from hubcheck.pageobjects.basepagewidget import BasePageWidget

class MembersProfileForm1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileForm1,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileForm_Locators  = self.load_class('MembersProfileForm_Locators')
        MembersProfileBiography      = self.load_class('MembersProfileBiography')
        MembersProfileCitizenship    = self.load_class('MembersProfileCitizenship')
        MembersProfileEmail          = self.load_class('MembersProfileEmail')
        MembersProfileEmployment     = self.load_class('MembersProfileEmployment')
        MembersProfileGender         = self.load_class('MembersProfileGender')
        MembersProfileInterests      = self.load_class('MembersProfileInterests')
        MembersProfileMailPreference = self.load_class('MembersProfileMailPreference')
        MembersProfileName           = self.load_class('MembersProfileName')
        MembersProfileOrganization   = self.load_class('MembersProfileOrganization')
        MembersProfilePassword       = self.load_class('MembersProfilePassword')
        MembersProfileResidence      = self.load_class('MembersProfileResidence')
        MembersProfileWebsite        = self.load_class('MembersProfileWebsite')
        MembersProfileTelephone      = self.load_class('MembersProfileTelephone')

        # update this object's locator
        self.locators.update(MembersProfileForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.biography      = MembersProfileBiography(self,{'base':'biography'})
        self.citizenship    = MembersProfileCitizenship(self,{'base':'citizenship'})
        self.email          = MembersProfileEmail(self,{'base':'email'})
        self.employment     = MembersProfileEmployment(self,{'base':'employment'})
        self.gender         = MembersProfileGender(self,{'base':'gender'})
        self.interests      = MembersProfileInterests(self,{'base':'interests'})
        self.mailpreference = MembersProfileMailPreference(self,{'base':'mailpreference'})
        self.name           = MembersProfileName(self,{'base':'name'})
        self.organization   = MembersProfileOrganization(self,{'base':'organization'})
        self.password       = MembersProfilePassword(self,{'base':'password'})
        self.residence      = MembersProfileResidence(self,{'base':'residence'})
        self.website        = MembersProfileWebsite(self,{'base':'website'})
        self.telephone      = MembersProfileTelephone(self,{'base':'telephone'})

        # update the component's locators with this objects overrides
        self._updateLocators()


class MembersProfileForm2(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(MembersProfileForm2,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileForm_Locators  = self.load_class('MembersProfileForm_Locators')
        MembersProfileBiography      = self.load_class('MembersProfileBiography')
        MembersProfileEmail          = self.load_class('MembersProfileEmail')
        MembersProfileName           = self.load_class('MembersProfileName')
        MembersProfilePassword       = self.load_class('MembersProfilePassword')

        # update this object's locator
        self.locators.update(MembersProfileForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.biography = MembersProfileBiography(self,{'base':'biography'})
        self.email     = MembersProfileEmail(self,{'base':'email'})
        self.name      = MembersProfileName(self,{'base':'name'})
        self.password  = MembersProfilePassword(self,{'base':'password'})

        # update the component's locators with this objects overrides
        self._updateLocators()


class MembersProfileForm3(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileForm3,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileForm_Locators  = self.load_class('MembersProfileForm_Locators')
        MembersProfileBiography      = self.load_class('MembersProfileBiography')
        MembersProfileEmail          = self.load_class('MembersProfileEmail')
        MembersProfileEmployment     = self.load_class('MembersProfileEmployment')
        MembersProfileInterests      = self.load_class('MembersProfileInterests')
        MembersProfileMailPreference = self.load_class('MembersProfileMailPreference')
        MembersProfileName           = self.load_class('MembersProfileName')
        MembersProfileOrganization   = self.load_class('MembersProfileOrganization')
        MembersProfileWebsite        = self.load_class('MembersProfileWebsite')
        MembersProfileTelephone      = self.load_class('MembersProfileTelephone')

        # update this object's locator
        self.locators.update(MembersProfileForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.biography      = MembersProfileBiography(self,{'base':'biography'})
        self.email          = MembersProfileEmail(self,{'base':'email'})
        self.employment     = MembersProfileEmployment(self,{'base':'employment'})
        self.interests      = MembersProfileInterests(self,{'base':'interests'})
        self.mailpreference = MembersProfileMailPreference(self,{'base':'mailpreference'})
        self.name           = MembersProfileName(self,{'base':'name'})
        self.organization   = MembersProfileOrganization(self,{'base':'organization'})
        self.website        = MembersProfileWebsite(self,{'base':'website'})
        self.telephone      = MembersProfileTelephone(self,{'base':'telephone'})

        # update the component's locators with this objects overrides
        self._updateLocators()

class MembersProfileForm_Locators_Base(object):
    """locators for MembersProfileForm object"""

    locators = {
        'base'           : "css=#profile",
        'biography'      : "css=.profile-bio",
        'citizenship'    : "css=.profile-countryorigin",
        'email'          : "css=.profile-email",
        'employment'     : "css=.profile-orgtype",
        'gender'         : "css=.profile-sex",
        'interests'      : "css=.profile-interests",
        'mailpreference' : "css=.profile-optin",
        'name'           : "css=.profile-name",
        'organization'   : "css=.profile-org",
        'password'       : "css=.profile-password",
        'residence'      : "css=.profile-countryresident",
        'website'        : "css=.profile-web",
        'telephone'      : "css=.profile-phone",
    }
