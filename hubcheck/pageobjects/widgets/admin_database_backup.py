from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import Link

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminDatabaseBackup1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminDatabaseBackup1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminDatabaseBackup_Locators = self.load_class('AdminDatabaseBackup_Locators')
#        ItemList = self.load_class('ItemList')

        # update this object's locator defaults
        self.locators.update(AdminDatabaseBackup_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.backup = Button(self,{'base':'backup'})
        self.backup_log = TextArea(self,{'base':'backup_log'})
#        self.download_list = ItemList(self,
#                                {
#                                    'base' : 'listbase',
#                                    'row'  : 'item',
#                                }, Link,
#                                {'base':'download_link'})


        # update the component's locators with this objects overrides
        self._updateLocators()


    def do_backup(self):
        """perform a database backup"""

        oldlog = self.backup_log.value
        self.backup.click()

        # wait for the alert to show up
        self.logger.debug('waiting for database backup confirmation')
        WebDriverWait(self._browser,10).until(EC.alert_is_present(),
            'while waiting for the database backup confirmation')
        self.logger.debug('found confirmation')
        alert = self._browser.switch_to_alert()
        alert.accept()
        self.logger.debug('accepted confirmation')
        self._browser.switch_to_default_content()

        def has_new_log_info(driver):
            driver.refresh()
            newlog = self.backup_log.value
            logdiff = newlog[0:-len(oldlog)]
            if len(logdiff) > 0:
                return logdiff
            else:
                return False

        logdiff = WebDriverWait(self._browser,10)\
                    .until(has_new_log_info,
                        'while waiting for new backup log info')

        # return the new log text
        return logdiff


class AdminDatabaseBackup1_Locators_Base_1(object):
    """locators for AdminDatabaseBackup1 object"""

    locators = {
        'base'       : "css=#main",
        'backup'     : "css=#db-backup-now",
        'backup_log' : "css=#main textarea",
    }
