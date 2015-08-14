from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

import re
import datetime

class AdminDatabaseTableListItem1(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(AdminDatabaseTableListItem1,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        AdminDatabaseTableListItem_Locators = \
            self.load_class('AdminDatabaseTableListItem_Locators')

        # update this object's locator
        self.locators.update(AdminDatabaseTableListItem_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name       = TextReadOnly(self,{'base':'name'})
        self.created    = TextReadOnly(self,{'base':'created'})
        self.updated    = TextReadOnly(self,{'base':'updated'})
        self.records    = TextReadOnly(self,{'base':'records'})
        self.schema     = Link(self,{'base':'schema'})
        self.view_data  = Link(self,{'base':'view_data'})
        self.manage_data = Link(self,{'base':'manage_data'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of properties for this row"""

        properties = {
            'name'      : self.name.value,
            'created'   : self.created.value,
            'updated'   : self.updated.value,
            'records'   : self.records.value,
        }

        return properties


    def goto_table_schema(self):
        """navigate to the table schema page for this item"""

        self.schema.click()
        return


    def goto_view_data(self):
        """navigate to the view data page for this item"""

        self.view_data.click()
        return


    def goto_manage_data(self):
        """navigate to the manage data page for this item"""

        self.manage_data.click()
        return


class AdminDatabaseTableListItem1_Locators_Base_1(object):
    """locators for AdminDatabaseTableListItem1 object"""

    locators = {
        'base'          : "css=.adminlist tbody tr:nth-of-type({row_num})",
        'name'          : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(1)",
        'created'       : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
        'updated'       : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(3)",
        'records'       : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(4)",
        'schema'        : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(5) a",
        'view_data'     : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(6) a",
        'manage_data'   : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(7) a",
    }
