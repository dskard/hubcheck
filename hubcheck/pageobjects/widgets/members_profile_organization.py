from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileOrganization(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileOrganization,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileOrganization_Locators = self.load_class('MembersProfileOrganization_Locators')

        # update this object's locator
        self.locators.update(MembersProfileOrganization_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.organization   = Select(self,{'base':'organization'})
        self.orgtext        = Text(self,{'base':'orgtext'})
        self.access         = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of the organization, orgtext, and access values"""

        return {'organization' : self.organization.value(),
                'orgtext'      : self.orgtext.value(),
                'access'       : self.access.value()}


    def update(self,organization=None,orgtext=None,access=None):
        """update the organization, orgtext, and access values"""

        if organization != None:
            self.organization.value = organization
        if orgtext != None:
            self.orgtext.value = orgtext
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileOrganization_Locators_Base(object):
    """locators for MembersProfileOrganization object"""

    locators = {
        'base'          : "css=.profile-org",
        'organization'  : "css=.profile-org [name='org']",
        'orgtext'       : "css=.profile-org [name='orgtext']",
        'access'        : "css=.profile-org select[name='access[org]']",
        'sectionkey'    : "css=.profile-org .key",
        'sectionvalue'  : "css=.profile-org .value",
        'open'          : "css=.profile-org .edit-profile-section",
        'close'         : "css=.profile-org .edit-profile-section",
        'save'          : "css=.profile-org .section-edit-submit",
        'cancel'        : "css=.profile-org .section-edit-cancel",
    }
