from hubcheck.pageobjects.po_tools_status_base_page import ToolsStatusBasePage

class ToolsStatusApprovedPage(ToolsStatusBasePage):
    """tools pipeline status page for tool in approved state"""

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusApprovedPage,self).__init__(browser,catalog)
        self.path = "/tools/%s/status" % (toolname)

        # load hub's classes
        ToolsStatusApprovedPage_Locators = \
            self.load_class('ToolsStatusApprovedPage_Locators')
        ToolsStatusWhatsNextApproved = \
            self.load_class('ToolsStatusWhatsNextApproved')
        ToolsStatusRemainingSteps = self.load_class('ToolsStatusRemainingSteps')


        # update this object's locator
        self.locators.update(ToolsStatusApprovedPage_Locators.locators)

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextApproved(self)
        self.remaining = ToolsStatusRemainingSteps(self)


    def goto_tool_page(self):

        return self.whatsnext.goto_tool_page()


    def get_tool_page_name(self):

        return self.whatsnext.get_tool_page_name()


    def get_time_since_request(self):

        return self.whatsnext.get_time_since_request()


    def get_todo_register_status(self):

        return self.remaining.get_register_status()


    def get_todo_upload_status(self):

        return self.remaining.get_upload_status()


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


    def goto_todo_update_tool(self):

        return self.remaining.goto_approved_update_tool()



class ToolsStatusApprovedPage_Locators_Base(object):
    """locators for ToolsStatusApprovedPage object"""

    locators = {
        'whatsnext'         : "css=#whatsnext",
        'admin_controls'    : "css=#adminCalls",
        'admin_form'        : "css=#adminForm",
    }


class ToolsStatusApprovedAdminPage(ToolsStatusApprovedPage):
    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusApprovedAdminPage,self).__init__(browser,catalog,toolname)

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


class ContribtoolToolsStatusApprovedPage(ToolsStatusApprovedPage):
    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusApprovedPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)


class ContribtoolToolsStatusApprovedAdminPage(ToolsStatusApprovedAdminPage):
    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusApprovedAdminPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)
