from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.exceptions import NoSuchUserException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ToolSessionShare(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolSessionShare,self).__init__(owner,locatordict)

        # load hub's classes
        ToolSessionShare_Locators = self.load_class('ToolSessionShare_Locators')
        ToolSessionSharedWithItem = self.load_class('ToolSessionSharedWithItem')
        ItemList = self.load_class('ItemList')

        # update this object's locator
        self.locators.update(ToolSessionShare_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name = TextAC(self,{'base':'name',
                                 'aclocatorid':'nameac',
                                 'choicelocatorid':'nameacchoices',
                                 'tokenlocatorid':'nameactoken',
                                 'deletelocatorid':'nameacdelete'})
        self.group = Select(self,{'base':'group'})
        self.read_only = Checkbox(self,{'base':'readonly'})
        self.share = Button(self,{'base':'share'})
        self.share_list = ItemList(self,
                                {
                                    'base' : 'listbase',
                                    'row'  : 'item',
                                }, ToolSessionSharedWithItem,
                                {})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def share_session_with(self,sharelist=None,group=None,readonly=False):

        # we don't handle cases where no sharelist or group is provided
        if sharelist is None and group is None:
            return

        if sharelist is not None:
            self.name.value = sharelist
        if group is not None:
            self.group.value = group
        self.read_only.value = readonly
        self.share.click()

        self.wait_for_overlay("waiting for session to be shared")


    def get_shared_with(self):

        shared_with = []

        try:
            for item in self.share_list:
                shared_with.append(item.name.text())
        except TimeoutException:
            pass

        return shared_with


    def disconnect(self,user):

        if  self.share_list.num_rows() == 0:
            msg = 'Could not find matching connected user: {0}'.format(user)
            raise NoSuchUserException(msg)

        item = self.share_list.get_row_by_property('name',user)

        if item is None:
            # try a little harder to find the row
            # see if any row's name property contain user
            compare = lambda x,y: y in x
            item = self.share_list.get_row_by_property('name',user,compare)
            if item is None:
                msg = 'Could not find matching connected user: {0}'.format(user)
                raise NoSuchUserException(msg)

        item.disconnect.click()
        self.wait_for_overlay("waiting for session to be disconnected")


    def disconnect_all(self):

        # deleteing rows messes up the internal count of the share_list
        # as we disconnect, we grab the next item at the top.

        for count in xrange(self.share_list.num_rows()):
            item = self.share_list.get_row_by_position(0)
            item.disconnect.click()
            self.wait_for_overlay("waiting for session to be disconnected")


    def wait_for_overlay(self,message=None):
        """let the share overlay flash on the screen
        """

        loctype,loctext = self._po._split_locator(self.locators['shareoverlay'])
        WebDriverWait(self._browser,10).until(
            EC.visibility_of_element_located((loctype,loctext)),
            message=message)
        WebDriverWait(self._browser,10).until_not(
            EC.visibility_of_element_located((loctype,loctext)),
            message=message)


class ToolSessionShare_Locators_Base(object):
    """locators for ToolSessionShare object"""

    locators = {
        'base'              : "css=#app-wrap",
        'name'              : "css=#acmembers",
        'nameac'            : "css=#token-input-acmembers",
        'nameacchoices'     : "css=.token-input-dropdown-acm",
        'nameactoken'       : "css=.token-input-token-acm",
        'nameacdelete'      : "css=.token-input-delete-token-acm",
        'group'             : "css=#group",
        'readonly'          : "css=#readonly",
        'share'             : "css=#share-btn",
        'listbase'          : "css=.entries",
        'item'              : "css=.entries tbody tr .entry-title",
        'sharedwith'        : "xpath=//*[contains(@class,'entries')]//a[contains(text(),'{name}')]",
        'shareoverlay'      : "css=#app-share-overlay",
    }

