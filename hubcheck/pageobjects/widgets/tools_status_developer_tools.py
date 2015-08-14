from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class ToolsStatusDeveloperTools(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusDeveloperTools,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusDeveloperTools_Locators = self.load_class('ToolsStatusDeveloperTools_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusDeveloperTools_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.history    = Link(self,{'base':'history'})
        self.wiki       = Link(self,{'base':'wiki'})
        self.source     = Link(self,{'base':'source'})
        self.timeline   = Link(self,{'base':'timeline'})
        self.message    = Link(self,{'base':'message'})
        self.cancel     = Link(self,{'base':'cancel'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_history(self):

        self.history.click()


    def goto_wiki(self):

        self.wiki.click()


    def goto_source_code(self):

        self.source.click()


    def goto_timeline(self):

        self.timeline.click()


    def open_message(self):

        self.message.click()


    def cancel_tool(self):

        self.cancel.click()


class ToolsStatusDeveloperTools_Locators_Base(object):
    """locators for ToolsStatusDeveloperTools object"""

    locators = {
        'base'              : "css=#toolstatus",
        'history'           : "css=.history",
        'wiki'              : "css=.wiki",
        'source'            : "css=.sourcecode",
        'timeline'          : "css=.timeline",
        'message'           : "css=.message",
        'cancel'            : "css=.canceltool",
    }

