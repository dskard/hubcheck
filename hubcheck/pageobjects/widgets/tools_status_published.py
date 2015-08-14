from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusPublished(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusPublished,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusPublished_Locators = self.load_class('ToolsStatusPublished_Locators')
        ToolsStatusWhatsNextPublished = self.load_class('ToolsStatusWhatsNextPublished')

        # update this object's locator
        self.locators.update(ToolsStatusPublished_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextPublished(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_tool_page(self):

        return self.whatsnext.goto_tool_page()


    def get_tool_page_name(self):

        return self.whatsnext.get_tool_page_name()


    def flip_status_to_updated(self):

        return self.whatsnext.flip_status_to_updated()


class ToolsStatusPublished_Locators_Base(object):
    """locators for ToolsStatusPublished object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }

