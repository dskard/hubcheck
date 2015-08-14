from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text

class Upload2(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Upload2,self).__init__(owner,locatordict)

        # load hub's classes
        Upload2_Locators = self.load_class('Upload2_Locators')

        # update this object's locator
        self.locators.update(Upload2_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.fname = Text(self,{'base':'fname'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    @property
    def value(self):

        return self.fname.value


    @value.setter
    def value(self,val):
        """upload filename or list of filenames provided as parameter"""

        if not val:
            return
        if not isinstance(val,list):
            val = [val]
        for item in val:
            nrows = len(self.find_elements(self.locators['attachments']))
            self.fname.append(item)
            self._po.wait_for_page_element_displayed(self.locators['next_upload'] % (nrows+1))



class Upload2_Locators_Base(object):
    """locators for Upload2 object"""

    locators = {
        'base'      : "css=#file-uploader",
        'fname'     : "css=#file-uploader [name='file']",
        'attachments' : "css=#file-uploader-list tr",
        'next_upload' : "css=#file-uploader-list tr:nth-of-type(%s)",
    }
