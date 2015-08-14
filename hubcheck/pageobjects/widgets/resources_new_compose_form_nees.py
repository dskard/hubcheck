from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class ResourcesNewComposeFormNees(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewComposeFormNees,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewComposeFormNees_Locators = self.load_class('ResourcesNewComposeFormNees_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewComposeFormNees_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title          = Text(self,{'base':'title'})
        self.abstract       = IframeWrap(TextArea(self,{'base':'abstract'}),
                                ['abstractframe'])

        self.fields += ['title','abstract']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ResourcesNewComposeFormNees_Locators_Base(object):
    """locators for ResourcesNewComposeFormNees object"""

    locators = {
        'base'              : "css=#hubForm",
        'title'             : "css=#field-title",
#        'abstract'          : "css=#field-fulltxt",
        'abstract'          : "css=body",
        'submit'            : "css=[type='submit']",
        'abstractframe'     : "css=#cke_contents_field-fulltxt iframe",
    }
