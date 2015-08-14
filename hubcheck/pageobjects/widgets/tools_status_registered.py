from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusRegistered(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusRegistered,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusRegistered_Locators = self.load_class('ToolsStatusRegistered_Locators')
        ToolsStatusWhatsNextRegistered = self.load_class('ToolsStatusWhatsNextRegistered')

        # update this object's locator
        self.locators.update(ToolsStatusRegistered_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextRegistered(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_forge(self):

        return self.whatsnext.goto_forge()


    def get_forge_name(self):

        return self.whatsnext.get_forge_name()


    def get_time_since_request(self):

        return self.whatsnext.get_time_since_request()


class ToolsStatusRegistered_Locators_Base(object):
    """locators for ToolsStatusRegistered object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }
