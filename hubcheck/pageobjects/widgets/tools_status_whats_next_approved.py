from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsStatusWhatsNextApproved(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextApproved,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextApproved_Locators = self.load_class('ToolsStatusWhatsNextApproved_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextApproved_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tool_page = Link(self,{'base':'tool_page'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_tool_page(self):

        self.tool_page.click()


    def get_tool_page_name(self):

        return self.tool_page.text


    def get_time_since_request(self):

        pass


class ToolsStatusWhatsNextApproved_Locators_Base(object):
    """locators for ToolsStatusWhatsNextApproved object"""

    locators = {
        'base'          : "css=#whatsnext",
        'tool_page'     : "css=#whatsnext p:nth-of-type(2) > a",
    }

