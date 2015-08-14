from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextArea

class ToolsStatusApproveLicenseForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusApproveLicenseForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusApproveLicenseForm_Locators = \
            self.load_class('ToolsStatusApproveLicenseForm_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusApproveLicenseForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.sourceaccess  = Select(self,{'base':'access'})
        self.templates = Select(self,{'base':'templates'})
        self.licensetext = TextArea(self,{'base':'license'})
        self.reason = TextArea(self,{'base':'reason'})
        self.authorize = Checkbox(self,{'base':'authorize'})

        self.fields = ['sourceaccess','templates','licensetext','reason','authorize']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ToolsStatusApproveLicenseForm_Locators_Base(object):
    """locators for ToolsStatusApproveLicenseForm object"""

    locators = {
        'base'        : "css=#licenseForm",
        'access'      : "css=#t_code",
        'templates'   : "css=#templates",
        'license'     : "css=#license",
        'reason'      : "css=#reason",
        'authorize'   : "css=#field-authorize",
        'submit'      : "css=#licenseForm [type='submit']",
    }
