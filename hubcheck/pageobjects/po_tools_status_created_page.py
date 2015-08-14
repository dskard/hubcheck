from hubcheck.pageobjects.po_tools_status_base_page import ToolsStatusBasePage

class ToolsStatusCreatedPage(ToolsStatusBasePage):
    """tools pipeline status page for tool in approved state"""

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusCreatedPage,self).__init__(browser,catalog)
        self.path = "/tools/%s/status" % (toolname)

        # load hub's classes
        ToolsStatusCreatedPage_Locators = \
            self.load_class('ToolsStatusCreatedPage_Locators')
        ToolsStatusWhatsNextCreated = \
            self.load_class('ToolsStatusWhatsNextCreated')
        ToolsStatusRemainingSteps = self.load_class('ToolsStatusRemainingSteps')

        # update this object's locator
        self.locators.update(ToolsStatusCreatedPage_Locators.locators)

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextCreated(self)
        self.remaining = ToolsStatusRemainingSteps(self, {
                            'register'     : 'rs_register',
                            'upload'       : 'rs_upload',
                            'upload_howto' : 'rs_upload_howto',
                            'toolpage'     : 'rs_toolpage',
                            'test_approve' : 'rs_test_approve',
                            'publish'      : 'rs_publish',
                            })


    def goto_forge(self):

        return self.whatsnext.goto_forge()


    def get_forge_name(self):

        return self.whatsnext.get_forge_name()


    def goto_wiki(self):

        return self.whatsnext.goto_wiki()


    def get_wiki_name(self):

        return self.whatsnext.get_wiki_name()


    def goto_getting_started(self):

        return self.whatsnext.goto_getting_started()


    def flip_status_to_uploaded(self):

        return self.whatsnext.flip_status_to_uploaded()


    def get_todo_register_status(self):

        return self.remaining.get_register_status()


    def get_todo_upload_status(self):

        return self.remaining.get_upload_status()


    def goto_todo_upload_done(self):

        return self.remaining.goto_upload_done()


    def goto_todo_upload_howto(self):

        return self.remaining.goto_upload_howto()


    def get_todo_toolpage_status(self):

        return self.remaining.get_toolpage_status()


    def goto_todo_toolpage_create(self):

        return self.remaining.goto_toolpage_create()


    def goto_todo_toolpage_preview(self):

        return self.remaining.goto_toolpage_preview()


    def goto_todo_toolpage_edit(self):

        return self.remaining.goto_toolpage_edit()


    def get_todo_test_approve_status(self):

        return self.remaining.get_test_approve_status()


    def get_todo_publish_status(self):

        return self.remaining.get_publish_status()



class ToolsStatusCreatedPage_Locators_Base(object):
    """locators for ToolsStatusCreatedPage object"""

    locators = {
        'whatsnext'         : "css=#whatsnext",
        'admin_controls'    : "css=#adminCalls",
        'admin_form'        : "css=#adminForm",
        'rs_register'       : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(1)",
        'rs_upload'         : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(2)",
        'rs_upload_howto'   : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(2) > a.developer-wiki",
        'rs_toolpage'       : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(3)",
        'rs_test_approve'   : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(4)",
        'rs_publish'        : "css=#whatsnext ul:nth-of-type(3) li:nth-of-type(5)",
    }


class ToolsStatusCreatedAdminPage(ToolsStatusCreatedPage):

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusCreatedAdminPage,self).__init__(browser,catalog,toolname)

        ToolsStatusAdministratorControls = self.load_class('ToolsStatusAdministratorControls')
        ToolsStatusAdministratorForm = self.load_class('ToolsStatusAdministratorForm')

        self.admin_controls = ToolsStatusAdministratorControls(self,{'base':'admin_controls'})
        self.admin_form = ToolsStatusAdministratorForm(self,{'base':'admin_form'})


    def do_addrepo(self):

        return self.admin_controls.do_addrepo()


    def do_install(self):

        return self.admin_controls.do_install()


    def do_publish(self):

        return self.admin_controls.do_publish()


    def do_retire(self):

        return self.admin_controls.do_retire()


    def populate_form(self, data):

        return self.admin_form.populate_form(data)


    def submit_form(self, data={}):

        return self.admin_form.submit_form(data)


class ContribtoolToolsStatusCreatedPage(ToolsStatusCreatedPage):

    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusCreatedPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)


class ContribtoolToolsStatusCreatedAdminPage(ToolsStatusCreatedAdminPage):

    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusCreatedAdminPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)
