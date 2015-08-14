from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.exceptions import NoSuchFileAttachmentError
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class UploadList2(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(UploadList2,self).__init__(owner,locatordict)

        # load hub's classes
        UploadList2_Locators = self.load_class('UploadList2_Locators')

        # update this object's locator
        self.locators.update(UploadList2_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self._updateLocators()


    def get_uploaded_files(self):

        fname = []
        elist = []

        try:
            elist = self.find_elements_in_owner(self.locators['filename'])
        except NoSuchElementException:
            pass

        # store filename is there are any
        fnames = [e.text for e in elist]

        return fname


    def delete_file(self,filename):

        if not filename:
            return
        elist = self.find_elements_in_owner(self.locators['row'])
        for e in elist:
            fnameEle = self.find_element(self.locators['filename'],e)
            if fnameEle.text == filename:
                self.logger.debug('deleting row with filename: %s' % (filename))
                deleteEle = self.find_element(self.locators['delete'],e)
                deleteEle.click()
                loc = self.locators['deletecheck'] % (filename)
                self.wait_until_not_present(locator=loc)
                break
        else:
            raise NoSuchFileAttachmentError(
                "file named \"%s\" not uploaded" % (filename))


class UploadList2_Locators_Base(object):
    """locators for UploadList2 object as seen on hubzero.org"""

    locators = {
        'base'          : "css=#file-uploader-list",
        'row'           : "css=#file-uploader-list tr",
        'filetype'      : "css=#file-uploader-list td:nth-of-type(1)",
        'filename'      : "css=#file-uploader-list td:nth-of-type(2)",
        'delete'        : "css=#file-uploader-list .delete",
        'deletecheck'   : "xpath=//td//*[text()='%s']/../..",
    }


class UploadList2_Locators_Base_2(object):
    """locators for UploadList2 object as see on dev.hubzero.org"""

    locators = {
        'base'          : "css=#file-uploader-list",
        'row'           : "css=#file-uploader-list tr",
        'filetype'      : "css=",
        'filename'      : "css=#file-uploader-list td:nth-of-type(1)",
        'delete'        : "css=#file-uploader-list .delete",
        'deletecheck'   : "xpath=//td//*[text()='%s']/../..",
    }
