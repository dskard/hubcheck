from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsStatusWhatsNextInstalled(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextInstalled,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextInstalled_Locators = self.load_class('ToolsStatusWhatsNextInstalled_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextInstalled_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.launch_tool         = Link(self,{'base':'launch_tool'})
        self.tool_page           = Link(self,{'base':'tool_page'})
        self.warning_create      = Link(self,{'base':'warning_create'})
        self.approved            = Link(self,{'base':'approved'})
        self.updated             = Link(self,{'base':'updated'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsNoToolPage(self,widgets=None,cltype='NoToolPage'):

        widgets = [self.launch_tool, self.tool_page,
                   self.warning_create, self.updated]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsToolPageExists(self,widgets=None,cltype='ToolPageExists'):

        widgets = [self.launch_tool, self.tool_page,
                   self.approved, self.updated]
        return self._checkLocators(widgets,cltype)


    def goto_launch_tool(self):

        self.launch_tool.click()


    def goto_tool_page(self):

        self.tool_page.click()


    def goto_warning_create(self):

        self.warning_create.click()


    def flip_status_to_approved(self):

        self.approved.click()


    def flip_status_to_updated(self):

        self.updated.click()


class ToolsStatusWhatsNextInstalled_Locators_Base(object):
    """locators for ToolsStatusWhatsNextInstalled object"""

    locators = {
        'base'              : "css=#whatsnext",
        'launch_tool'       : "css=#whatsnext .launchtool",
        'tool_page'         : "css=#whatsnext ul:nth-of-type(1) > li:nth-of-type(2) a",
        'warning_create'    : "css=#whatsnext .warning a",
        'approved'          : "css=#Approved a",
        'updated'           : "css=#Updated a",
    }

