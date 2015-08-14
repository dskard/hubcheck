from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

class GroupsInfo1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsInfo1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsInfo_Locators = self.load_class('GroupsInfo_Locators')

        # update this object's locator
        self.locators.update(GroupsInfo_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.privacy     = TextReadOnly(self,{'base':'privacy'})
        self.join_policy = TextReadOnly(self,{'base':'join_policy'})
        self.create_date = TextReadOnly(self,{'base':'create_date'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_privacy(self):
        """return the group privacy policy"""

        return self.privacy.value


    def get_join_policy(self):
        """return the group join policy"""

        return self.join_policy.value

    def get_create_date(self):
        """return the group create"""

        return self.create_date.value


class GroupsInfo1_Locators_Base(object):
    """locators for GroupsInfo1 object"""

    locators = {
        'base'              : "css=#page_info",
        'privacy'           : "css=.info-discoverability .value",
        'join_policy'       : "css=.info-join-policy .value",
        'create_date'       : "css=.info-created .value",
    }


class GroupsInfo2(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(GroupsInfo2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsInfo_Locators = self.load_class('GroupsInfo_Locators')
        TagsList            = self.load_class('TagsList')

        # update this object's locator
        self.locators = GroupsInfo_Locators.locators

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.managers        = TextReadOnly(self,{'base':'managers'})
        self.nmembers        = TextReadOnly(self,{'base':'nmembers'})
        self.privacy         = TextReadOnly(self,{'base':'privacy'})
        self.join_policy     = TextReadOnly(self,{'base':'join_policy'})
        self.create_date     = TextReadOnly(self,{'base':'create_date'})
        self.tags            = TagsList(self,{'base':'tags'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_managers(self):
        """return the group managers"""

        return self.managers.value


    def get_nmembers(self):
        """return the number of group members"""

        return self.nmembers.value


    def get_privacy(self):
        """return the group privacy policy"""

        return self.privacy.value


    def get_join_policy(self):
        """return the group join policy"""

        return self.join_policy.value


    def get_create_date(self):
        """return the group create date"""

        return self.create_date.value


    def get_tags(self):
        """return the group's tags"""

        return self.tags.get_tags()


    def click_tag(self,tagname):
        """click on a tag"""

        return self.tags.click_tag(tagname)


class GroupsInfo2_Locators_Base(object):
    """locators for GroupsInfo2 object"""

    locators = {
        'base'              : "css=.group-info-mod",
        'managers'          : "xpath=//span[text()='Managers']/../span[contains(@class,'value')]",
        'nmembers'          : "xpath=//span[text()='Members']/../span[contains(@class,'value')]",
        'privacy'           : "xpath=//span[text()='Discoverability']/../span[contains(@class,'value')]",
        'join_policy'       : "xpath=//span[text()='Policy']/../span[contains(@class,'value')]",
        'create_date'       : "xpath=//span[text()='Created']/../span[contains(@class,'value')]",
        'tags'              : "css=.group-info-mod .tags",
    }
