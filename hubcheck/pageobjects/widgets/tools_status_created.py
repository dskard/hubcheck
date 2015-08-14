from hubcheck.pageobjects.widgets.tools_status_base import ToolsStatusBase

class ToolsStatusCreated(ToolsStatusBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusCreated,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusCreated_Locators = self.load_class('ToolsStatusCreated_Locators')
        ToolsStatusWhatsNextCreated = self.load_class('ToolsStatusWhatsNextCreated')

        # update this object's locator
        self.locators.update(ToolsStatusCreated_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.whatsnext = ToolsStatusWhatsNextCreated(self,{'base':'whatsnext'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_forge(self):

        return self.whatsnext.goto_forge()


    def get_forge_name(self):

        return self.whatsnext.get_forge_name()


    def goto_wiki(self):

        return self.whatsnext.goto_wiki()


    def get_wiki_name(self):

        return self.whatsnext.get_wiki_name()


    def goto_getting_started(self):

        return self.whatsnext.goto_getting_started()


    def flip_status_to_uploaded(self):

        return self.whatsnext.flip_status_to_uploaded()


class ToolsStatusCreated_Locators_Base(object):
    """locators for ToolsStatusCreated object"""

    locators = {
        'base'       : "css=#main",
        'whatsnext'  : "css=#whatsnext",
    }

