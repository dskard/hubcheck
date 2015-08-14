from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly


class ToolsStatusBase(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusBase,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusBase_Locators = self.load_class('ToolsStatusBase_Locators')
        ToolsStatusToolInfo = self.load_class('ToolsStatusToolInfo')
        ToolsStatusRemainingSteps = self.load_class('ToolsStatusRemainingSteps')
        ToolsStatusDeveloperTools = self.load_class('ToolsStatusDeveloperTools')

        # update this object's locator
        self.locators.update(ToolsStatusBase_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.alltools       = Link(self,{'base':'alltools'})
        self.newtool        = Link(self,{'base':'alltools'})
        self.state          = TextReadOnly(self,{'base':'state'})
        self.info           = ToolsStatusToolInfo(self,{'base':'info'})
        self.remaining      = ToolsStatusRemainingSteps(self,{'base':'remaining'})
        self.system_message = TextReadOnly(self,{'base':'system_message'})
        self.devtools       = ToolsStatusDeveloperTools(self,{'base':'devtools'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_all_tools_page(self):

        self.alltools.click()


    def goto_new_tool_form(self):

        self.newtool.click()


    def get_tool_state(self):

        return self.state.value


    def get_todo_register_status(self):

        return self.remaining.get_register_status()


    def get_todo_upload_status(self):

        return self.remaining.get_upload_status()


    def get_todo_toolpage_status(self):

        return self.remaining.get_toolpage_status()


    def get_todo_test_approve_status(self):

        return self.remaining.get_test_approve_status()


    def get_todo_publish_status(self):

        return self.remaining.get_publish_status()


    def goto_todo_toolpage_create(self):

        return self.remaining.goto_toolpage_create()


    def goto_todo_toolpage_preview(self):

        return self.remaining.goto_toolpage_preview()


    def goto_todo_toolpage_edit(self):

        return self.remaining.goto_toolpage_edit()


    def goto_todo_upload_done(self):

        return self.remaining.goto_upload_done()


    def goto_todo_upload_howto(self):

        return self.remaining.goto_upload_howto()


    def goto_todo_approve_tool(self):

        return self.remaining.goto_approve_tool()


    def goto_todo_installed_update_tool(self):

        return self.remaining.goto_installed_update_tool()


    def goto_todo_approved_update_tool(self):

        return self.remaining.goto_approved_update_tool()


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

        if self.system_message.is_displayed():
            return self.system_message.value
        else:
            return None


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



class ToolsStatusBase_Locators_Base(object):
    """locators for ToolsStatusBase object"""

    locators = {
        'base'          : "css=#main",
        'alltools'      : "css=.main-page",
        'newtool'       : "css=.add",
        'state'         : "css=.state_hed",
        'info'          : "css=#toolstatus",
        'whatsnext'     : "css=#whatsnext",
        'remaining'     : "css=#whatsnext",
        'system_message' : "css=#system-message",
        'devtools'      : "css=.adminactions",
    }

