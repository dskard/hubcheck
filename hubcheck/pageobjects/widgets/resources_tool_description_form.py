from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Button

class ResourcesToolDescriptionForm1(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ResourcesToolDescriptionForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolDescriptionForm_Locators = self.load_class('ResourcesToolDescriptionForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolDescriptionForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = Text(self,{'base':'title'})
        self.description = Text(self,{'base':'description'})
        self.abstract = Text(self,{'base':'abstract'})
        self.top_submit = Button(self,{'base':'top_submit'})

        self.fields = ['title','description','abstract']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesToolDescriptionForm1_Locators_Base_1(object):
    """locators for ResourcesToolDescriptionForm object"""

    locators = {
        'base'          : "css=#hubForm",
        'title'         : "css=#field-title",
        'description'   : "css=#field-description",
        'abstract'      : "css=#field-fulltxt",
        'top_submit'    : "css=#hubForm div:nth-of-type(1) [type='submit']",
        'submit'        : "css=#hubForm div:nth-of-type(7) [type='submit']",
    }


class ResourcesToolDescriptionForm2(FormBase):
    """
    ResourcesToolDescriptionForm2 that embeds the abstract inside of an iframe
    """

    def __init__(self, owner, locatordict={}):
        super(ResourcesToolDescriptionForm2,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolDescriptionForm_Locators = self.load_class(
            'ResourcesToolDescriptionForm_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolDescriptionForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = Text(self,{'base':'title'})
        self.description = Text(self,{'base':'description'})
        self.abstract = IframeWrap(Text(self,{'base':'abstract'}),
                                   ['abstractframe'])
        self.top_submit = Button(self,{'base':'top_submit'})

        self.fields = ['title','description','abstract']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesToolDescriptionForm2_Locators_Base_1(object):
    """locators for ResourcesToolDescriptionForm object"""

    locators = {
        'base'          : "css=#hubForm",
        'title'         : "css=#field-title",
        'description'   : "css=#field-description",
        'abstract'      : "css=body",
        'abstractframe' : "css=label[for='field-fulltxt'] iframe",
        'top_submit'    : "css=#hubForm div:nth-of-type(1) [type='submit']",
        'submit'        : "css=#hubForm div:nth-of-type(7) [type='submit']",
    }
