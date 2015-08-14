from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

class ToolSessionSharedWithItem(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(ToolSessionSharedWithItem,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        ToolSessionSharedWithItem_Locators = \
            self.load_class('ToolSessionSharedWithItem_Locators')

        # update this object's locator
        self.locators.update(ToolSessionSharedWithItem_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name = Link(self,{'base':'name'})
        self.disconnect = Link(self,{'base':'disconnect'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of properties for this item"""

        properties = {
            'name'          : self.name.text(),
        }

        return properties


class ToolSessionSharedWithItem_Locators_Base(object):
    """locators for ToolSessionSharedWithItem object"""

    locators = {
        'base'       : "css=.entries tbody tr:nth-of-type({row_num})",
        'name'       : "css=.entries tbody tr:nth-of-type({row_num}) .entry-title",
        'disconnect' : "css=.entries tbody tr:nth-of-type({row_num}) .entry-remove",
    }
