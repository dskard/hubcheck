from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.exceptions import NoSuchMemberException

class GroupsMemberBrowser(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsMemberBrowser,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsMemberBrowser_Locators = self.load_class('GroupsMemberBrowser_Locators')

        # update this object's locator default
        self.locators.update(GroupsMemberBrowser_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.memberlink     = Link(self,{'base':'memberlink'})
        self.membername     = TextReadOnly(self,{'base':'membername'})
        self.memberorg      = TextReadOnly(self,{'base':'memberorg'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_member_names(self):
        """get group members names"""

        membernames = []
        memberElements = self.find_elements(self.locators['membername'])
        for e in memberElements:
            membernames.append(e.text)
        return membernames


    def goto_member_profile(self,membername):
        """navigate to a group member's profile"""

        memberElements = self.find_elements(self.locators['membername'])
        for e in memberElements:
            if e.text == membername:
                e.click()
                break
        else:
            raise NoSuchMemberException("member \"%s\" is not displayed" % (membername))


class GroupsMemberBrowser_Locators_Base(object):
    """locators for GroupsMemberBrowser object"""

    locators = {
        'base'              : "css=#member_browser",
        'memberlink'        : "css=#member_browser a",
        'membername'        : "css=#member_browser .member",
        'memberorg'         : "css=#member_browser .org",
    }
