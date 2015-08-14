from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

import re
import datetime

class AdminDatabaseListItem1(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(AdminDatabaseListItem1,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        AdminDatabaseListItem_Locators = \
            self.load_class('AdminDatabaseListItem_Locators')

        # update this object's locator
        self.locators.update(AdminDatabaseListItem_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name       = TextReadOnly(self,{'base':'name'})
        self.config     = Link(self,{'base':'config'})
        self.backups    = Link(self,{'base':'backups'})
        self.tables     = Link(self,{'base':'tables'})
        self.dataviews  = Link(self,{'base':'dataviews'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of properties for this row"""

        properties = {
            'name' : self.name.value,
        }

        return properties


    def goto_configuration(self):
        """navigate to the configuration page"""

        self.config.click()
        return


    def goto_backups(self):
        """navigate to the backups page"""

        self.backups.click()
        return


    def goto_table_list(self):
        """navigate to the table list page"""

        self.tables.click()
        return


    def goto_dataviews(self):
        """navigate to the dataviews page"""

        self.dataviews.click()
        return


class AdminDatabaseListItem1_Locators_Base_1(object):
    """locators for AdminDatabaseListItem1 object"""

    locators = {
        'base'      : "css=.adminlist tbody tr:nth-of-type({row_num})",
        'name'      : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
        'config'    : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(3) a",
        'backups'   : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(4) a",
        'tables'    : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(5) a",
        'dataviews' : "css=.adminlist tbody tr:nth-of-type({row_num}) td:nth-of-type(6) a",
    }
