from hubcheck.pageobjects.po_generic_page import GenericPage

class MembersChangePasswordPage(GenericPage):
    """members change password page"""

    def __init__(self,browser,catalog,memberid='myaccount'):
        super(MembersChangePasswordPage,self).__init__(browser,catalog)
        self.memberid = memberid
        self.path = "/members/%s/changepassword" % (str(self.memberid))

        # load hub's classes
        MembersChangePasswordPage_Locators = self.load_class('MembersChangePasswordPage_Locators')
        MembersChangePasswordForm          = self.load_class('MembersChangePasswordForm')

        # update this object's locator
        self.locators.update(MembersChangePasswordPage_Locators.locators)

        # setup page object's components
        self.form = MembersChangePasswordForm(self,{'base':'form'})

    def change_password(self,current_password,new_password,confirm_password):
        data = {
            'currentpassword' : current_password,
            'newpassword'     : new_password,
            'confirmpassword' : confirm_password,
        }
        self.set_page_load_marker()
        out = self.form.submit_form(data)
        self.wait_for_page_to_load()
        return out


class MembersChangePasswordPage_Locators_Base(object):
    """locators for MembersChangePasswordPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
