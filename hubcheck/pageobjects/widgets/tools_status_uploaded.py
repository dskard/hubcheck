from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusUploaded(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusUploaded,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusUploaded_Locators = self.load_class('ToolsStatusUploaded_Locators')
        ToolsStatusWhatsNextUploaded = self.load_class('ToolsStatusWhatsNextUploaded')

        # update this object's locator
        self.locators.update(ToolsStatusUploaded_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextUploaded(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_time_since_request(self):

        return self.whatsnext.get_time_since_request()


class ToolsStatusUploaded_Locators_Base(object):
    """locators for ToolsStatusUploaded object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }
