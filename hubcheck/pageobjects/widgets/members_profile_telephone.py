from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileTelephone(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileTelephone,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileTelephone_Locators = self.load_class('MembersProfileTelephone_Locators')

        # update this object's locator
        self.locators.update(MembersProfileTelephone_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.telephone   = Text(self,{'base':'telephone'})
        self.access      = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of telephone and access values"""

        return {'telephone' : self.telephone.value(),
                'access'    : self.access.value()}


    def update(self,telephone=None,access=None):
        """update the telephone and access values"""

        if telephone != None:
            self.telephone.value = telephone
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileTelephone_Locators_Base(object):
    """locators for MembersProfileTelephone object"""

    locators = {
        'base'          : "css=.profile-phone",
        'telephone'     : "css=#profile-phone",
        'access'        : "css=.profile-phone select[name='access[phone]']",
        'sectionkey'    : "css=.profile-phone .key",
        'sectionvalue'  : "css=.profile-phone .value",
        'open'          : "css=.profile-phone .edit-profile-section",
        'close'         : "css=.profile-phone .edit-profile-section",
        'save'          : "css=.profile-phone .section-edit-submit",
        'cancel'        : "css=.profile-phone .section-edit-cancel",
    }
