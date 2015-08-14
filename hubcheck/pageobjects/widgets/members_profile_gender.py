from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileGender(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileGender,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileGender_Locators = self.load_class('MembersProfileGender_Locators')

        # update this object's locator
        self.locators.update(MembersProfileGender_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.gender = Select(self,{'base':'gender'})
        self.access = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with gender and access values"""

        return {'gender' : self.gender.value(),
                'access' : self.access.value()}


    def update(self,gender=None,access=None):
        """update the gender and access values"""

        if gender != None:
            self.gender.value = gender
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileGender_Locators_Base(object):
    """locators for MembersProfileGender object"""

    locators = {
        'base'          : "css=.profile-sex",
        'gender'        : "css=.profile-sex [name='sex']",
        'access'        : "css=.profile-sex select[name='access[gender]']",
        'sectionkey'    : "css=.profile-sex .key",
        'sectionvalue'  : "css=.profile-sex .value",
        'open'          : "css=.profile-sex .edit-profile-section",
        'close'         : "css=.profile-sex .edit-profile-section",
        'save'          : "css=.profile-sex .section-edit-submit",
        'cancel'        : "css=.profile-sex .section-edit-cancel",
    }
