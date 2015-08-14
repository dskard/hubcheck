from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.exceptions import NoSuchFileAttachmentError
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class UploadList1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(UploadList1,self).__init__(owner,locatordict)

        # load hub's classes
        UploadList1_Locators = self.load_class('UploadList1_Locators')

        # update this object's locator
        self.locators.update(UploadList1_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def find_element_in_owner(self,locator):
        # switch to the iframe's context
        # use the pageobject's find_element() function
        # because we want to search within the iframe

        framebase = self._switch_to_iframe_context()
        e = self._po.find_element(locator,framebase)
        return e


    def find_elements_in_owner(self,locator):
        # switch to the iframe's context
        # use the pageobject's find_element() function
        # because we want to search within the iframe

        framebase = self._switch_to_iframe_context()
        e = self._po.find_elements(locator,framebase)
        return e


    def _switch_to_iframe_context(self):
        # switch to the iframe's context

        frame = self.owner.find_element_in_owner(self.locators['base'])
        self._browser.switch_to_frame(frame)

        # use the html tag as the base while in the iframe
        insideframe = self._po.find_element(self.locators['framebase'])
        return insideframe


    def _switch_to_default_context(self):
        # switch back to the main page's context
        # this should be called after any of the following methods:
        #   _switch_to_iframe_context
        #   find_element
        #   find_elements

        self._browser.switch_to_default_content()


    def get_uploaded_files(self):

        fnames = []
        elist = []

        try:
            elist = self.find_elements_in_owner(self.locators['filename'])
        except NoSuchElementException:
            pass

        # store filename is there are any
        fnames = [e.text for e in elist]

        # get out of the iframe
        self._switch_to_default_context()

        return fnames


    def delete_file(self,filename):

        if not filename:
            return
        elist = self.find_elements_in_owner(self.locators['row'])
        for e in elist:
            fnameEle = self.find_element(self.locators['filename'],e)
            if fnameEle.text == filename:
                deleteEle = self.find_element(self.locators['delete'],e)
                deleteEle.click()
                try:
                    # wait for the row to disappear from the list
                    # we need to do a little wait, 1 or 2 second usually
                    # to let the page update. the testDeleteFileFunction
                    # unit tests fails without this as the calls to
                    # get_uploaded_files() returns the wrong value.
                    # unfortunately, asking to do find_element()
                    # inside of webdriverwait takes at least
                    # 10 seconds depending on the default wait time.
                    # i'm thinking the find_element() isnt worth the wait.
                    loc = self.locators['deletecheck'] % (filename)
                    wait = WebDriverWait(self._po, 5)
                    def waitCondition(po):
                        try:
                            po.find_element(loc)
                            return False
                        except:
                            return True
                    wait.until(waitCondition)
                except TimeoutException:
                    # get out of the iframe
                    self._switch_to_default_context()

                    # browser.save_screenshot_as_base64
                    # self._browser.save_screenshot_as_file("need_help.submitted-1.png")
                    raise TimeoutException("Timeout while waiting for deleted row to disappear")

                break
        else:
            # get out of the iframe
            self._switch_to_default_context()

            raise NoSuchFileAttachmentError("file named \"%s\" not uploaded" % (filename))

        # get out of the iframe
        self._switch_to_default_context()


class UploadList1_Locators_Base(object):
    """locators for UploadList1 object as seen on hubzero.org"""

    locators = {
        'base'          : "css=#attaches",
        'row'           : "css=tr",
        'filename'      : "css=.ftitle",
        'filetypesize'  : "css=.caption",
        'delete'        : "css=.t",
        'deletecheck'   : "xpath=//span[text()='%s']",
        'framebase'     : "css=html",
    }
