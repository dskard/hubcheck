from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import Button

class ResourcesToolTagsForm(FormBase):
    def __init__(self, owner, locatordict=None):
        super(ResourcesToolTagsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolTagsForm_Locators = self.load_class('ResourcesToolTagsForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolTagsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tags = TextAC(self,{'base':'tags',
                                 'aclocatorid':'tagsac',
                                 'choicelocatorid':'tagsacchoices',
                                 'tokenlocatorid':'tagsactoken',
                                 'deletelocatorid':'tagsacdelete'})

        self.top_previous   = Button(self,{'base':'top_previous'})
        self.top_submit     = Button(self,{'base':'top_submit'})
        self.previous       = Button(self,{'base':'previous'})

        self.fields = ['tags']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesToolTagsForm_Locators_Base(object):
    """locators for ResourcesToolTagsForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'top_previous'      : "css=#hubForm div:nth-of-type(1) .returntoedit",
        'top_submit'        : "css=#hubForm div:nth-of-type(1) [type='submit']",
        'previous'          : "css=#hubForm div:nth-of-type(6) .returntoedit",
        'submit'            : "css=#hubForm div:nth-of-type(6) [type='submit']",
    }
