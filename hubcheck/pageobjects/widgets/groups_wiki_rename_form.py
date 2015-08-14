from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Text

class GroupsWikiRenameForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsWikiRenameForm,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiRenameForm_Locators = self.load_class('GroupsWikiRenameForm_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiRenameForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.newpagename    = Text(self,{'base':'newpagename'})
        self.submit         = Button(self,{'base':'submit'})

        self.fields += ['newpagename']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def rename_page(self,name):
        """rename the group wiki page with name"""

        self.submit_form(data={'newpagename':name})


class GroupsWikiRenameForm_Locators_Base(object):
    """locators for GroupsWikiRenameForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'newpagename'       : "css=#hubForm [name='newpagename']",
        'submit'            : "css=#hubForm [type='submit']",
    }

