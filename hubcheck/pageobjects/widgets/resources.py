from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Text

class Resources(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Resources,self).__init__(owner,locatordict)

        # load hub's classes
        Resources_Locators = self.load_class('Resources_Locators')
        ResourcesCategoryBrowser = self.load_class('ResourcesCategoryBrowser')

        # update this object's locator
        self.locators.update(Resources_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.create         = Link(self,{'base':'create'})
        self.faq            = Link(self,{'base':'faq'})
        self.search         = Text(self,{'base':'searchi'})
        self.submit         = Button(self,{'base':'searchb'})
        self.browse         = Link(self,{'base':'browse'})
        self.catbrowser     = ResourcesCategoryBrowser(self,{'base':'catbrowser'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_create(self):
        """click the resource create link"""

        self.create.click()


    def goto_faq(self):
        """click the resource faq link"""

        self.faq.click()


    def search_resources(self,searchtext):
        """perform a search on resources"""

        self.search.value = searchtext
        self.submit.click()


    def goto_browse_list(self):
        """click the browse resources link"""

        self.browse.click()


    def goto_category_by_browse(self,category):
        """click a category"""

        return self.catbrowser.goto_category_by_browse(category)


    def goto_category_by_title(self,category):
        """click a category title"""

        return self.catbrowser.goto_category_by_title(category)


    def get_category_titles(self):
        """return a list of category titles"""

        return self.catbrowser.get_category_titles()


    def get_category_classes(self):
        """return a list of category classes"""

        return self.catbrowser.get_category_classes()


class Resources_Locators_Base(object):
    """locators for Resources object"""

    locators = {
        'base'          : "css=#content",
        'create'        : "css=#getstarted a",
        'faq'           : "css=#introduction li:nth-of-type(1) a",
        'searchi'       : "css=#rsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.browse a",
        'catbrowser'    : "css=#content",
    }


class Resources_Locators_Base_2(object):
    """locators for Resources object as seen on old vhub"""

    locators = {
        'base'          : "css=#content",
        'create'        : "css=#introduction li:nth-of-type(2)",
        'faq'           : "css=#introduction li:nth-of-type(1)",
        'searchi'       : "css=#rsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.browse a",
        'catbrowser'    : "css=#content",
    }

