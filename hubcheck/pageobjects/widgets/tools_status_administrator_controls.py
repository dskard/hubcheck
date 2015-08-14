from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class ToolsStatusAdministratorControls(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusAdministratorControls,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusAdministratorControls_Locators = \
            self.load_class('ToolsStatusAdministratorControls_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusAdministratorControls_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.addrepo    = Link(self,{'base':'addrepo'},self._onClick)
        self.install    = Link(self,{'base':'install'},self._onClick)
        self.publish    = Link(self,{'base':'publish'},self._onClick)
        self.retire     = Link(self,{'base':'retire'},self._onClick)

        # update the component's locators with this objects overrides
        self._updateLocators()


    def do_addrepo(self):

        return self.addrepo.click()


    def do_install(self):

        return self.install.click()


    def do_publish(self):

        return self.publish.click()


    def do_retire(self):

        return self.retire.click()


    def _onClick(self):

        self.logger.debug("waiting for response from admin control")

        try:
            # wait for the page to refresh
            wait = WebDriverWait(self._browser, 300)
            wait.until(lambda browser :
                       browser.find_element_by_id("ctSuccess").is_displayed())
        except TimeoutException:
            raise TimeoutException(
                "Timeout while waiting for contribtool admin control to return")

        e = self.find_element(self.locators['output'])
        text = e.text

        self.logger.info("admin control returned: %s" % (text))
        self.logger.debug("checking output for pass / fail")

        status_passed = False
        try:
            # check if the message was success or failure
            wait = WebDriverWait(self._browser, 5)
            wait.until(lambda e :
                       e.find_element_by_css_selector(".passed").is_displayed())
            status_passed = True
        except TimeoutException:
            pass

        self.logger.debug("status_passed = %s" % (status_passed))

        return (status_passed,text)


class ToolsStatusAdministratorControls_Locators_Base(object):
    """locators for ToolsStatusAdministratorControls object"""

    locators = {
        'base'              : "css=#adminCalls",
        'addrepo'           : "css=#createtool",
        'install'           : "css=#installtool",
        'publish'           : "css=#publishtool",
        'retire'            : "css=#retiretool",
        'output'            : "css=#output",
        'ctpassed'          : "css=#output .passed",
        'ctfailed'          : "css=#output .failed",
#        'ctstatus'          : "css=#ctSuccess",
    }

