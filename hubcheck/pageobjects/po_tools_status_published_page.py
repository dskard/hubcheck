from hubcheck.pageobjects.po_tools_status_base_page import ToolsStatusBasePage

class ToolsStatusPublishedPage(ToolsStatusBasePage):
    """tools pipeline status page for tool in approved state"""

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusPublishedPage,self).__init__(browser,catalog)
        self.path = "/tools/%s/status" % (toolname)

        # load hub's classes
        ToolsStatusPublishedPage_Locators = \
            self.load_class('ToolsStatusPublishedPage_Locators')
        ToolsStatusWhatsNextPublished = \
            self.load_class('ToolsStatusWhatsNextPublished')

        # update this object's locator
        self.locators.update(ToolsStatusPublishedPage_Locators.locators)

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextPublished(self)


    def goto_tool_page(self):

        return self.whatsnext.goto_tool_page()


    def get_tool_page_name(self):

        return self.whatsnext.get_tool_page_name()


    def flip_status_to_updated(self):

        return self.whatsnext.flip_status_to_updated()


class ToolsStatusPublishedPage_Locators_Base(object):
    """locators for ToolsStatusPublishedPage object"""

    locators = {
        'whatsnext'         : "css=#whatsnext",
        'admin_controls'    : "css=#adminCalls",
        'admin_form'        : "css=#adminForm",
    }


class ToolsStatusPublishedAdminPage(ToolsStatusPublishedPage):

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusPublishedAdminPage,self).__init__(browser,catalog,toolname)

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


class ContribtoolToolsStatusPublishedPage(ToolsStatusPublishedPage):

    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusPublishedPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)


class ContribtoolToolsStatusPublishedAdminPage(ToolsStatusPublishedAdminPage):

    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusPublishedAdminPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)
