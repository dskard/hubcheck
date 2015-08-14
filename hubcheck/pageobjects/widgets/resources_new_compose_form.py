from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class ResourcesNewComposeForm1(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewComposeForm1,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewComposeForm_Locators = self.load_class('ResourcesNewComposeForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewComposeForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title          = Text(self,{'base':'title'})
        self.abstract       = TextArea(self,{'base':'abstract'})

        self.fields += ['title','abstract']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ResourcesNewComposeForm1_Locators_Base(object):
    """locators for ResourcesNewComposeForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'title'             : "css=#field-title",
        'abstract'          : "css=#field-fulltxt",
        'submit'            : "css=#hubForm [type='submit']",
    }


class ResourcesNewComposeForm2(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewComposeForm2,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewComposeForm_Locators = self.load_class('ResourcesNewComposeForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewComposeForm_Locators.locators)

        # update the locators from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title          = Text(self,{'base':'title'})
        self.abstract       = IframeWrap(TextArea(self,{'base':'abstract'}),
                                ['abstractframe'])

        # there is a small bug in the IframeWrap that requires
        # you to be on the page before creating the object
        # I think it has to do with .value being a property
        # that is called when we are looking for the TextArea's attributes


        self.fields += ['title','abstract']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ResourcesNewComposeForm2_Locators_Base(object):
    """locators for ResourcesNewComposeForm2 object"""

    locators = {
        'base'              : "css=#hubForm",
        'title'             : "css=#field-title",
#        'abstract'          : "css=#field-fulltxt",
        'abstract'          : "css=body",
        'submit'            : "css=#hubForm [type='submit']",
        'abstractframe'     : "css=#cke_contents_field-fulltxt iframe",
    }
