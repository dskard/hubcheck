from hubcheck.pageobjects.po_generic_page import GenericPage

from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsStatusBasePage(GenericPage):
    """tools pipeline status page for tool in registered state"""

    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusBasePage,self).__init__(browser,catalog)
        self.path = "/tools/%s/status" % (toolname)

        # load hub's classes
        ToolsStatusBasePage_Locators = \
            self.load_class('ToolsStatusBasePage_Locators')
        ToolsStatusToolInfo = self.load_class('ToolsStatusToolInfo')
        ToolsStatusRemainingSteps = self.load_class('ToolsStatusRemainingSteps')
        ToolsStatusDeveloperTools = self.load_class('ToolsStatusDeveloperTools')

        # update this object's locator
        self.locators.update(ToolsStatusBasePage_Locators.locators)

        # setup page object's components
        self.alltools       = Link(self,{'base':'alltools'})
        self.newtool        = Link(self,{'base':'newtool'})
        self.toolstate      = TextReadOnly(self,{'base':'state'})
        self.info           = ToolsStatusToolInfo(self,{'base':'info'})
        self.system_message = TextReadOnly(self,{'base':'system_message'})
        self.devtools       = ToolsStatusDeveloperTools(self,{'base':'devtools'})


    def goto_all_tools_page(self):

        return self.alltools.click()


    def goto_new_tool_form(self):

        return self.newtool.click()


    def get_tool_state(self):

        return self.toolstate.value


    def goto_toolinfo_edit(self):

        return self.info.goto_edit()


    def get_toolinfo_title(self):

        return self.info.get_title()


    def get_toolinfo_version(self):

        return self.info.get_version()


    def get_toolinfo_glance(self):

        return self.info.get_glance()


    def goto_toolinfo_toolpage_preview(self):

        return self.info.goto_toolpage_preview()


    def goto_toolinfo_toolpage_edit(self):

        return self.info.goto_toolpage_edit()


    def get_toolinfo_vncgeometry(self):

        return self.info.get_vncgeometry()


    def get_toolinfo_toolaccess(self):

        return self.info.get_toolaccess()


    def get_toolinfo_codeaccess(self):

        return self.info.get_codeaccess()


    def get_toolinfo_wikiaccess(self):

        return self.info.get_wikiaccess()


    def get_toolinfo_devteam(self):

        return self.info.get_devteam()


    def get_system_message(self):

        return self.system_message.value


    def goto_tooldev_history(self):

        return self.devtools.goto_history()


    def goto_tooldev_wiki(self):

        return self.devtools.goto_wiki()


    def goto_tooldev_source_code(self):

        return self.devtools.goto_source_code()


    def goto_tooldev_timeline(self):

        return self.devtools.goto_timeline()


    def open_tooldev_message(self):

        return self.devtools.open_message()


    def cancel_tool(self):

        return self.devtools.cancel_tool()


class ToolsStatusBasePage_Locators_Base(object):
    """locators for ToolsStatusBasePage object"""

    locators = {
        'admin_controls'    : "css=#adminCalls",
        'admin_form'        : "css=#adminForm",
        'alltools'          : "css=.main-page",
        'newtool'           : "css=.add",
        'state'             : "css=.state_hed",
        'info'              : "css=#toolstatus",
        'whatsnext'         : "css=#whatsnext",
        'remaining'         : "css=#whatsnext",
        'system_message'    : "css=#system-message",
        'devtools'          : "css=.adminactions",
    }



class ToolsStatusBaseAdminPage(ToolsStatusBasePage):
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


class ContribtoolToolsStatusBasePage(ToolsStatusBasePage):
    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusBasePage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)


class ContribtoolToolsStatusBaseAdminPage(ToolsStatusBaseAdminPage):
    def __init__(self,browser,catalog,toolid=''):
        super(ContribtoolToolsStatusApprovedAdminPage,self).__init__(browser,catalog)
        self.path = "/contribtool/status/%d" % (toolid)
