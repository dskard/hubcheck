from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.exceptions import NoSuchFileAttachmentError
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class Upload3(BasePageWidget):
    """upload widget with browse input and upload button and file viewer.

       the browse input and upload buttons are inside of an iframe
       the file viewer is inside of two iframes
    """

    def __init__(self, owner, locatordict, row_class, row_class_loc_dict):
        super(Upload3,self).__init__(owner,locatordict)

        # load hub's classes
        Upload3_Locators = self.load_class('Upload3_Locators')
        UploadListRow = self.load_class('UploadListRow')
        ItemList = self.load_class('ItemList')

        # update this object's locator
        self.locators.update(Upload3_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.browse = IframeWrap(
                        Text(self,{'base':'browse'},click_focus=False),
                        ['uploadframe'])
        self.upload = IframeWrap(
                        Button(self,{'base':'upload'}),
                        ['uploadframe'])
        self.filelist = IframeWrap(
                            ItemList(self,
                                     {'base':'uploadlist',
                                      'row':'uploadlistrow'},
                                     row_class, row_class_loc_dict),
                            ['fileframe', 'uploadframe'])

        # update the component's locators with this objects overrides
        self._updateLocators()


    @property
    def value(self):
        return self.get_uploaded_files()


    @value.setter
    def value(self,filenames):
        """upload list of filenames"""

        if not hasattr(filenames,'__iter__'):
            filenames = [filenames]

        for filename in filenames:
            self.browse.value = filename
            self.upload.click()

            # wait for the row to appear
            message = "row with filename %s did not appear" % (filename)

            def condition(browser):
                self.logger.debug('waiting until row with file %s appears' \
                    % (filename))
                row = self.filelist.get_row_by_property('filename',filename)
                return row is None

            ignored_exceptions = [ TimeoutException,
                                   NoSuchElementException,
                                   StaleElementReferenceException ]

            w = WebDriverWait(self._browser,10,
                    ignored_exceptions=ignored_exceptions)
            w.until(condition,message=message)


    def get_uploaded_files(self):
        """return a list of files uploaded to the wiki page"""

        fnames = []
        for row in self.filelist:
            fnames.append(row.value()['filename'])
        return fnames


    def delete_file(self,filename):
        """delete a file uploaded to the wiki page"""

        # get the row representing the file
        row = self.filelist.get_row_by_property('filename',filename)

        if row is None:
            raise NoSuchFileAttachmentError(
                "file named \"%s\" not uploaded" % (filename))

        # click the delete link
        row.delete.click()

        # wait for the row to disappear
        message = "row with filename %s did not disappear" % (filename)

        def condition(browser):
            self.logger.debug('waiting until row with file %s disappears' \
                % (filename))
            row = self.filelist.get_row_by_property('filename',filename)
            return row is None

        ignored_exceptions = [ TimeoutException,
                               NoSuchElementException,
                               StaleElementReferenceException ]

        w = WebDriverWait(self._browser,10,
                ignored_exceptions=ignored_exceptions)
        w.until_not(condition,message=message)


class Upload3_Locators_Base(object):
    """locators for Upload3 object"""

    locators = {
        'base'          : "css=#file-uploader",
        'uploadframe'   : "css=#filer",
        'browse'        : "css=#upload",
        'upload'        : "css=#adminForm input[type='submit']",
        'fileframe'     : "css=#imgManager",
        'uploadlist'    : "css=#filelist",
        'uploadlistrow' : "css=#filelist tr",
    }
