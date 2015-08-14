import logging
import pprint
import hubcheck.conf

from hubcheck.exceptions import LocatorException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class BasePageWidget(object):
    def __init__(self, owner, locatordict):
        self.owner = owner
        self.locators = {}
        self.locatordict = locatordict
        self._browser = owner._browser
        self._po = owner._po
        self.logger = owner.logger
        self.widgets = []
        self.iframe_tracker = None

        # in general, functions that do not call any of the
        # find_element* functions should go in the noiframe list
        self.noiframe = ['_updateLocators',
                         'attach_to_owner',
                         'detach_from_owner',
                         'update_locators_from_owner',
                         'update_locators_in_widgets',
                         'load_class',
                        ]

        self.attach_to_owner()
        self._updateLocators()


    def __del__(self):
        try:
            for w in self.widgets:
                del w
            self.detach_from_owner()
        except Exception as e:
            self.logger.exception(e)


    def attach_to_owner(self):
        # register the widget with it's owner
        # so it can get checked by _checkLocators
        # and updated by _updateLocators
        if hubcheck.conf.settings.log_widget_attachments:
            self.logger.debug("%s attaching to owner %s with locators %s" \
                % (self.__class__.__name__,self.owner.__class__.__name__,
                pprint.pformat(self.locatordict)))
        self.owner.widgets.append(self)


    def detach_from_owner(self):
        # unregister the widget with it's owner
        # so it can be deleted
        if hubcheck.conf.settings.log_widget_attachments:
            self.logger.debug("%s detaching from owner %s" \
                % (self.__class__.__name__,self.owner.__class__.__name__))
        try:
            self.owner.widgets.remove(self)
        except ValueError:
            pass


    def _checkLocators(self,widgets=None,cltype=''):
        header = "\n===== missing locators in %s =====" % (self.owner.__class__.__name__)
        missing = ''

        if widgets is None:
            widgets = self.widgets

        if self.is_present() == False:
            # missing += "\n%s: \"%s\"" % (self.locatorid,self.locators['base'])
            missing += "\nbase: \"%s\"" % (self.locators['base'])

        for w in widgets:
            clfxn = getattr(w,"_checkLocators%s" % (cltype), None)
            if clfxn is None:
                clfxn = getattr(w,"_checkLocators")
            clfxn(cltype=cltype)

        if missing != '':
            raise LocatorException(header+missing)


    def _updateLocators(self):
        self.update_locators_from_owner()
        self.update_locators_in_widgets()

        if hubcheck.conf.settings.log_locator_updates:
            self.logger.debug("%s locators: %s" \
                % (self.__class__.__name__,pprint.pformat(self.locators)))


    def update_locators_in_widgets(self):
        for w in self.widgets:
            w._updateLocators()


    def update_locators_from_owner(self):
        if self.locators == {}:
            for k,v in self.locatordict.items():
                self.locators[k] = self.owner.locators[v]
        else:
            for k,v in self.locatordict.items():
                if k in self.locators:
                    self.locators[k] = self.owner.locators[v]


    def find_element(self,locator,base=None):
        e = self._po.find_element(locator,base)
        return e


    def find_elements(self,locator,base=None):
        e = self._po.find_elements(locator,base)
        return e


    def find_element_in_owner(self,locator):
        base = None
        e = self._po.find_element(locator,base)
        return e


    def find_elements_in_owner(self,locator):
        base = None
        e = self._po.find_elements(locator,base)
        return e


    def is_present(self,locator=None,base=None):
        """is this element on the page,
           not necessarily visible or can
           be interacted with"""

        present = False

        if locator is None:
            locator = self.locators['base']

        self.logger.debug("browser checking if widget \"%s\" is present" \
            % (locator))

        try:
            self.owner.find_element(locator,base)
            present = True
        except NoSuchElementException:
            present = False

        self.logger.debug("browser element present: %s" % present)

        return present


    def is_displayed(self,locator=None,base=None):
        """can the user see and interact with this element"""

        displayed = False

        if locator is None:
            locator = self.locators['base']

        self.logger.debug("browser checking if widget \"%s\" is displayed" \
            % (locator))

        try:
            e = self.owner.find_element(locator,base)
            displayed = e.is_displayed()
        except NoSuchElementException:
            displayed = False

        self.logger.debug("browser element displayed: %s" % displayed)

        return displayed


    def wait_until_present(self,message='',locator=None):

        if locator is None:
            locator = self.locators['base']

        if message == '':
            message = 'while waiting for %s to become present' % (locator)

        def condition(browser):
            self.logger.debug('waiting until %s present' % (locator))
            return self.owner.find_element_in_owner(locator)

        ignored_exceptions = [ TimeoutException,
                               NoSuchElementException,
                               StaleElementReferenceException ]

        w = WebDriverWait(self._browser,10,
                ignored_exceptions=ignored_exceptions)
        e = w.until(condition,message=message)

        return e


    def wait_until_not_present(self,message='',locator=None):

        if locator is None:
            locator = self.locators['base']

        if message == '':
            message = 'while waiting for %s to become not present' % (locator)

        def condition(browser):
            self.logger.debug('waiting until %s not present' % (locator))
            return self.owner.find_element_in_owner(locator)

        ignored_exceptions = [ TimeoutException,
                               NoSuchElementException,
                               StaleElementReferenceException ]

        w = WebDriverWait(self._browser,10,
                ignored_exceptions=ignored_exceptions)
        w.until_not(condition,message=message)


    def wait_until_visible(self,message='',locator=None):

        if locator is None:
            locator = self.locators['base']

        if message == '':
            message = 'while waiting for %s to become visible' % (locator)

        def condition(browser):
            self.logger.debug('waiting until %s visible' % (locator))
            e = self.owner.find_element_in_owner(locator)
            if e.is_displayed():
                return e
            else:
                return False

        ignored_exceptions = [ TimeoutException,
                               NoSuchElementException,
                               StaleElementReferenceException ]

        w = WebDriverWait(self._browser,10,
                ignored_exceptions=ignored_exceptions)
        e = w.until(condition,message=message)

        return e


    def wait_until_invisible(self,message='',locator=None):

        if locator is None:
            locator = self.locators['base']

        if message == '':
            message = 'while waiting for %s to become invisible' % (locator)

        def condition(browser):
            self.logger.debug('waiting until %s invisible' % (locator))
            e = self.owner.find_element_in_owner(locator)
            if e.is_displayed():
                return e
            else:
                return False

        ignored_exceptions = [ TimeoutException,
                               NoSuchElementException,
                               StaleElementReferenceException ]

        w = WebDriverWait(self._browser,10,
                ignored_exceptions=ignored_exceptions)
        w.until_not(condition,message=message)


    def get_attribute(self,attribute):
        e = self.owner.find_element(self.locators['base'])
        return e.get_attribute(attribute)


    def get_tag_name(self):
        e = self.owner.find_element(self.locators['base'])
        return e.tag_name


    def load_class(self,classname):
        return self.owner.load_class(classname)


    def hover_mouse_over(self,locator=None):

        if locator is None:
            locator = self.locators['base']

        e = self.find_element(locator)

        # hover mouse over the item
        ActionChains(self._browser)\
        .move_to_element(e)\
        .perform()

        return e

