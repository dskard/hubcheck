from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileResidence(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileResidence,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileResidence_Locators = self.load_class('MembersProfileResidence_Locators')

        # update this object's locator
        self.locators.update(MembersProfileResidence_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.cresidentus = Radio(self,{'Yes':'cresidentus_yes','No':'cresidentus_no'})
        self.cresident   = Select(self,{'base':'cresident'})
        self.access      = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the cresidentus, cresident, and access values"""

        return {'cresidentus' : self.cresidentus.value(),
                'cresident'   : self.cresident.value(),
                'access'      : self.access.value()}


    def update(self,cresidentus=None,cresident=None,access=None):
        """update the cresidentus, cresident, and access values"""

        if cresidentus != None:
            self.cresidentus.value = cresidentus
        if cresident != None:
            self.cresident.value = cresident
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileResidence_Locators_Base(object):
    """locators for MembersProfileResidence object"""

    locators = {
        'base'              : "css=.profile-countryresident",
        'cresidentus_yes'   : "css=#cresident_usyes",
        'cresidentus_no'    : "css=#cresident_usno",
        'cresident'         : "css=#cresident",
        'access'            : "css=.profile-countryresident select[name='access[countryresident]']",
        'sectionkey'        : "css=.profile-countryresident .key",
        'sectionvalue'      : "css=.profile-countryresident .value",
        'open'              : "css=.profile-countryresident .edit-profile-section",
        'close'             : "css=.profile-countryresident .edit-profile-section",
        'save'              : "css=.profile-countryresident .section-edit-submit",
        'cancel'            : "css=.profile-countryresident .section-edit-cancel",
    }
