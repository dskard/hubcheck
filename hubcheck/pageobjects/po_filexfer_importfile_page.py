from hubcheck.pageobjects.basepageobject import BasePageObject
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilexferImportfilePage(BasePageObject):
    """
    Filexfer upload page
    """

    def __init__(self, owner, locatordict={}):
        super(FilexferImportfilePage,self).__init__(owner,locatordict)

        # load hub's classes
        FilexferImportfilePage_Locators = \
            self.load_class('FilexferImportfilePage_Locators')

        # update this object's locator
        self.locators = FilexferImportfilePage_Locators.locators

        # setup page object's components
        self.upload_type = Radio(self,{'File' : 'upload_type_file',
                                       'Text' : 'upload_type_text'})
        self.browse = Text(self,{'base':'browse'},click_focus=False)
        self.filetext = TextArea(self,{'base':'filetext'})
        self.upload = Button(self,{'base':'upload'})


    def upload_file(self,filename,timeout=60):
        """choose a file to upload into the workspace"""

        self.upload_type.value = 'File'
        self.browse.value = filename
        self.upload.click()
        WebDriverWait(self._browser,timeout)\
            .until(EC.title_is('Upload Complete'))


    def upload_text(self,text,timeout=60):
        """upload text to a file in the workspace"""

        self.upload_type.value = 'Text'
        self.filetext.value = text
        self.upload.click()
        WebDriverWait(self._browser,timeout)\
            .until(EC.title_is('Upload Complete'))


class FilexferImportfilePage_Locators_Base(object):
    """locators for FilexferImportfilePage object"""

    locators = {
        'upload_type_file'  : "css=[name='which1'][value='file1']",
        'upload_type_text'  : "css=[name='which1'][value='text1']",
        'browse'            : "css=[name='file1']",
        'filetext'          : "css=[name='text1']",
        'upload'            : "css=#submit [type='submit']",
    }
