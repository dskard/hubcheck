from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfilePassword(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfilePassword,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfilePassword_Locators = self.load_class('MembersProfilePassword_Locators')

        # update this object's locator
        self.locators.update(MembersProfilePassword_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.currentpassword    = Text(self,{'base':'currentpassword'})
        self.newpassword        = Text(self,{'base':'newpassword'})
        self.confirmpassword    = Text(self,{'base':'confirmpassword'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of currentpassword, newpassword, confirmpassword"""

        return {'currentpassword' : self.currentpassword.value(),
                'newpassword'     : self.newpassword.value(),
                'confirmpassword' : self.confirmpassword.value()}


    def update(self,currentpassword=None,newpassword=None,confirmpassword=None):
        """update the currentpassword, newpassword, and confirmpassword values"""

        if currentpassword != None:
            self.currentpassword.value = currentpassword
        if newpassword != None:
            self.newpassword.value = newpassword
        if confirmpassword != None:
            self.confirmpassword.value = confirmpassword
        self.save.click()


class MembersProfilePassword_Locators_Base(object):
    """locators for MembersProfilePassword object"""

    locators = {
        'base'              : "css=.profile-password",
        'currentpassword'   : "css=#password",
        'newpassword'       : "css=#newpass",
        'confirmpassword'   : "css=#newpass2",
        'sectionkey'        : "css=.profile-password .key",
        'sectionvalue'      : "css=.profile-password .value",
        'open'              : "css=.profile-password .edit-profile-section",
        'close'             : "css=.profile-password .edit-profile-section",
        'save'              : "css=.profile-password .section-edit-submit",
        'cancel'            : "css=.profile-password .section-edit-cancel",
    }
