from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import TextAC

class ResourcesNewTagsForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewTagsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewTagsForm_Locators = self.load_class('ResourcesNewTagsForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewTagsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tags = TextAC(self,{'base':'tags',
                                 'aclocatorid':'tagsac',
                                 'choicelocatorid':'tagsacchoices',
                                 'tokenlocatorid':'tagsactoken',
                                 'deletelocatorid':'tagsacdelete'})

        self.fields = ['tags']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesNewTagsForm_Locators_Base(object):
    """locators for ResourcesNewTagsForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'submit'            : "css=#hubForm [type='submit']",
    }
