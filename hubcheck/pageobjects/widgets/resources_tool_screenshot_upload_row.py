from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

class ResourcesToolScreenshotUploadRow(ItemListItem):

    def __init__(self, owner, locatordict={}, row_number=0):

        super(ResourcesToolScreenshotUploadRow,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        ResourcesToolScreenshotUploadRow_Locators = self.load_class('ResourcesToolScreenshotUploadRow_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolScreenshotUploadRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.edit     = Link(self,{'base':'edit'})
        self.img_edit = Link(self,{'base':'img_edit'})
        self.delete   = Link(self,{'base':'delete'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return the title"""

        return self.img_edit.get_attribute('title')


class ResourcesToolScreenshotUploadRow_Locators_Base(object):
    """locators for ResourcesToolScreenshotUploadRow object"""

    locators = {
        'base'           : "css=.screenshots li:nth-of-type(2*{row_num}-1)",
        'edit'           : "css=.screenshots li:nth-of-type(2*{row_num}-1) .edit_ss",
        'img_edit'       : "css=.screenshots li:nth-of-type(2*{row_num}-1) .popup",
        'delete'         : "css=.screenshots li:nth-of-type(2*{row_num}-1) .delete_ss",
    }
