from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class TagsBrowseOrderOptions(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(TagsBrowseOrderOptions,self).__init__(owner,locatordict)

        # load hub's classes
        TagsBrowseOrderOptions_Locators = self.load_class('TagsBrowseOrderOptions_Locators')

        # update this object's locator
        self.locators.update(TagsBrowseOrderOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.alphabetically = Link(self,{'base':'alphabetically'})
        self.popular        = Link(self,{'base':'popular'})

        self.fields = ['alphabetically','popular']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def select(self,option):

        if not option in self.fields:
            raise ValueError("invalid button: %s" % (option))
        link = getattr(self,option)
        link.click()


class TagsBrowseOrderOptions_Locators_Base(object):
    """locators for TagsBrowseOrderOptions object"""

    locators = {
        'base'          : "css=.entries-menu",
        'alphabetically': "css=.entries-menu li:nth-child(2) a",
        'popular'       : "css=.entries-menu li:nth-child(1) a",
    }
