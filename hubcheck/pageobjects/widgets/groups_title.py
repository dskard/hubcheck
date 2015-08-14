from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class GroupsTitle1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsTitle1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsTitle_Locators = self.load_class('GroupsTitle_Locators')

        # update this object's locator
        self.locators.update(GroupsTitle_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = TextReadOnly(self,{'base':'title'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def get_title(self):
        """return the title of the group"""

        return self.title.value

class GroupsTitle2(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsTitle2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsTitle_Locators = self.load_class('GroupsTitle_Locators')

        # update this object's locator
        self.locators.update(GroupsTitle_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = Link(self,{'base':'title'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def get_title(self):
        """return the title of the group"""

        return self.title.text()

    def goto_title(self):
        """click the group title link"""

        return self.title.click()

class GroupsTitle_Locators_Base_1(object):
    """locators for GroupsTitle1 object"""

    locators = {
        'base'              : "css=#page_header",
        'title'             : "css=#page_header h2",
    }

class GroupsTitle_Locators_Base_2(object):
    """locators for GroupsTitle2 object"""

    locators = {
        'base'              : "css=#page_header",
        'title'             : "css=#page_header h2 a",
    }

