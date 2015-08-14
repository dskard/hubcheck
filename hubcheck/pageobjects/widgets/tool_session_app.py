from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link, Text, TextReadOnly

class ToolSessionApp(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolSessionApp,self).__init__(owner,locatordict)

        # load hub's classes
        ToolSessionApp_Locators = self.load_class('ToolSessionApp_Locators')
        ToolSessionAppStorage = self.load_class('ToolSessionAppStorage')

        # update this object's locator
        self.locators.update(ToolSessionApp_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title      = Text(self,{'base':'title'})
        self.terminate  = Link(self,{'base':'terminate'})
        self.keep       = Link(self,{'base':'keep'})
        self.storage    = ToolSessionAppStorage(self,{'base':'storage'})
        self.popout     = Link(self,{'base':'popout'})
        self.refresh    = Link(self,{'base':'refresh'})
        self.resize     = Link(self,{'base':'resize'})
        self.size       = TextReadOnly(self,{'base':'size'})

        # update the component's locators with this objects overrides
        self._updateLocators()


#    def set_title(self):
#
#        # requires clicking on the title element to expose the underlying text widget.
#

    def do_terminate(self):

        self.terminate.click()


    def do_keep(self):

        self.keep.click()


    def do_popout(self):

        self.popout.click()


    def do_refresh(self):

        self.refresh.click()


#    def do_resize(self):
#
#        # requires click and drag to a location on the screen
#        self.resize.click()
#

    def get_session_number(self):

        title_ele = self.find_element_in_owner(self.locators['title'])
        session_number = int(title_ele.get_attribute('rel'))
        return session_number


class ToolSessionApp_Locators_Base(object):
    """locators for ToolSessionApp object"""

    locators = {
        'base'              : "css=#app-wrap",
        'title'             : "css=#session-title",
        'terminate'         : "css=#app-btn-close",
        'keep'              : "css=#app-btn-keep",
        'storage'           : "css=#diskusage",
        'popout'            : "css=#app-btn-newwindow",
        'refresh'           : "css=#app-btn-refresh",
        'resize'            : "css=#app-btn-resizehandle",
        'size'              : "css=#app-size",
    }

