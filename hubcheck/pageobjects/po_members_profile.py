from hubcheck.pageobjects.po_generic_page import GenericPage

class MembersProfilePage(GenericPage):
    """members profile page"""

    def __init__(self,browser,catalog,memberid='myaccount'):
        super(MembersProfilePage,self).__init__(browser,catalog)
        self.memberid = memberid
        self.path = "/members/%s/profile" % (str(self.memberid))

        # load hub's classes
        MembersProfilePage_Locators = self.load_class('MembersProfilePage_Locators')
        MembersProfileForm          = self.load_class('MembersProfileForm')
        MembersPageMenu             = self.load_class('MembersPageMenu')

        # update this object's locator
        self.locators.update(MembersProfilePage_Locators.locators)

        # setup page object's components
        self.form = MembersProfileForm(self,{'base':'form'})
        self.menu = MembersPageMenu(self,{'base':'menu'})


class MembersProfilePage_Locators_Base(object):
    """locators for MembersProfilePage object"""

    locators = {
        'form' : "css=#profile",
        'menu' : "css=#page_menu",
    }
