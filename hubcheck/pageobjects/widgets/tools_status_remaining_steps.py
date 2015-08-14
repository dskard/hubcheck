from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ToolsStatusRemainingSteps(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ToolsStatusRemainingSteps,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsStatusRemainingSteps_Locators = \
            self.load_class('ToolsStatusRemainingSteps_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusRemainingSteps_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.register           = TextReadOnly(self,{'base':'register'})
        self.upload             = TextReadOnly(self,{'base':'upload'})
        self.upload_done        = Link(self,{'base':'upload_done'})
        self.upload_howto       = Link(self,{'base':'upload_howto'})
        self.toolpage           = TextReadOnly(self,{'base':'toolpage'})
        self.toolpage_create    = Link(self,{'base':'toolpage_create'})
        self.toolpage_preview   = Link(self,{'base':'toolpage_preview'})
        self.toolpage_edit      = Link(self,{'base':'toolpage_edit'})
        self.test_approve       = TextReadOnly(self,{'base':'test_approve'})
        self.approve_it         = Link(self,{'base':'approve_it'})
        self.updated_approve    = Link(self,{'base':'updated_approve'})
        self.publish            = TextReadOnly(self,{'base':'publish'})
        self.updated_publish    = Link(self,{'base':'updated_publish'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsRegistered(self,widgets=None,cltype='Registered'):

        widgets = [self.register, self.upload, self.toolpage,
                   self.test_approve, self.publish]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsCreated(self,widgets=None,cltype='Created'):

        widgets = [self.register, self.upload, self.toolpage,
                   self.test_approve, self.publish]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsUploaded(self,widgets=None,cltype='Uploaded'):

        widgets = [self.register, self.upload, self.toolpage,
                   self.test_approve, self.publish]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsInstalled(self,widgets=None,cltype='Installed'):

        widgets = [self.register, self.upload, self.toolpage,
                   self.test_approve, self.updated_approve, self.publish]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsApproved(self,widgets=None,cltype='Approved'):

        widgets = [self.register, self.upload, self.toolpage,
                   self.test_approve, self.publish, self.updated_publish]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsToolPageCreate(self,widgets=None,cltype='ToolPageCreate'):

        widgets = [self.toolpage_create]
        return self._checkLocators(widgets,cltype)


    def _checkLocatorsToolPageCreated(self,widgets=None,cltype='ToolPageCreated'):

        widgets = [self.toolpage_preview, self.toolpage_edit]
        return self._checkLocators(widgets,cltype)


    def _get_status(self,w):

        obj = getattr(self,w)
        class_attrs = obj.get_attribute('class').split()
        for status in ['incomplete','complete','todo']:
            if status in class_attrs:
                break
        else:
            status = None
        return status


    def get_register_status(self):

        return self._get_status('register')


    def get_upload_status(self):

        return self._get_status('upload')


    def get_toolpage_status(self):

        return self._get_status('toolpage')


    def get_test_approve_status(self):

        return self._get_status('test_approve')


    def get_publish_status(self):

        return self._get_status('publish')


    def goto_toolpage_create(self):

        return self.toolpage_create.click()


    def goto_toolpage_preview(self):

        return self.toolpage_preview.click()


    def goto_toolpage_edit(self):

        return self.toolpage_edit.click()


    def goto_upload_done(self):

        return self.upload_done.click()


    def goto_upload_howto(self):

        return self.upload_howto.click()


    def goto_approve_tool(self):

        return self.approve_it.click()


    def goto_installed_update_tool(self):

        return self.updated_approve.click()


    def goto_approved_update_tool(self):

        return self.updated_publish.click()



class ToolsStatusRemainingSteps_Locators_Base(object):
    """locators for ToolsStatusRemainingSteps object"""

    locators = {
        'base'              : "css=#whatsnext",
        'register'          : "css=#whatsnext ul li:nth-of-type(1)",
        'upload'            : "css=#whatsnext ul li:nth-of-type(2)",
        'upload_done'       : "css=#Uploaded_ .flip",
        'upload_howto'      : "css=#whatsnext ul li:nth-of-type(2) > a.developer-wiki",
        'toolpage'          : "css=#whatsnext ul li:nth-of-type(3)",
        'toolpage_create'   : "css=#whatsnext .create-resource",
        'toolpage_preview'  : "css=#whatsnext .preview-resource",
        'toolpage_edit'     : "css=#whatsnext .edit-resource",
        'test_approve'      : "css=#whatsnext ul li:nth-of-type(4)",
        'approve_it'        : "css=#Approved_ .flip",
        'updated_approve'   : "css=#Updated_ .flip",
        'publish'           : "css=#whatsnext ul li:nth-of-type(5)",
        'updated_publish'   : "css=#Updated .flip",
    }
