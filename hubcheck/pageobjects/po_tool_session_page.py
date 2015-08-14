from hubcheck.pageobjects.po_generic_page import GenericPage

class ToolSessionPage(GenericPage):
    """tools session page for running simulation tools"""

    def __init__(self,browser,catalog,toolname=None,session_number=None):
        super(ToolSessionPage,self).__init__(browser,catalog)
        if toolname is not None and session_number is not None:
            self.path = "/tools/%s/session?sess=%d" % (toolname,session_number)
        else:
            self.path = "/"

        # load hub's classes
        ToolSessionPage_Locators = self.load_class('ToolSessionPage_Locators')
        ToolSessionApp = self.load_class('ToolSessionApp')
        ToolSessionShare = self.load_class('ToolSessionShare')
        # ToolSessionManager = self.load_class('ToolSessionManager')

        # update this object's locator
        self.locators.update(ToolSessionPage_Locators.locators)

        # setup page object's components
        self.app = ToolSessionApp(self,{'base':'app'})
        self.share = ToolSessionShare(self,{'base':'share'})
        #self.manager = ToolSessionManager(self,{'base':'manager'})


    def do_terminate(self):

        return self.app.do_terminate()


    def do_keep(self):

        return self.app.do_keep()


    def do_popout(self):

        return self.app.do_popout()


    def do_refresh(self):

        return self.app.do_refresh()


    def get_session_number(self):

        return self.app.get_session_number()


class ToolSessionPage1(ToolSessionPage):
    """hubzero version 1.1.0 tool session page for running simulation tools

       updated page url
    """

    def __init__(self,browser,catalog,toolname=None,session_number=None):
        super(ToolSessionPage1,self).__init__(browser,catalog)
        if toolname is not None and session_number is not None:
            self.path = "/tools/%s/session/%d" % (toolname,session_number)
        else:
            self.path = "/"


class ToolSessionPage2(ToolSessionPage):
    """hubzero version 1.1.2 tool session page for running simulation tools

       updated page url
    """

    def __init__(self,browser,catalog,toolname=None,session_number=None):
        super(ToolSessionPage2,self).__init__(browser,catalog)
        if toolname is not None and session_number is not None:
            self.path = "/tools/%s/session?sess=%d" % (toolname,session_number)
        else:
            self.path = "/"


class ToolSessionPage_Locators_Base(object):
    """locators for ToolSessionPage object"""

    locators = {
        'app'               : "css=#app-wrap",
        'share'             : "css=#app-share",
        'manager'           : "css=#app-manager",
    }
