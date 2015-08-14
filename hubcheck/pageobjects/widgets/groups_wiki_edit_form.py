from hubcheck.pageobjects.widgets.groups_wiki_new_form import \
    GroupsWikiNewForm1, GroupsWikiNewForm1_Locators_Base, \
    GroupsWikiNewForm2, GroupsWikiNewForm2_Locators_Base, \
    GroupsWikiNewForm3, GroupsWikiNewForm3_Locators_Base

from hubcheck.pageobjects.basepageelement import Link

class GroupsWikiEditForm1(GroupsWikiNewForm1):
    """
    GroupsWikiNewForm with TextArea widget for pagetext
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiEditForm1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiEditForm_Locators = self.load_class('GroupsWikiEditForm_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiEditForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.rename = Link(self,{'base':'rename'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_rename(self):
        """click the rename link"""

        self.rename.click()


class GroupsWikiEditForm1_Locators_Base(object):
    """locators for GroupsWikiEditForm1 object"""

    locators = {
        'rename'            : "xpath=//a[text()='here']",
    }


class GroupsWikiEditForm2(GroupsWikiNewForm2):
    """
    GroupsWikiEditForm that uses an IframeWrap widget for pagetext
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiEditForm2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiEditForm_Locators = self.load_class('GroupsWikiEditForm_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiEditForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.rename = Link(self,{'base':'rename'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_rename(self):
        """click the rename link"""

        self.rename.click()


class GroupsWikiEditForm2_Locators_Base(object):
    """locators for GroupsWikiEditForm2 object"""

    locators = {
        'rename'            : "xpath=//a[text()='here']",
    }


class GroupsWikiEditForm3(GroupsWikiNewForm3):
    """GroupsWikiEditForm

       TextArea widget for pagetext
       Upload3 file upload widget with embedded iframes
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiEditForm3,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiEditForm_Locators = self.load_class('GroupsWikiEditForm_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiEditForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.rename = Link(self,{'base':'rename'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_rename(self):
        """click the rename link"""

        self.rename.click()


class GroupsWikiEditForm3_Locators_Base(object):
    """locators for GroupsWikiEditForm3 object"""

    locators = {
        'rename'            : "xpath=//a[text()='here']",
    }


