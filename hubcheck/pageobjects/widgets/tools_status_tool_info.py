from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class ToolsStatusToolInfo(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusToolInfo,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusToolInfo_Locators = self.load_class('ToolsStatusToolInfo_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusToolInfo_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.edit               = Link(self,{'base':'edit'})
        self.title              = TextReadOnly(self,{'base':'title'})
        self.version            = TextReadOnly(self,{'base':'version'})
        self.glance             = TextReadOnly(self,{'base':'glance'})
        self.toolpage_preview   = Link(self,{'base':'toolpage_preview'})
        self.toolpage_edit      = Link(self,{'base':'toolpage_edit'})
        self.vncgeometry        = TextReadOnly(self,{'base':'vncgeometry'})
        self.toolaccess         = TextReadOnly(self,{'base':'toolaccess'})
        self.codeaccess         = TextReadOnly(self,{'base':'codeaccess'})
        # self.codeaccesslink     = Link(self,{'base':'codeaccesslink'})
        self.wikiaccess         = TextReadOnly(self,{'base':'wikiaccess'})
        self.devteam            = TextReadOnly(self,{'base':'devteam'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_edit(self):

        self.edit.click()


    def get_title(self):

        return self.title.value


    def get_version(self):

        return self.version.value


    def get_glance(self):

        return self.glance.value


    def goto_toolpage_preview(self):

        self.toolpage_preview.click()


    def goto_toolpage_edit(self):

        self.toolpage_edit.click()


    def get_vncgeometry(self):

        return self.vncgeometry.value


    def get_toolaccess(self):

        return self.toolaccess.value


    def get_codeaccess(self):

        return self.codeaccess.value


    def get_wikiaccess(self):

        return self.wikiaccess.value


    def get_devteam(self):

        return self.devteam.value


class ToolsStatusToolInfo_Locators_Base(object):
    """locators for ToolsStatusToolInfo object"""

    locators = {
        'base'              : "css=#toolstatus",
        'edit'              : "css=#toolstatus .edit",
        'title'             : "css=#toolstatus tr:nth-of-type(2) td",
        'version'           : "css=#toolstatus tr:nth-of-type(3) td",
        'glance'            : "css=#toolstatus tr:nth-of-type(4) td",
        'toolpage_preview'  : "link=Preview",
        'toolpage_edit'     : "link=Edit description page",
        'vncgeometry'       : "css=#toolstatus tr:nth-of-type(6) td",
        'toolaccess'        : "css=#toolstatus tr:nth-of-type(7) td",
        'codeaccess'        : "css=#toolstatus tr:nth-of-type(8) td",
        'wikiaccess'        : "css=#toolstatus tr:nth-of-type(9) td",
        'devteam'           : "css=#toolstatus tr:nth-of-type(10) td",
    }
