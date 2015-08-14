from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

import re

class ToolsStatusWhatsNextRegistered(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextRegistered,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextRegistered_Locators = \
            self.load_class('ToolsStatusWhatsNextRegistered_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextRegistered_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.forge = Link(self,{'base':'forge'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_forge(self):

        self.forge.click()


    def get_forge_name(self):

        return self.forge.text


    def get_time_since_request(self):

        pass


class ToolsStatusWhatsNextRegistered_Locators_Base(object):
    """locators for ToolsStatusWhatsNextRegistered object"""

    locators = {
        'base'          : "css=#whatsnext",
        'forge'         : "css=#whatsnext p:nth-of-type(1) > a",
    }

