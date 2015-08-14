from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

import re

class ToolsStatusWhatsNextPublished(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextPublished,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextPublished_Locators = self.load_class('ToolsStatusWhatsNextPublished_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextPublished_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tool_page      = Link(self,{'base':'tool_page'})
        self.updated        = Link(self,{'base':'updated'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_tool_page(self):

        self.tool_page.click()


    def get_tool_page_name(self):

        return self.tool_page.text


    def flip_status_to_updated(self):

        self.updated.click()


class ToolsStatusWhatsNextPublished_Locators_Base(object):
    """locators for ToolsStatusWhatsNextPublished object"""

    locators = {
        'base'          : "css=#whatsnext",
        'tool_page'     : "css=#whatsnext p:nth-of-type(1) > a",
        'updated'       : "css=#Updated a",
    }

