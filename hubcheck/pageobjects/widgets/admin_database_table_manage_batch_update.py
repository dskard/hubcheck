from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Link

class AdminDatabaseTableManageBatchUpdate1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminDatabaseTableManageBatchUpdate1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminDatabaseTableManageBatchUpdate_Locators = \
            self.load_class('AdminDatabaseTableManageBatchUpdate_Locators')

        # update this object's locator defaults
        self.locators.update(AdminDatabaseTableManageBatchUpdate_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.download = Link(self,{'base':'download'})
        self.browse = Text(self,{'base':'browse'},click_focus=False)
        self.upload = Button(self,{'base':'upload'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def download_data(self):
        self.download.click()


    def upload_data(self,filename):
        self.browse.value = filename
        self.upload.click()
        self.upload.wait_until_invisible()


class AdminDatabaseTableManageBatchUpdate1_Locators_Base_1(object):
    """locators for AdminDatabaseTableManageBatchUpdate1 object"""

    locators = {
        'base'      : "css=#tabs-4",
        'download'  : "css=#tabs-4 a",
        'browse'    : "css=#csv_file",
        'upload'    : "css=#tabs-4 input[type='submit']",
    }
