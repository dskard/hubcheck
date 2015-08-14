from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text

class ToolsStatusApproveVersionForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusApproveVersionForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusApproveVersionForm_Locators = \
            self.load_class('ToolsStatusApproveVersionForm_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusApproveVersionForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.version  = Text(self,{'base':'version'})

        self.fields = ['version']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ToolsStatusApproveVersionForm_Locators_Base(object):
    """locators for ToolsStatusApproveVersionForm object"""

    locators = {
        'base'        : "css=#versionForm",
        'version'     : "css=#newversion",
        'submit'      : "css=#versionForm [type='submit']",
    }
