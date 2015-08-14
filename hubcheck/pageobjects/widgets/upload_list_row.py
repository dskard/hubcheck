from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

class UploadListRow(ItemListItem):

    def __init__(self, owner, locatordict={}, row_number=0):

        super(UploadListRow,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        UploadListRow_Locators = self.load_class('UploadListRow_Locators')

        # update this object's locator
        self.locators.update(UploadListRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.filename = TextReadOnly(self,{'base':'filename'})
        self.delete = Link(self,{'base':'delete'},self.manage_alert)

        # update the component's locators with this objects overrides
        self._updateLocators()


    def manage_alert(self,accept=True):
        alert = self._browser.switch_to_alert()
        if accept is True:
            alert.accept()
        else:
            alert.dismiss()


    def value(self):
        """return a dictionary of the following row properties:
            filename
        """

        # text looks like this:
        # <filename>
        # simulink.jpg
        return({'filename':self.filename.value})


class UploadListRow_Locators_Base(object):
    """locators for UploadListRow object"""

    locators = {
        'base'           : "css=#filelist tr:nth-of-type({row_num})",
        'filename'       : "css=#filelist tr:nth-of-type({row_num}) .file",
        'delete'         : "css=#filelist tr:nth-of-type({row_num}) a.delete",
    }
