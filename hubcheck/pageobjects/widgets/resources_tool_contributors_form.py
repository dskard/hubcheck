from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class ResourcesToolContributorsForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ResourcesToolContributorsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolContributorsForm_Locators = self.load_class('ResourcesToolContributorsForm_Locators')
        ResourcesNewAuthorsAuthorsForm = self.load_class('ResourcesNewAuthorsAuthorsForm')
        ResourcesNewAuthorsAuthorsList = self.load_class('ResourcesNewAuthorsAuthorsList')
        # update this object's locator
        self.locators.update(ResourcesToolContributorsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.top_previous = Button(self,{'base':'top-previous'})
        self.top_submit = Button(self,{'base':'top-submit'})
        self.authorform = IframeWrap(
                            ResourcesNewAuthorsAuthorsForm(
                                self, {'base':'authorsform'}),
                            ['authorsframe'])
        self.authorlist = IframeWrap(
                            ResourcesNewAuthorsAuthorsList(
                                self, {'base':'authorslist'}),
                            ['authorsframe'])
        self.previous = Button(self,{'base':'previous'})
        self.submit = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


class ResourcesToolContributorsForm_Locators_Base(object):
    """locators for ResourcesToolContributorsForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'top-previous'      : "css=#hubForm div:nth-of-type(1) .returntoedit",
        'top-submit'        : "css=#hubForm div:nth-of-type(1) [type='submit']",
        'authorsform'       : "css=#authors-form",
        'authorslist'       : "css=#authors-list",
        'authorsframe'      : "css=#authors",
        'previous'          : "css=#hubForm div:nth-of-type(6) .returntoedit",
        'submit'            : "css=#hubForm div:nth-of-type(6) [type='submit']",
    }
