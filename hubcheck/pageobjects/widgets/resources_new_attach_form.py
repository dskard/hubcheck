from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Upload
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class ResourcesNewAttachForm(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(ResourcesNewAttachForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewAttachForm_Locators = self.load_class('ResourcesNewAttachForm_Locators')
        UploadList1 = self.load_class('UploadList1')

        # update this object's locator
        self.locators.update(ResourcesNewAttachForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.upload         = IframeWrap(
                                Upload(self,{'browselocatorid':'browse',
                                             'uploadlocatorid':'upload',}),
                                ['uploadframe'])
        self.uploadlist     = UploadList1(self,{'base':'iframe'})

        self.submit         = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def upload_files(self,flist):
        """upload the files in the list flist"""

        for fname in flist:
            self.upload.value = fname


    def get_uploaded_files(self):
        """return the list of uploaded files"""

        return self.uploadlist.get_uploaded_files()


    def delete_file(self,filename):
        """delete an uploaded file"""

        return self.uploadlist.delete_file(filename)


    def submit_form(self,flist):
        """upload and attach the list of files in flist"""

        self.upload_files(flist)
        return self.submit.click()


class ResourcesNewAttachForm_Locators_Base(object):
    """locators for ResourcesNewAttachForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'browse'            : "css=[name='upload']",
        'upload'            : "css=[type='submit']",
        'uploadframe'       : "css=#attaches",
        'submit'            : "css=#hubForm [type='submit']",
    }
