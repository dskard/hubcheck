from hubcheck.pageobjects.po_admin_base_page import AdminBasePage
from hubcheck.pageobjects.basepageelement import Link

class AdminDatabaseBackupPage(AdminBasePage):
    """admin database list page object"""

    def __init__(self,browser,catalog):
        super(AdminDatabaseBackupPage,self).__init__(browser,catalog)
        # this path needs a database associated with it
        # ex:
        # /administrator/index.php?option=com_databases&task=backup_list&db=solarpv
        self.path = '/administrator/index.php?option=com_databases'\
                    + '&task=backup_list'
#                    + '&db=%s' % (dbname)

        # load hub's classes
        AdminDatabaseBackupPage_Locators = \
            self.load_class('AdminDatabaseBackupPage_Locators')
        AdminDatabaseBackup = self.load_class('AdminDatabaseBackup')

        # update this object's locator
        self.locators.update(AdminDatabaseBackupPage_Locators.locators)

        # setup page object's components
        self.back = Link(self,{'base':'back'})
        self.backup = AdminDatabaseBackup(self,{'base':'backup'})


    def goto_back(self):

        self.back.click()


class AdminDatabaseBackupPage_Locators_Base(object):
    """locators for AdminDatabaseBackupPage object"""

    locators = {
        'backup' : "css=#main",
        'back'   : "css=#toolbar-back a",
    }
