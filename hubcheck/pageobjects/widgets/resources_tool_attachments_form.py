from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Upload
from hubcheck.pageobjects.widgets.item_list import ItemList

class ResourcesToolAttachmentsForm(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(ResourcesToolAttachmentsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesToolAttachmentsForm_Locators = \
            self.load_class('ResourcesToolAttachmentsForm_Locators')
        ResourcesToolFileUploadRow = \
            self.load_class('ResourcesToolFileUploadRow')
        ResourcesToolScreenshotUploadRow = \
            self.load_class('ResourcesToolScreenshotUploadRow')
        Upload3 = self.load_class('Upload3')

        # update this object's locator
        self.locators.update(ResourcesToolAttachmentsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
#        self.documents_upload = IframeWrap(
#                                    Upload(self,
#                                        {'browselocatorid':'doc_browse',
#                                         'uploadlocatorid':'doc_upload',}),
#                                    ['doc_upload_frame'])
#
#        self.documents_list = IframeWrap(['doc_upload_frame']
#                                ItemList, {'base':'doc_list',
#                                           'row':'doc_list_row'},
#                                IframeWrap, {'base':'doc_upload_frame'},
#                                ResourcesToolFileUploadRow, {})

        self.documents = Upload3(self,{'uploadframe':'doc_upload_frame',
                                       'browse':'doc_browse',
                                       'upload':'doc_upload',
                                       'fileframe':'doc_list_frame',
                                       'uploadlist':'doc_list',
                                       'uploadlistrow':'doc_list_row'},
                                 ResourcesToolFileUploadRow,{})

        self.screenshots = Upload3(self,{'uploadframe':'screenshot_upload_frame',
                                         'browse':'screenshot_browse',
                                         'upload':'screenshot_upload',
                                         'fileframe':'screenshot_list_frame',
                                         'uploadlist':'screenshot_list',
                                         'uploadlistrow':'screenshot_list_row'},
                                   ResourcesToolScreenshotUploadRow,{})


#        self.screenshot_upload = IframeWrap(self,
#                                   {'base':'screenshot_upload_frame'},
#                                   Upload,
#                                   {'browselocatorid':'screenshot_browse',
#                                    'uploadlocatorid':'screenshot_upload',})
#
#        self.screenshot_list = IframeWrap(self,
#                                 {'base':'screenshot_upload_frame'},
#                                 ItemList,
#                                 {'base':'screenshot_list',
#                                  'row':'screenshot_list_row'},
#                                 IframeWrap,
#                                 {'base':'screenshot_upload_frame'},
#                                 ResourcesToolScreenshotUploadRow, {})

        self.top_previous   = Button(self,{'base':'top_previous'})
        self.top_submit     = Button(self,{'base':'top_submit'})
        self.previous       = Button(self,{'base':'previous'})
        self.submit         = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def upload_files(self,flist):
        """upload the files in the list flist"""

        for fname in flist:
            self.documents_upload.value = fname


    def get_uploaded_files(self):
        """return the list of uploaded files"""

        fnames = []

        for row in self.documents_list:
            fnames.append(row.value['name'])

        return fnames


    def delete_file(self,filename):
        """delete an uploaded file"""

        for row in self.documents_list:
            if row.value['name'] == filename:
                row.delete.click()


    def submit_form(self,flist):
        """upload and attach the list of files in flist"""

        self.upload_files(flist)
        return self.submit.click()


class ResourcesToolAttachmentsForm_Locators_Base(object):
    """locators for ResourcesToolAttachmentsForm object"""


    locators = {
        'base'                    : "css=#hubForm",
        'top_previous'            : "css=#hubForm div:nth-of-type(1) .returntoedit",
        'top_submit'              : "css=#hubForm div:nth-of-type(1) [type='submit']",
        'doc_upload_frame'        : "css=#attaches",
        'doc_browse'              : "css=#upload",
        'doc_upload'              : "css=#attachments-form [type='submit']",
        'doc_list_frame'          : None,
        'doc_list'                : "css=.list",
        'doc_list_row'            : "css=.list tr",
        'screenshot_upload_frame' : "css=#screens",
        'screenshot_browse'       : "css=#screenshots-form [name='upload']",
        'screenshot_upload'       : "css=#screenshots-form [type='submit']",
        'screenshot_list_frame'   : None,
        'screenshot_list'         : "css=.screenshots",
        'screenshot_list_row'     : "css=.screenshots li:nth-of-type(2*{row_num}-1)",
        'screenshot_switch'       : "css=.screenshots li:nth-of-type(2*{row_num})",
        'previous'                : "css=#hubForm div:nth-of-type(8) .returntoedit",
        'submit'                  : "css=#hubForm div:nth-of-type(8) [type='submit']",
    }
