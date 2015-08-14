import time
import re
import logging

from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from hubcheck.exceptions import LocatorException
from hubcheck.pageobjects.basepagewidget import BasePageWidget


class Button(BasePageWidget):


    def __init__(self, owner, locatordict, onClick=None):
        super(Button,self).__init__(owner, locatordict)
        self.onClick = onClick


    @property
    def value(self):
        e = self.wait_until_present()
        return e.get_attribute('value')


    def click(self):
        self.logger.info("clicking %s" % (self.locators['base']))
        e = self.wait_until_present()
        e.click()

        # perform "after-click" actions
        if self.onClick is not None:
            return self.onClick()


class Checkbox(BasePageWidget):


    @property
    def value(self):
        e = self.wait_until_present()
        return e.is_selected()


    @value.setter
    def value(self, val):
        e = self.wait_until_present()

        # normalize the input
        if val:
            val = True
        else:
            val = False

        # set the value
        self.logger.info("setting %s to %s" % (self.locators['base'],val))
        if e.is_selected() is not val:
            e.click()


class Link(BasePageWidget):


    def __init__(self, owner, locatordict, onClick=None):
        super(Link,self).__init__(owner, locatordict)
        self.onClick = onClick


    def text(self):
        e = self.wait_until_present()
        return e.text


    def click(self):
        self.logger.info("clicking %s" % (self.locators['base']))
        e = self.wait_until_visible()

        # use action chains to move the mouse to the element
        # this helps us avoid accidentally clicking drop down menus
        # that open up when the mouse moves over them.
        #
        # some elements don't seem to be able to be scrolled into view
        # when using move_to_element_with_offset(e,1,1). in these cases
        # we could fiddle around with the offset to try to get them to
        # work, but its probably just easier to use move_to_element(e)
        # to get to the center of the element and hope it doesnt trigger
        # any popup menus. This is why we catch MoveTargetOutOfBoundsException
        # exceptions and retry the move.

        try:
            self.logger.debug("moving the mouse to element offset")
            ActionChains(self._browser)\
            .move_to_element_with_offset(e,1,1)\
            .perform()
        except MoveTargetOutOfBoundsException:
            self.logger.debug("moving the mouse to element offset failed")
            self.logger.debug("moving the mouse to element center")
            ActionChains(self._browser)\
            .move_to_element(e)\
            .perform()

        e.click()

        # perform "after-click" actions
        if self.onClick is not None:
            return self.onClick()

    def get_attribute(self,attribute):

        e = self.wait_until_present()

        # look for the attribute in this object
        self.logger.debug("looking for attribute in object: %s" % (attribute))
        v = super(Link,self).get_attribute(attribute)

        if v is None:
            # if it is not there, check for the attribute in the
            # anchor tag underneath this element in the HTML DOM
            try:
                self.logger.debug("looking for attribute in anchor tag")
                v = e.find_element_by_css_selector('a')\
                     .get_attribute(attribute)
            except NoSuchElementException:
                pass

        return v


class Radio(BasePageWidget):
    """
        this object has no locatorid or locator,
        all the information is in locatordict
    """


    def __init__(self, owner, locatordict):
        self._values = locatordict
        super(Radio,self).__init__(owner, None)


    def _updateLocators(self):
        self._locvalues = {}
        for (textkey,locatorid) in self._values.items():
            self._locvalues[textkey] = self.owner.locators[locatorid]


    def _checkLocators(self,widgets=None,cltype=''):
        """
            loop through all of the radio buttons
            and check that they are present
        """

        header = "\n===== missing locators in %s =====" % (self.owner.__class__.__name__)
        missing = ''

        for (key,loctext) in self._locvalues.items():
            if self.owner.is_present(locator=loctext) == False:
                locatorid = self._values[key]
                missing += "\n%s: \"%s\"" % (locatorid,loctext)

        if missing != '':
            raise LocatorException(header+missing)


    @property
    def value(self):
        """
            go through each radio button
            check if it has the "checked" attribute
            if it does, send this element's key back
            otherwise return None
        """

        for (key,loctext) in self._locvalues.items():
            e = self.wait_until_present(locator=loctext)
            try:
                c = e.get_attribute('checked')
                if c == 'checked':
                    return key
            except NoSuchAttributeException:
                pass
        return None


    @value.setter
    def value(self, val):
        """
            choose a specific radio button
        """

        loctext = self._locvalues[val]
        self.logger.info("clicking %s" % (loctext))

        e = self.wait_until_visible(locator=loctext)
        e.click()


