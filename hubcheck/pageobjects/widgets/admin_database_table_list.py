from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Link

class AdminDatabaseTableList1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminDatabaseTableList1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminDatabaseTableList_Locators = self.load_class('AdminDatabaseTableList_Locators')
        AdminDatabaseTableListItem = self.load_class('AdminDatabaseTableListItem')
        ItemList = self.load_class('ItemList')

        # update this object's locator defaults
        self.locators.update(AdminDatabaseTableList_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.table_list = ItemList(self,
                                {
                                    'base' : 'listbase',
                                    'row'  : 'item',
                                }, AdminDatabaseTableListItem,
                                {})


        # update the component's locators with this objects overrides
        self._updateLocators()


class AdminDatabaseTableList1_Locators_Base_1(object):
    """locators for AdminDatabaseTableList1 object"""

    locators = {
        'base'      : "css=#form-login",
        'listbase'  : "css=.adminlist",
        'item'      : "css=.adminlist tbody tr",

    }
