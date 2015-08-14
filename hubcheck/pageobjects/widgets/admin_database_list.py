from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Link

class AdminDatabaseList1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminDatabaseList1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminDatabaseList_Locators = self.load_class('AdminDatabaseList_Locators')
        AdminDatabaseListItem = self.load_class('AdminDatabaseListItem')
        ItemList = self.load_class('ItemList')

        # update this object's locator defaults
        self.locators.update(AdminDatabaseList_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.db_list = ItemList(self,
                                {
                                    'base' : 'listbase',
                                    'row'  : 'item',
                                }, AdminDatabaseListItem,
                                {})


        # update the component's locators with this objects overrides
        self._updateLocators()


class AdminDatabaseList1_Locators_Base_1(object):
    """locators for AdminDatabaseList1 object"""

    locators = {
        'base'      : "css=#form-login",
        'listbase'  : "css=.adminlist",
        'item'      : "css=.adminlist tbody tr",

    }
