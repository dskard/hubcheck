from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button

class ResourcesToolFinalizeForm(FormBase):
    def __init__(self, owner, locatordict=None):
        super(ResourcesToolFinalizeForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolFinalizeForm_Locators = self.load_class('ResourcesToolFinalizeForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolFinalizeForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components

        self.previous       = Button(self,{'base':'previous'})

        self.fields = []

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesToolFinalizeForm_Locators_Base(object):
    """locators for ResourcesToolFinalizeForm object"""

    locators = {
        'base'      : "css=#hubForm",
        'previous'  : "css=#hubForm div:nth-of-type(1) .returntoedit",
        'submit'    : "css=#hubForm div:nth-of-type(1) [type='submit']",
    }