class Select(BasePageWidget):


    def __init__(self, owner, locatordict):
        super(Select,self).__init__(owner,locatordict)
        self.optionText = []
        self.optionElements = []


    def options(self):
        self.optionText = []
        self.optionElements = []
        select = self.wait_until_present()
        self.optionElements = self.find_elements("css=option",select)
        self.optionText = [o.text for o in self.optionElements]
        return self.optionText


    def choose(self, val):
        # check if the options are populated, if not, populate them
        if (len(self.optionText) == 0) and (len(self.options()) == 0):
            raise ValueError("invalid option: %s" % val)

        index = None

        # if val is an integer, use it as the index
        if isinstance(val,int):
            index = val
        else:
            # the val is a string representing the option to be picked
            # get the index of the requested option
            try:
                index = self.optionText.index(val)
            except:
                self.logger.warn("select option searched: %s" % (val))
                self.logger.warn("select menu options are: %s"
                    % (self.optionText))
                raise

        # select the option
        # index errors will happen here
        self.logger.info("selecting from %s (choice #%d)" % (self.optionText,index))
        self.optionElements[index].click()


    def filter(self, expression):
        def like(x): return re.search(expression,x)
        return filter(like,self.optionText)


    def text(self):
        e = self.wait_until_present()
        return e.text


    def selected(self):
        select = self.wait_until_present()
        o = self.find_element("css=option[selected]",select)
        selectedText = o.text
        self.logger.info("selected item is '%s'" % (selectedText))
        return selectedText


    @property
    def value(self):
        return self.selected()


    @value.setter
    def value(self,val):
        return self.choose(val)


class Text(BasePageWidget):
    """represents typeable <input> elements
       like those with state text or file

       click_focus determins whether the object should
       first click on the element to make sure it is in focus
       before sending keys to it. This is good for elements
       of state text, but will not work for elements of state
       file because clicking the element will popup a file
       browser.
    """

    def __init__(self, owner, locatordict, click_focus=True):
        super(Text,self).__init__(owner,locatordict)
        self.click_focus = click_focus


    @property
    def value(self):
        e = self.wait_until_present()
        return e.get_attribute('value')


    @value.setter
    def value(self, val):
        e = self.wait_until_present()

        if self.click_focus is True:
            # hover mouse over upper left corner of the element
            # we use the action chain to help avoid java script drop down menus
            # that get in the way of us clicking the element. this is especially
            # bad on nees.org
            ActionChains(self._browser)\
            .move_to_element_with_offset(e,0,0)\
            .perform()

            e.click()

        # some elements raise error when we use the clear() function.
        # we could try sending 's but that seems to be troublesome sometimes.
        # send 's is good for example, when clearing a body element
        # within an iframe for the WikiTextArea object.
        # instead of sending individual backspaces,
        # we try to highlight and replace
        e.send_keys(Keys.CONTROL,'a')
        self.logger.info("typing into %s" % (self.locators['base']))
        self.logger.debug("typing '%s' in %s" % (val,self.locators['base']))
        e.send_keys(val)


    def append(self,val):
        self.logger.info("appending into %s" % (self.locators['base']))
        self.logger.debug("appending '%s' in %s" % (val,self.locators['base']))
        # check for presence instead of visibility because some upload buttons
        # use the text widget to fill in the name of the file to be uploaded.
        # in these cases, the element does not seem to be visible, only present.
        e = self.wait_until_present()
        e.send_keys(val)


class TextReadOnly(BasePageWidget):

    @property
    def value(self):
        e = self.wait_until_present()
        return e.text


