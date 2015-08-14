from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.members_profile_element import MembersProfileElement

class MembersProfileWebsite(MembersProfileElement):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileWebsite,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileWebsite_Locators = self.load_class('MembersProfileWebsite_Locators')

        # update this object's locator
        self.locators.update(MembersProfileWebsite_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.website        = Text(self,{'base':'website'})
        self.access         = Select(self,{'base':'access'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with website and access values"""

        return {'website' : self.website.value(),
                'access'  : self.access.value()}


    def update(self,website=None,access=None):
        """update the website and access values"""

        if website != None:
            self.website.value = website
        if access != None:
            self.access.value = access
        self.save.click()


class MembersProfileWebsite_Locators_Base(object):
    """locators for MembersProfileWebsite object"""

    locators = {
        'base'          : "css=.profile-web",
        'website'       : "css=#profile-url",
        'access'        : "css=.profile-web select[name='access[org]']",
        'sectionkey'    : "css=.profile-web .key",
        'sectionvalue'  : "css=.profile-web .value",
        'open'          : "css=.profile-web .edit-profile-section",
        'close'         : "css=.profile-web .edit-profile-section",
        'save'          : "css=.profile-web .section-edit-submit",
        'cancel'        : "css=.profile-web .section-edit-cancel",
    }
