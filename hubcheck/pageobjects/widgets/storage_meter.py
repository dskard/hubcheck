from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly


class StorageMeter(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(StorageMeter,self).__init__(owner,locatordict)

        # load hub's classes
        StorageMeter_Locators = self.load_class('StorageMeter_Locators')

        # update this object's locator
        self.locators.update(StorageMeter_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.manage = Link(self,{'base':'manage'})
        self.meter = TextReadOnly(self,{'base':'meter'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_manage(self):
        """navigate to the storage management page"""

        return self.manage.click()


    def storage_meter(self):
        """return the used percentage and total amount of storage in GB"""

        return self.meter.value


class StorageMeter_Locators_Base_1(object):
    """locators for StorageMeter object"""

    locators = {
        'base'      : "css=.session-storage",
        'manage'    : "css=.session-storage span a",
        'meter'     : "css=.storage-meter-amount",
    }

class StorageMeter_Locators_Base_2(object):
    """locators for StorageMeter object"""

    locators = {
        'base'      : "css=#diskusage",
        'manage'    : "css=#diskusage dt a",
        'meter'     : "css=#du-amount",
    }