class TextAC(BasePageWidget):
    # FIXME:
    # most current instances of TextAC need 2 more locators
    # the list element locator for items that have
    # already been typed into the widget:
    #  token-input-token-acm
    # the above element is important for the text() fxn
    # i don't think it will work properly until the
    # correct locator is used.
    # the delete locator for deleting items that have
    # already been typed into the widget:
    #  token-input-delete-token-acm
    """Text input with autocomplete features.

       This class represents a text input that performs autocomplete lookups.
       The user can send a string of characters to a web page element,
       wait for autocomplete to kick in to provide suggestions, and review
       the suggestions. Options from the autocomplete suggestions can also be
       added or deleted from the web page element.

       :Args:
        - owner - parent widget or pageobject
        - locatordict - dictionary mapping internal locator keys to
          owner's locatordict keys

       Notes:
       locatordict is a mapping of keys referenced internally by the object
       to keys on the owner's locatordict. the keys of the owner's locatordict
       should map to a locator string in the owner's dictionary.

       locatordict accepts the following keys:
       base            - key of locator for the input tag without autocomplete
       aclocatorid     - key of locator for the input tag with autocomplete
       choicelocatorid - key of locator for the dropdown menu holding
                         autocomplete choices
       tokenlocatorid  - key of locator used to identify elements already
                         in the autocomplete field.
       deletelocatorid - key of locator used to delete an element already
                         in the autocomplete field. this element should be
                         a child of the element identified by tokenlocatorid.
    """


    def __init__(self, owner, locatordict):
        super(TextAC,self).__init__(owner,locatordict)

        self.acresults = []
        self.acvalues = []


    def send_keys(self, val, timeout=30):
        self.acresults = []
        self.acvalues = []

        # try to use auto-complete functions to populate the input
        e = self.wait_until_visible(locator=self.locators['aclocatorid'])

        # type the value into the field
        self.logger.info("typing into %s" % (self.locators['aclocatorid']))
        self.logger.debug("typing '%s' in %s" % (val,self.locators['aclocatorid']))
        e.send_keys(val)

        # if a non negative timeout was given, return auto-complete suggestions
        if timeout > 0:
            # return the suggestions from auto-complete, if any

            try:
                # wait for the autocomplete to kick in
                self.logger.debug("waiting for autocomplete...")

                def condition(o):
                    choices = o.find_element(self.locators['choicelocator'])
                    e = o.find_elements('css=li',choices)
                    return e

                wait = WebDriverWait(self.owner, timeout)
                self.acvalues = wait.until(condition)

            except TimeoutException:
                # no autocomplete options came up within the timeout
                self.acvalues = []

        # store the text of the elements in a list
        self.acresults = [acvalue.text for acvalue in self.acvalues]
        self.logger.debug("autocomplete returned: '%s'" % (self.acresults))

        # return the list of autocomplete options
        return self.acresults


    def choose(self, val):
        index = self.acresults.index(val)
        self.logger.info("clicking autocomplete option %s (index %d)" % (val,index))
        self.acvalues[index].click()


    def filter(self, expression):
        def like(x): return re.search(expression,x)
        results = filter(like,self.acresults)
        self.logger.debug("filtered results: '%s'" % (results))
        return results


    def text(self):
        t = []
        tokens = self.find_elements(self.locators['tokenlocatorid'])
        for e in tokens:
            tokentext = e.find_element_by_css_selector('p').text
            t.append(tokentext)
        return t


    def remove(self,text):
        """
        remove the token with the specified text
        """

        if not text:
            return

        tokens = self.find_elements(self.locators['tokenlocatorid'])
        for e in tokens:
            tokentext = e.find_element_by_css_selector('p').text
            if text == tokentext:
                # the span is the delete button.
                # find it and click it.
                self.logger.info("deleting autocomplete option %s" % (tokentext))
                delete_button = self.find_element(self.locators['deletelocatorid'],e)
                delete_button.click()


    def remove_all(self):
        """
        remove all tokens from the widget
        """

        # might need to clean out the input field
        # first if a tag is in the middle of being typed
        deleteElements = self.find_elements(self.locators['tokenlocatorid'])
        for e in deleteElements:
            tokentext = e.find_element_by_css_selector('p').text
            self.logger.info("deleting autocomplete option %s" % (tokentext))
            delete_button = self.find_element(self.locators['deletelocatorid'],e)
            delete_button.click()


    @property
    def value(self):

        return self.text()


    @value.setter
    def value(self, val):

        # need to clear the widget first...
        self.remove_all()
        # populate the field without evaluating auto-complete options
        e = self.find_element(self.locators['aclocatorid'])
        if isinstance(val,list):
            for item in val:
                self.logger.info("typing into %s" % (self.locators['aclocatorid']))
                self.logger.debug("typing '%s' into %s" % (item,self.locators['aclocatorid']))
                e.send_keys(item+'\n')
        else:
            self.logger.info("typing into %s" % (self.locators['aclocatorid']))
            self.logger.debug("typing '%s' into %s" % (val,self.locators['aclocatorid']))
            e.send_keys(val+'\n')


class TextArea(Text):

    @property
    def value(self):
        self.wait_until_present()
        e = self.find_element(self.locators['base'])
        return e.text

    @value.setter
    def value(self, val):
        return Text.value.fset(self,val)


class Upload(BasePageWidget):

    def browsefor(self,filename):
        if not filename:
            return
        self.logger.info("typing '%s' into %s" % (filename,self.locators['browselocatorid']))
        browseElement = self.find_element(self.locators['browselocatorid'])
        browseElement.send_keys(filename)


    def upload(self):
        if 'uploadloacatorid' not in self.locators:
            return
        self.logger.info("clicking %s" % (self.locators['uploadlocatorid']))
        uploadElement = self.find_element(self.locators['uploadlocatorid'])
        uploadElement.click()


    @property
    def value(self):
        browseElement = self.find_element(self.locators['browselocatorid'])
        text = browseElement.text
        return text


    @value.setter
    def value(self,filename):
        self.browsefor(filename)
        self.upload()
