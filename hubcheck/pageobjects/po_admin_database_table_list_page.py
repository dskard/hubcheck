from hubcheck.pageobjects.po_admin_base_page import AdminBasePage
from hubcheck.pageobjects.basepageelement import Link

class AdminDatabaseTableListPage(AdminBasePage):
    """admin database table list page object"""

    def __init__(self,browser,catalog):
        super(AdminDatabaseTableListPage,self).__init__(browser,catalog)
        # this path needs a database associated with it
        # ex:
        # /administrator/index.php?option=com_databases&task=table_list&db=solarpv
        self.path = '/administrator/index.php?option=com_databases&task=table_list'

        # load hub's classes
        AdminDatabaseTableListPage_Locators = \
            self.load_class('AdminDatabaseTableListPage_Locators')
        AdminDatabaseTableList = self.load_class('AdminDatabaseTableList')

        # update this object's locator
        self.locators.update(AdminDatabaseTableListPage_Locators.locators)

        # setup page object's components
        self.table_list = AdminDatabaseTableList(self,{'base':'tablelist'})
        self.back = Link(self,{'base':'back'})
        self.new_table = Link(self,{'base':'new_table'})


    def goto_back(self):

        self.back.click()


class AdminDatabaseTableListPage_Locators_Base(object):
    """locators for AdminDatabaseTableListPage object"""

    locators = {
        'tablelist'  : "css=.adminlist",
        'back'       : "css=#toolbar-back a",
        'new_table'  : "css=#toolbar-new a",
    }
