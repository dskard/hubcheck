from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from selenium.webdriver.support.ui import WebDriverWait

class MembersProfileElement(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersProfileElement,self).__init__(owner,locatordict)

        # load hub's classes
        MembersProfileElement_Locators = self.load_class('MembersProfileElement_Locators')

        # update this object's locator
        self.locators.update(MembersProfileElement_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.sectionkey     = TextReadOnly(self,{'base':'sectionkey'})
        self.sectionvalue   = TextReadOnly(self,{'base':'sectionvalue'})
        self.openlink       = Link(self,{'base':'open'})
        self.closelink      = Link(self,{'base':'close'})
        self.save           = Button(self,{'base':'save'},self._onClickSave)
        self.cancel         = Button(self,{'base':'cancel'},self._onClickCancel)

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocators(self, widgets=None, cltype=''):

        self.open()
        super(MembersProfileElement,self)._checkLocators(widgets,cltype)


    def _onClickSave(self):

        self.save.wait_until_invisible()


    def _onClickCancel(self):

        self.cancel.wait_until_invisible()


    def open(self):
        """open the slide to reveal the widget"""

        self.openlink.click()

        # wait until the save and cancel buttons are displayed in the DOM
        self.wait_until_visible(locator=self.locators['save'])


    def close(self):
        """close the slide to hide the widget"""

        self.closelink.click()

        # wait until the save and cancel buttons are not displayed in the DOM
        self.wait_until_invisible(locator=self.locators['save'])


class MembersProfileElement_Locators_Base(object):
    """locators for MembersProfileElement object"""

    locators = {
        'sectionkey'    : "css=.key",
        'sectionvalue'  : "css=.value",
        'open'          : "css=.edit-profile-section",
        'close'         : "css=.edit-profile-section",
        'save'          : "css=.section-edit-submit",
        'cancel'        : "css=.section-edit-cancel",
    }
