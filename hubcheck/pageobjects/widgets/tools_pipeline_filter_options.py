from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class ToolsPipelineFilterOptions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsPipelineFilterOptions,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsPipelineFilterOptions_Locators = self.load_class('ToolsPipelineFilterOptions_Locators')

        # update this object's locator
        self.locators.update(ToolsPipelineFilterOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.alltools       = Link(self,{'base':'alltools'})
        self.mine           = Link(self,{'base':'mine'})
        self.published      = Link(self,{'base':'published'})
        self.development    = Link(self,{'base':'development'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def filter_by_all(self):

        self.alltools.click()


    def filter_by_mine(self):

        self.mine.click()


    def filter_by_published(self):

        self.published.click()


    def filter_by_development(self):

        self.development.click()


class ToolsPipelineFilterOptions_Locators_Base(object):
    """locators for ToolsPipelineFilterOptions object"""

    locators = {
        'base'          : "css=.filter-options",
        'alltools'      : "css=a[title='All tools']",
        'mine'          : "css=a[title='My submissions']",
        'published'     : "css=a[title='Published tools']",
        'development'   : "css=a[title='Tools under development']",
    }

class ToolsPipelineFilterOptions_Locators_Base_2(object):
    """locators for ToolsPipelineFilterOptions object"""

    locators = {
        'base'          : "css=.filter-options",
        'alltools'      : "css=.filter-all",
        'mine'          : "css=.filter-mine",
        'published'     : "css=.filter-published",
        'development'   : "css=.filter-dev",
    }
