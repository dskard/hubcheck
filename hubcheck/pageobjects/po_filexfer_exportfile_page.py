from hubcheck.pageobjects.basepageobject import BasePageObject
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap


class FilexferExportfilePage(BasePageObject):
    """
    Filexfer download page
    """

    def __init__(self, owner, locatordict={}):
        super(FilexferExportfilePage,self).__init__(owner,locatordict)

        # load hub's classes
        FilexferExportfilePage_Locators = \
            self.load_class('FilexferExportfilePage_Locators')

        # update this object's locator
        self.locators = FilexferExportfilePage_Locators.locators

        # setup page object's components
        self.save_as = IframeWrap(Button(self,{'base':'saveas'}),['topframe'])
        self.print_b = IframeWrap(Button(self,{'base':'print'}),['topframe'])
        self.file_text = IframeWrap(TextReadOnly(self,{'base':'filetext'}),
                            ['fileframe'])


    def get_file_text(self):
        """retrieve the exported file's text"""

        return self.file_text.value


class FilexferExportfilePage_Locators_Base(object):
    """locators for FilexferExportfilePage object"""

    locators = {
        'saveas'         : "css=input[value='Save As...']",
        'print'          : "css=input[value='Print...']",
        'filetext'       : "css=pre",
        'topframe'       : "css=#container frame:nth-of-type(1)",
        'fileframe'      : "css=#container frame[name='file']",
    }
