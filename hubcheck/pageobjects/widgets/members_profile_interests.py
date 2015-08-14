from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileInterests(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileInterests,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileInterests_Locators = self.load_class('MembersProfileInterests_Locators')

        # update this object's locator
        self.locators.update(MembersProfileInterests_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.interests   = TextAC(self,{'base':'interests',
                                        'aclocatorid':'interestsac',
                                        'choicelocatorid':'interestsacchoices',
                                        'tokenlocatorid':'interestsactoken',
                                        'deletelocatorid':'interestsacdelete'})
        self.access      = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the interests and access values"""

        return {'interests' : self.interests.value(),
                'access'    : self.access.value()}


    def update(self,interests=None,access=None):
        """update the value of the interests and access values"""

        if interests != None:
            self.interests.value = interests
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileInterests_Locators_Base(object):
    """locators for MembersProfileInterests object"""

    locators = {
        'base'               : "css=.profile-interests",
        'interests'          : "css=#actags",
        'interestsac'        : "css=#token-input-actags",
        'interestsacchoices' : "css=.profile-interests .token-input-dropdown-act",
        'interestsactoken'   : "css=.profile-interests .token-input-token-act",
        'interestsacdelete'  : "css=.profile-interests .token-input-delete-token-act",
        'access'             : "css=.profile-interests select[name='access[tags]']",
        'sectionkey'         : "css=.profile-interests .key",
        'sectionvalue'       : "css=.profile-interests .value",
        'open'               : "css=.profile-interests .edit-profile-section",
        'close'              : "css=.profile-interests .edit-profile-section",
        'save'               : "css=.profile-interests .section-edit-submit",
        'cancel'             : "css=.profile-interests .section-edit-cancel",
    }
