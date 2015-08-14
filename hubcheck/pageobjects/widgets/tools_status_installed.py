from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusInstalled(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusInstalled,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusInstalled_Locators = self.load_class('ToolsStatusInstalled_Locators')
        ToolsStatusWhatsNextInstalled = self.load_class('ToolsStatusWhatsNextInstalled')

        # update this object's locator
        self.locators.update(ToolsStatusInstalled_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextInstalled(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_launch_tool(self):

        return self.whatsnext.goto_launch_tool()


    def goto_tool_page(self):

        return self.whatsnext.goto_tool_page()


    def goto_warning_create(self):

        return self.whatsnext.goto_warning_create()


    def flip_status_to_approved(self):

        return self.whatsnext.flip_status_to_approved()


    def flip_status_to_updated(self):

        return self.whatsnext.flip_status_to_updated()


class ToolsStatusInstalled_Locators_Base(object):
    """locators for ToolsStatusInstalled object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }

