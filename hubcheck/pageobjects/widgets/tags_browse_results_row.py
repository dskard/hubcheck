from hubcheck.pageobjects.widgets.item_list_item import ItemListItem
from hubcheck.pageobjects.basepageelement import TextReadOnly, Link

class TagsBrowseResultsRow1(ItemListItem):

    def __init__(self, owner, locatordict={}, row_number=0):

        super(TagsBrowseResultsRow1,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        TagsBrowseResultsRow_Locators = self.load_class('TagsBrowseResultsRow_Locators')

        # update this object's locator
        self.locators.update(TagsBrowseResultsRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name     = Link(self,{'base':'name'})
        self.count    = TextReadOnly(self,{'base':'count'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with the name and count properties of the tag"""

        return({'name':self.name.text(), 'count':int(self.count.value)})


    def goto_tag(self):
        """click the tag"""

        self.name.click()


class TagsBrowseResultsRow1_Locators_Base_1(object):
    """locators for TagsBrowseResultsRow1 object"""

    locators = {
        'base'           : "css=#taglist tbody tr:nth-of-type({row_num})",
        'name'           : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(1) a",
        'count'          : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
    }


class TagsBrowseResultsRow2(ItemListItem):
    """
       In HUBzero version 1.2, the row changed to provide
       the name and alias of the tagi
    """

    def __init__(self, owner, locatordict={}, row_number=0):

        super(TagsBrowseResultsRow2,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        TagsBrowseResultsRow_Locators = self.load_class('TagsBrowseResultsRow_Locators')

        # update this object's locator
        self.locators.update(TagsBrowseResultsRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name     = Link(self,{'base':'name'})
        self.alias    = TextReadOnly(self,{'base':'alias'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with the name and count properties of the tag"""

        return({'name':self.name.text(), 'alias':self.alias.value})


    def goto_tag(self):
        """click the tag"""

        self.name.click()


class TagsBrowseResultsRow2_Locators_Base_1(object):
    """locators for TagsBrowseResultsRow2 object"""

    locators = {
        'base'           : "css=#taglist tbody tr:nth-of-type({row_num})",
        'name'           : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(1) a",
        'alias'          : "css=#taglist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
    }
