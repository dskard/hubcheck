import re
import logging
import time
from urlparse import urlsplit, urlunsplit, urljoin, SplitResult, ParseResult
from hubcheck.exceptions import CatalogError

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import hubcheck.conf


class BasePageObject(object):


    def __init__(self,browser,catalog):

        self._hcbo = browser
        self._catalog = catalog
        self._browser = browser._browser
        self._po = self
        self.logger = logging.getLogger(__name__)
        self.downloaddir = browser.downloaddir
        self.url = urlsplit(self._browser.current_url)
        self.baseUrl = self._populate_urlsplit_tuple(
                            scheme=self.url.scheme,netloc=self.url.netloc)
        self.widgets = []
        self.path = '/'
        self.locator = None


    def _checkLocators(self):

        for w in self.widgets:
            w._checkLocators()


    def _updateLocators(self):

        for w in self.widgets:
            w._updateLocators()


    def _populate_urlparse_tuple(self,scheme='',netloc='',path='',
                                 params='',query='',fragment=''):

        return ParseResult(scheme,netloc,path,params,query,fragment)


    def _populate_urlsplit_tuple(self,scheme='',netloc='',path='',
                                 query='',fragment=''):

        return SplitResult(scheme,netloc,path,query,fragment)


    def _split_locator(self,locator):

        if locator is None:
            return None,None

        (loctype, loctext) = locator.split('=',1)

        loctypes = {
            'id'      : By.ID,
            'name'    : By.NAME,
            'link'    : By.LINK_TEXT,
            'tagname' : By.TAG_NAME,
            'xpath'   : By.XPATH,
            'css'     : By.CSS_SELECTOR,
        }

        loctype = loctypes[loctype]

        self.logger.debug('split locator: %s into loctype = %s, loctext = %s' \
                            % (locator,loctype,loctext))

        return loctype,loctext


    def find_element(self,locator,element=None):

        self.logger.info("searching for browser element: %s in %s" \
                            % (locator,element))

        if locator is None:
            raise NoSuchElementException

        if element is None:
            element = self._browser

        loctype,loctext = self._split_locator(locator)
        result = element.find_element(loctype,loctext)

        self.scroll_to_element(result)
        self.highlight_web_element(result)

        return result


    def find_elements(self,locator,element=None):

        self.logger.info("searching for browser elements: %s in %s" \
                            % (locator,element))

        if locator is None:
            raise NoSuchElementException

        if element is None:
            element = self._browser

        loctype,loctext = self._split_locator(locator)
        result = element.find_elements(loctype,loctext)

        self.highlight_web_element(result)

        return result


    def highlight_web_element(self,element,color='red',timeout=1):

        if hubcheck.conf.settings.highlight_web_elements is False:
            return

        # check if object is iterable, if not, wrap it in a list
        if not hasattr(element,'__iter__'):
            element = [element]

        for e in element:
            self._highlight_element(e,color=color)
        time.sleep(timeout)
        for e in element:
            self._unhighlight_element(e)


    def _highlight_element(self,element,color='red'):

        self.logger.debug('highlighting element %s %s' % (element,color))
        self._browser.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element, "border: 2px solid %s;" % color)


    def _unhighlight_element(self,element):

        self.logger.debug('unhighlighting element: "%s"' % (element))
        self._browser.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element, "")


    def scroll_to_element(self,element):

        if hubcheck.conf.settings.scroll_to_web_elements is False:
            return

        # make sure the element is visible
        if element.is_displayed():
            # we could use action chains or the javascript function
            # scrollIntoView() to accomplish the scroll,
            # but this moves the item to the very top of the screen.
            # i prefer the element be near the middle of the screen
            # so we can see context around what is being highlighted

            # # Method #1: using ActionChains
            # ActionChains(self._browser)\
            # .move_to_element(result)\
            # .perform()

            # # Method #2: using JavaScript
            # self._browser.execute_script(
            #    "arguments[0].scrollIntoView(true);",result)

            # Method #3: using JavaScript with smart scrolling
            # browser menus and tabs take up about 70 px.
            self.logger.debug('scrolling page to element')
            header_height = 70
            offset = (self._browser.get_window_size()['height']/2) - header_height
            scroll_y = element.location['y']-offset
            if scroll_y < 0:
                scroll_y = 0
            self._browser.execute_script("window.scrollTo(0,"+str(scroll_y)+");")


    def find_element_in_owner(self,locator):

        return self.find_element(locator)


    def find_elements_in_owner(self,locator):

        return self.find_elements(locator)


    def goto_page(self,location=None):

        if location is None:
            # location is empty, use the object's path
            location = self.path
        parts = urlsplit(location)
        if parts.netloc == '':
            # location is missing a netloc, use our baseUrl
            location = urljoin(urlunsplit(self.baseUrl),location)
        # go to the page
        self.logger.info("browser go to page: %s" % location)
        self._browser.get(location)


    def current_url(self):

        return self._browser.current_url


    def object_url(self):

        return urljoin(urlunsplit(self.baseUrl),self.path)


    def is_on_page(self):

        currentpageurl = urlsplit(self._browser.current_url)

        # remove trailing / from the path
        normalized_path = re.sub('/$','',currentpageurl.path)
        currentpageurl = self._populate_urlsplit_tuple(
                            currentpageurl.scheme,
                            currentpageurl.netloc,
                            normalized_path,
                            currentpageurl.query,
                            currentpageurl.fragment)

        objectspageurl = urlsplit(urljoin(urlunsplit(self.baseUrl),self.path))
        return currentpageurl == objectspageurl


    def page_title(self):

        return self._browser.title


    def is_present(self,locator):
        """is this element on the page,
           not necessarily visible or can
           be interacted with
        """

        self.logger.debug("browser checking if \"%s\" is present" % locator)
        present = False
        try:
            self.find_element(locator)
            present = True
        except NoSuchElementException:
            present = False
        self.logger.debug("browser element present: %s" % present)
        return present


    def is_displayed(self,locator):
        """can the user see and interact with this element"""

        self.logger.debug("browser checking if \"%s\" is displayed" % locator)
        displayed = False
        try:
            e = self.find_element(locator)
            displayed = e.is_displayed()
        except NoSuchElementException:
            displayed = False
        self.logger.debug("browser element displayed: %s" % displayed)
        return displayed


    def count_elements(self,locator):

        return len(self.find_elements(locator))


    def wait_for_page_element_displayed(self,loc='css=body',displayed=True,timeout=10):

        self.logger.debug(
            "waiting for page element '%s' displayed == %s" \
            % (loc,displayed))

        def condition(browser):
            #return self.is_displayed(loc) == displayed
            return self.is_displayed(loc)

        try:
            wait = WebDriverWait(self._browser,timeout)
            if displayed:
                message='while waiting for element "%s" to load' % loc
                wait.until(condition,message=message)
            else:
                message='while waiting for element "%s" to disappear' % loc
                wait.until_not(condition,message=message)
        except TimeoutException as e:
            # save a screen shot and reraise the exception
            # browser.save_screenshot_as_base64
            # self._browser.save_screenshot_as_file("need_help.submitted-1.png")
            self.logger.exception(e)
            raise
        except StaleElementReferenceException:
            # ignore stale element reference exceptions for now.
            pass


    def set_page_load_marker(self):

        self._browser.execute_script(
            "document.body.setAttribute(\"hc_page_load_marker\", \"%s\")" \
            % self._hcbo.next_marker())
        self.logger.debug("setting page marker: '%s'" % (self._hcbo.marker))

        loc = "body[hc_page_load_marker='%s']" % self._hcbo.marker
        r =  self._browser.find_element_by_css_selector(loc).get_attribute(
                'hc_page_load_marker')
        self.logger.debug("marker set as %s" % (r))


    def wait_for_page_load_marker(self):

        loc = "body[hc_page_load_marker='%s']" % self._hcbo.marker

        wait = WebDriverWait(self._browser,30)

        def condition(browser):
            try:
                self.logger.debug("looking for page marker: '%s'" % (loc))
                browser.find_element_by_css_selector(loc)
            except NoSuchElementException:
                return True
            return False

        # wait for the marker to disappear
        message = "waiting for the new page to load"
        wait.until(condition,message)

        # page is loading

        # wait for page load to complete
        wait.until(
            lambda browser: \
                browser.execute_script(
                    "return document.readyState;") == "complete")



    def wait_for_page_to_load(self):

        self.logger.debug("waiting for page to load")

        try:
            self.wait_for_page_load_marker()
            if self._hcbo.proxy_client is not None:
                self._hcbo.proxy_client.wait_for_traffic_to_stop(2,10)
        except TimeoutException:
            # save a screen shot and reraise the exception
            # browser.save_screenshot_as_base64
            # self._browser.save_screenshot_as_file("need_help.submitted-1.png")
            #raise TimeoutException(
            #    'timed out while waiting for page to finish loading')
            pass
        except StaleElementReferenceException:
            # page reloaded after wait started, wait again?
            # not sure what to do here yet
            # self.wait_for_page_to_finish_loading()
            pass


    def load_class(self,classname):

        if self._catalog is None:
            msg = "page object has invalid catalog: None"
            self.logger.error(msg)
            raise CatalogError(msg)

        self.logger.debug("pageobject '%s' loading class '%s'" \
            % (self.__class__.__name__,classname))

        return self._catalog.load(classname)


    def manage_alert(accept=True):
        alert = self._browser.switch_to_alert()
        if accept is True:
            alert.accept()
        else:
            alert.dismiss()
