from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileName(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileName,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileName_Locators = self.load_class('MembersProfileName_Locators')

        # update this object's locator
        self.locators.update(MembersProfileName_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.firstname      = Text(self,{'base':'firstname'})
        self.middlename     = Text(self,{'base':'middlename'})
        self.lastname       = Text(self,{'base':'lastname'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the firstname, middlename, and lastname values"""

        return {'firstname'  : self.firstname.value(),
                'middlename' : self.middlename.value(),
                'lastname'   : self.lastname.value()}


    def update(self,firstname=None,middlename=None,lastname=None):
        """update the firstname, middlename, and lastname values"""

        if firstname != None:
            self.firstname.value = firstname
        if middlename != None:
            self.middlename.value = middlename
        if lastname != None:
            self.lastname.value = lastname
        self.save.click()


class MembersProfileName_Locators_Base(object):
    """locators for MembersProfileName object"""

    locators = {
        'base'          : "css=.profile-name",
        'firstname'     : "css=.profile-name input[name='name[first]']",
        'middlename'    : "css=.profile-name input[name='name[middle]']",
        'lastname'      : "css=.profile-name input[name='name[last]']",
        'sectionkey'    : "css=.profile-name .key",
        'sectionvalue'  : "css=.profile-name .value",
        'open'          : "css=.profile-name .edit-profile-section",
        'close'         : "css=.profile-name .edit-profile-section",
        'save'          : "css=.profile-name .section-edit-submit",
        'cancel'        : "css=.profile-name .section-edit-cancel",
    }
