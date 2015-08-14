from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

class ToolsStatusApproveToolInfoForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusApproveToolInfoForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusApproveToolInfoForm_Locators = \
            self.load_class('ToolsStatusApproveToolInfoForm_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusApproveToolInfoForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tool_info          = Link(self,{'base':'tool_info'})
        self.title              = TextReadOnly(self,{'base':'title'})
        self.version            = TextReadOnly(self,{'base':'version'})
        self.version_edit       = Link(self,{'base':'version_edit'})
        self.description        = TextReadOnly(self,{'base':'description'})
        self.tool_access        = TextReadOnly(self,{'base':'tool_access'})
        self.code_access        = TextReadOnly(self,{'base':'code_access'})
        self.project_access     = TextReadOnly(self,{'base':'project_access'})
        self.screen_size        = TextReadOnly(self,{'base':'screen_size'})
        self.developers         = TextReadOnly(self,{'base':'developers'})
        self.authors            = TextReadOnly(self,{'base':'authors'})
        self.resource_preview   = Link(self,{'base':'resource_preview'})
        self.license_edit       = Link(self,{'base':'license_edit'})
        self.license            = TextReadOnly(self,{'base':'license'})
        self.approve            = Button(self,{'base':'approve'})


        # update the component's locators with this objects overrides
        self._updateLocators()


    def edit_tool_info(self):
        """
        edit the tool's information
        """

        self.tool_info.click()


    def edit_version(self):
        """
        edit the tool's version
        """

        self.version.click()


    def preview_resource_page(self):
        """
        navigate to the resource page preview
        """

        self.resource_preview.click()


    def edit_license(self):
        """
        edit the tool license
        """

        self.license_edit.click()


    def value(self):
        """
        return a summary of the widget
        """

        v = {'title' : self.title.value,
             'version' : self.version.value,
             'description' : self.description.value,
             'tool_access' : self.tool_access.value,
             'source_access' : self.source_access.value,
             'project_access' : self.project_access.value,
             'screen_size' : self.screen_size.value,
             'developers' : self.developers.value,
             'authors' : self.authors.value,
             'license' : self.license.value,
            }

        return v


    def approve_tool(self):
        """
        approve the tool's version, license, and info.
        """

        self.approve.click()


class ToolsStatusApproveToolInfoForm_Locators_Base(object):
    """locators for ToolsStatusApproveToolInfoForm object"""

    locators = {
        'base'             : "css=#versionForm",
        'tool_info'        : "css=.edit",
        'title'            : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(1) .desc",
        'version'          : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(2) .desc",
        'version_edit'     : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(2) .actionlink a",
        'description'      : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(3) .desc",
        'tool_access'      : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(4) .desc",
        'code_access'      : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(5) .desc",
        'project_access'   : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(6) .desc",
        'screen_size'      : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(7) .desc",
        'developers'       : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(8) .desc",
        'authors'          : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(9) .desc",
        'resource_preview' : "css=#versionForm .grid div:nth-of-type(1) p:nth-of-type(10) a",
        'license_edit'     : "css=#versionForm .grid div:nth-of-type(2) .actionlink a",
        'license'          : "css=#versionForm .grid div:nth-of-type(2) .licensetxt",
        'approve'          : "css=#versionForm [type='submit']",
    }
