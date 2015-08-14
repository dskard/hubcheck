from hubcheck.pageobjects.po_admin_base_page import AdminBasePage

class AdminDatabaseListPage(AdminBasePage):
    """admin database list page object"""

    def __init__(self,browser,catalog):
        super(AdminDatabaseListPage,self).__init__(browser,catalog)
        self.path = '/administrator/index.php?option=com_databases'

        # load hub's classes
        AdminDatabaseListPage_Locators = \
            self.load_class('AdminDatabaseListPage_Locators')
        AdminDatabaseList = self.load_class('AdminDatabaseList')

        # update this object's locator
        self.locators.update(AdminDatabaseListPage_Locators.locators)

        # setup page object's components
        self.db_list = AdminDatabaseList(self,{'base':'dblist'})


class AdminDatabaseListPage_Locators_Base(object):
    """locators for AdminDatabaseListPage object"""

    locators = {
        'dblist'  : "css=.adminlist",
    }
