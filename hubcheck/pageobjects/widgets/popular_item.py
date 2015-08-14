from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly, Link

class PopularItem(BasePageWidget):

    def __init__(self, owner, locatordict={}, item_number=0):

        # initialize variables
        self.__item_number = item_number

        super(PopularItem,self).__init__(owner,locatordict)

        # load hub's classes
        object_locators = self.load_class('PopularItem_Locators')

        # update this object's locator
        self.locators.update(object_locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = Link(self,{'base':'title'})
        self.description = TextReadOnly(self,{'base':'description'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def _updateLocators(self):

        super(PopularItem,self)._updateLocators()
        for k,v in self.locators.items():
            self.locators[k] = v % self.__item_number
        self.update_locators_in_widgets()


    def value(self):
        """return a dictionary with the properties of the group"""

        return({'title':self.title.text(),'description':self.description.value})


    def goto_group(self):
        """click the group title"""

        self.title.click()


class PopularItem_Locators_Base(object):
    """locators for PopularItem object"""

    locators = {
        'base'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]",
        'title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }
