from hubcheck.pageobjects.po_admin_base_page import AdminBasePage
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class AdminDatabaseTableManagePage(AdminBasePage):
    """admin database table list page object"""

    def __init__(self,browser,catalog):
        super(AdminDatabaseTableManagePage,self).__init__(browser,catalog)
        # this path needs a database associated with it
        # ex:
        # /administrator/index.php?option=com_databases&task=table_list&db=solarpv
        self.path = '/administrator/index.php?option=com_databases&task=table_list'

        # load hub's classes
        AdminDatabaseTableManagePage_Locators = \
            self.load_class('AdminDatabaseTableManagePage_Locators')
        AdminDatabaseList = self.load_class('AdminDatabaseTableList')
#        AdminDatabaseTableManageTableData = \
#            self.load_class('AdminDatabaseTableManageTableData')
#        AdminDatabaseTableManageAddRecord = \
#            self.load_class('AdminDatabaseTableManageAddRecord')
        AdminDatabaseTableManageBatchUpdate = \
            self.load_class('AdminDatabaseTableManageBatchUpdate')
#        AdminDatabaseTableManageRemoveTable = \
#            self.load_class('AdminDatabaseTableManageRemoveTable')

        # update this object's locator
        self.locators.update(AdminDatabaseTableManagePage_Locators.locators)

        # setup page object's components
        self.back = Link(self,{'base':'back'})

        self.message = TextReadOnly(self,{'base':'message'})
        self.menu_table_data = Link(self,{'base':'menu_table_data'})
        self.menu_add_record = Link(self,{'base':'menu_add_record'})
        self.menu_batch_update = Link(self,{'base':'menu_batch_update'})
        self.menu_remove_table = Link(self,{'base':'menu_remove_table'})

#        self.table_data = AdminDatabaseTableManageTableData(self,{'base':'table_data'})
#        self.add_record = AdminDatabaseTableManageAddRecord(self,{'base':'ble_data'})
        self.batch_update = AdminDatabaseTableManageBatchUpdate(self,{'base':'batch_update'})
#        self.remove_table = AdminDatabaseTableManageRemoveTable(self,{'base':'table_data'})


    def goto_table_data(self):

        self.menu_table_data.click()


    def goto_add_record(self):

        self.menu_add_record.click()


    def goto_batch_update(self):

        self.menu_batch_update.click()


    def goto_remove_table(self):

        self.menu_remove_table.click()


    def goto_back(self):

        self.back.click()


class AdminDatabaseTableManagePage_Locators_Base(object):
    """locators for AdminDatabaseTableManagePage object"""

    locators = {
        'tablelist'         : "css=.adminlist",
        'back'              : "css=#toolbar-back a",
        'message'           : "css=#main .message",
        'menu_table_data'   : "css=#ui-id-1",
        'menu_add_record'   : "css=#ui-id-2",
        'menu_batch_update' : "css=#ui-id-3",
        'menu_remove_table' : "css=#ui-id-4",
        'table_data'        : "css=#tabs-1",
        'add_record'        : "css=#tabs-2",
        'batch_update'      : "css=#tabs-4",
        'remove_table'      : "css=#tabs-5",
    }
