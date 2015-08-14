from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextAC

class ResourcesNewAuthorsAuthorsForm(FormBase):
    def __init__(self, owner, locatordict=None):
        super(ResourcesNewAuthorsAuthorsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewAuthorsAuthorsForm_Locators = \
            self.load_class('ResourcesNewAuthorsAuthorsForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewAuthorsAuthorsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.author   = TextAC(self,{'base':'author',
                                     'aclocatorid':'authorac',
                                     'choicelocatorid':'authoracchoices',
                                     'tokenlocatorid':'authoractoken',
                                     'deletelocatorid':'authoracdelete'})
        self.role     = Select(self,{'base':'role'})

        self.fields += ['author','role']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ResourcesNewAuthorsAuthorsForm_Locators_Base(object):
    """locators for ResourcesNewAuthorsAuthorsForm object"""

    locators = {
        'base'              : "css=#authors-form",
        'author'            : "css=#acmembers",
        'authorac'          : "css=#token-input-acmembers",
        'authoracchoices'   : "css=.token-input-dropdown-acm",
        'authoractoken'     : "css=.token-input-token-acm",
        'authoracdelete'    : "css=.token-input-delete-token-acm",
        'role'              : "css=#new-authors-role",
        'submit'            : "css=#authors-form [type='submit']",
    }
