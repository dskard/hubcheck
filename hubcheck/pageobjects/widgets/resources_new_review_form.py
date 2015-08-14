from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Select

class ResourcesNewReviewForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewReviewForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewReviewForm_Locators = self.load_class('ResourcesNewReviewForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewReviewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.authorization  = Checkbox(self,{'base':'authorization'})
        self.license        = Select(self,{'base':'license'})
        self.preview        = TextReadOnly(self,{'base':'preview'})

        self.fields = ['authorization','license']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_license_types(self):
        """return the license types from the dropdown menu"""

        return self.license.options()


    def get_license_preview(self):
        """retrieve the license preview text"""

        return self.preview.value


class ResourcesNewReviewForm_Locators_Base(object):
    """locators for ResourcesNewReviewForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'authorization'     : "css=#authorization",
        'license'           : "css=#license",
        'preview'           : "css=#license-preview",
        'submit'            : "css=#hubForm [type='submit']",
    }
