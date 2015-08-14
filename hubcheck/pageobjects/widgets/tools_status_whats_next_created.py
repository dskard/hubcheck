from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsStatusWhatsNextCreated(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextCreated,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextCreated_Locators = self.load_class('ToolsStatusWhatsNextCreated_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextCreated_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.forge              = Link(self,{'base':'forge'})
        self.wiki               = Link(self,{'base':'wiki'})
        self.getting_started    = Link(self,{'base':'getting_started'})
        self.uploaded           = Link(self,{'base':'uploaded'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_forge(self):

        self.forge.click()


    def get_forge_name(self):

        return self.forge.text


    def goto_wiki(self):

        return self.wiki.click()


    def get_wiki_name(self):

        return self.wiki.text


    def goto_getting_started(self):

        return self.getting_started.click()


    def flip_status_to_uploaded(self):

        return self.uploaded.click()


class ToolsStatusWhatsNextCreated_Locators_Base(object):
    """locators for ToolsStatusWhatsNextCreated object"""

    locators = {
        'base'            : "css=#whatsnext",
        'forge'           : "css=#whatsnext p:nth-of-type(1) > a:nth-of-type(1)",
        'wiki'            : "css=#whatsnext p:nth-of-type(1) > a:nth-of-type(2)",
        'getting_started' : "css=#whatsnext ul:nth-of-type(1) .developer-wiki",
        'uploaded'        : "css=#Uploaded .flip",
    }

