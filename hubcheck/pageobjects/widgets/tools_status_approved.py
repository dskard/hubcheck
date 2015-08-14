from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusApproved(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusApproved,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusApproved_Locators = \
            self.load_class('ToolsStatusApproved_Locators')
        ToolsStatusWhatsNextApproved = \
            self.load_class('ToolsStatusWhatsNextApproved')

        # update this object's locator
        self.locators.update(ToolsStatusApproved_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextApproved(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_tool_page(self):

        return self.whatsnext.goto_tool_page()


    def get_tool_page_name(self):

        return self.whatsnext.get_tool_page_name()


    def get_time_since_request(self):

        return self.whatsnext.get_time_since_request()


class ToolsStatusApproved_Locators_Base(object):
    """locators for ToolsStatusApproved object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }

