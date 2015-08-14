from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Text

class TextSearchBox(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TextSearchBox,self).__init__(owner,locatordict)

        # load hub's classes
        TextSearchBox_Locators = self.load_class('TextSearchBox_Locators')

        # update this object's locator
        self.locators.update(TextSearchBox_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.text           = Text(self,{'base':'text'})
        self.submit         = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def search_for(self,keyword):
        """search for a resource by keyword"""

        self.text.value = keyword
        self.submit.click()


class TextSearchBox_Locators_Base(object):
    """locators for TextSearchBox object"""

    locators = {
        'base'          : "css=.form",
        'text'          : "css=.entry-search-field",
        'submit'        : "css=.entry-search-submit",
    }
