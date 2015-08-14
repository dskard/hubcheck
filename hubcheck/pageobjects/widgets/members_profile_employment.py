from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileEmployment(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileEmployment,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileEmployment_Locators = self.load_class('MembersProfileEmployment_Locators')

        # update this object's locator
        self.locators.update(MembersProfileEmployment_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.employment = Select(self,{'base':'employment'})
        self.access     = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with employment and access values"""

        return {'employment' : self.employment.value(),
                'access' : self.access.value()}


    def update(self,employment=None,access=None):
        """update the employment and access values"""

        if employment != None:
            self.employment.value = employment
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileEmployment_Locators_Base(object):
    """locators for MembersProfileEmployment object"""

    locators = {
        'base'          : "css=.profile-orgtype",
        'employment'    : "css=.profile-orgtype [name='orgtype']",
        'access'        : "css=.profile-orgtype select[name='access[orgtype]']",
        'sectionkey'    : "css=.profile-orgtype .key",
        'sectionvalue'  : "css=.profile-orgtype .value",
        'open'          : "css=.profile-orgtype .edit-profile-section",
        'close'         : "css=.profile-orgtype .edit-profile-section",
        'save'          : "css=.profile-orgtype .section-edit-submit",
        'cancel'        : "css=.profile-orgtype .section-edit-cancel",
    }
