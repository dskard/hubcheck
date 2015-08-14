from hubcheck.pageobjects.po_generic_page import GenericPage

class MembersDashboardPage(GenericPage):
    """members profile page"""

    def __init__(self,browser,catalog,memberid='myaccount'):
        super(MembersDashboardPage,self).__init__(browser,catalog)
        self.memberid = memberid
        self.path = "/members/%s/dashboard" % (str(self.memberid))

        # load hub's classes
        MembersDashboardPage_Locators = self.load_class('MembersDashboardPage_Locators')
        MembersDashboardTable = self.load_class('MembersDashboardTable')
        MembersPageMenu = self.load_class('MembersPageMenu')

        # update this object's locator
        self.locators.update(MembersDashboardPage_Locators.locators)

        # setup page object's components
        self.modules = MembersDashboardTable(self,{'base':'modules'})
        self.menu = MembersPageMenu(self,{'base':'menu'})


class MembersDashboardPage_Locators_Base(object):
    """locators for MembersDashboardPage object"""

    locators = {
        'modules'   : "css=#droppables",
        'menu'      : "css=#page_menu",
    }
