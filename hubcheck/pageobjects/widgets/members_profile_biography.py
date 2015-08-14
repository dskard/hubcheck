from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileBiography(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileBiography,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileBiography_Locators = self.load_class('MembersProfileBiography_Locators')

        # update this object's locator
        self.locators.update(MembersProfileBiography_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.biography   = TextArea(self,{'base':'biography'})
        self.access      = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with the biography and access value settings"""

        return {'biography' : self.biography.value(),
                'access'    : self.access.value()}


    def update(self,biography=None,access=None):
        """update the biography and access settings"""

        if biography != None:
            self.biography.value = biography
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileBiography_Locators_Base(object):
    """locators for MembersProfileBiography object"""

    locators = {
        'base'          : "css=.profile-bio",
        'biography'     : "css=#profile_bio",
        'access'        : "css=.profile-bio select[name='access[bio]']",
        'sectionkey'    : "css=.profile-bio .key",
        'sectionvalue'  : "css=.profile-bio .value",
        'open'          : "css=.profile-bio .edit-profile-section",
        'close'         : "css=.profile-bio .edit-profile-section",
        'save'          : "css=.profile-bio .section-edit-submit",
        'cancel'        : "css=.profile-bio .section-edit-cancel",
    }
