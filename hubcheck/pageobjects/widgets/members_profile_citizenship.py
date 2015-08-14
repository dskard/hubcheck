from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileCitizenship(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileCitizenship,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileCitizenship_Locators = self.load_class('MembersProfileCitizenship_Locators')

        # update this object's locator
        self.locators.update(MembersProfileCitizenship_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.coriginus   = Radio(self,{'Yes':'coriginus_yes','No':'coriginus_no'})
        self.corigin     = Select(self,{'base':'corigin'})
        self.access      = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with the values of coriginus, corigin, and access"""

        return {'coriginus' : self.coriginus.value(),
                'corigin'   : self.corigin.value(),
                'access'    : self.access.value()}


    def update(self,coriginus=None,corigin=None,access=None):
        """update the values of coriginus, corigin, and access"""

        if coriginus != None:
            self.coriginus.value = coriginus
        if corigin != None:
            self.corigin.value = corigin
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileCitizenship_Locators_Base(object):
    """locators for MembersProfileCitizenship object"""

    locators = {
        'base'          : "css=.profile-countryorigin",
        'coriginus_yes' : "css=#corigin_usyes",
        'coriginus_no'  : "css=#corigin_usno",
        'corigin'       : "css=#corigin",
        'access'        : "css=.profile-countryorigin select[name='access[countryorigin]']",
        'sectionkey'    : "css=.profile-countryorigin .key",
        'sectionvalue'  : "css=.profile-countryorigin .value",
        'open'          : "css=.profile-countryorigin .edit-profile-section",
        'close'         : "css=.profile-countryorigin .edit-profile-section",
        'save'          : "css=.profile-countryorigin .section-edit-submit",
        'cancel'        : "css=.profile-countryorigin .section-edit-cancel",
    }
