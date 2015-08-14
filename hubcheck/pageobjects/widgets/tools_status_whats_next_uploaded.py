from hubcheck.pageobjects.basepagewidget import BasePageWidget

import re

class ToolsStatusWhatsNextUploaded(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusWhatsNextUploaded,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusWhatsNextUploaded_Locators = self.load_class('ToolsStatusWhatsNextUploaded_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusWhatsNextUploaded_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_time_since_request(self):

        pass


class ToolsStatusWhatsNextUploaded_Locators_Base(object):
    """locators for ToolsStatusWhatsNextUploaded object"""

    locators = {
        'base' : "css=#whatsnext",
    }

