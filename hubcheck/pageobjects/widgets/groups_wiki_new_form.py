from hubcheck.pageobjects.widgets.form_base import PreviewFormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap


class GroupsWikiNewForm1(PreviewFormBase):
    """
    GroupsWikiNewForm with TextArea widget for pagetext
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiNewForm1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiNewForm_Locators = self.load_class('GroupsWikiNewForm_Locators')
        Upload = self.load_class('Upload2')
        UploadList2 = self.load_class('UploadList2')

        # update this object's locator
        self.locators.update(GroupsWikiNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.parent         = Select(self,{'base':'parent'})
        self.templates      = Select(self,{'base':'templates'})
        self.title          = Text(self,{'base':'title'})
        self.pagetext       = TextArea(self,{'base':'pagetext'})
        self.upload         = Upload(self,{'base':'upload'})
        self.uploadlist     = UploadList2(self,{'base':'uploadlist'})
        self.access         = Select(self,{'base':'access'})
        self.authors        = TextAC(self,{'base':'authors',
                                           'aclocatorid':'authorsac',
                                           'choicelocatorid':'authorsacchoices',
                                           'tokenlocatorid':'authorsactoken',
                                           'deletelocatorid':'authorsacdelete'})
        self.hideauthors    = Checkbox(self,{'base':'hideauthors'})
        self.allowchanges   = Checkbox(self,{'base':'allowchanges'})
        self.allowcomments  = Checkbox(self,{'base':'allowcomments'})
        self.lockpage       = Checkbox(self,{'base':'lockpage'})
        self.tags           = TextAC(self,{'base':'tags',
                                           'aclocatorid':'tagsac',
                                           'choicelocatorid':'tagsacchoices',
                                           'tokenlocatorid':'tagsactoken',
                                           'deletelocatorid':'tagsacdelete'})
        self.summary        = Text(self,{'base':'summary'})

        self.fields = ['parent','templates','title','pagetext','upload',
                       'access','authors','hideauthros','allowchanges',
                       'allowcomments','lockpage','tags','summary']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def create_wiki_page(self, data):
        """create a new wiki page based on setting in data"""

        self.populate_form(data)
        self.submit_form()


    def get_uploaded_files(self):
        """return a list of files uploaded to the wiki page"""

        return self.uploadlist.get_uploaded_files()


    def delete_file(self,filename):
        """delete a file uploaded to the wiki page"""

        return self.uploadlist.delete_file(filename)


class GroupsWikiNewForm1_Locators_Base(object):
    """locators for GroupsWikiNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'parent'            : "css=#parent",
        'templates'         : "css=#templates",
        'title'             : "css=#title",
        'pagetext'          : "css=#pagetext",
        'upload'            : "css=#file-uploader",
        'uploadlist'        : "css=#file-uploader-list",
        'access'            : "css=#params_mode",
        'authors'           : "css=#params_authors",
        'authorsac'         : "css=#token-input-params_authors",
        'authorsacchoices'  : "css=.token-input-dropdown-acm",
        'authorsactoken'    : "css=.token-input-token-acm",
        'authorsacdelete'   : "css=.token-input-delete-token-acm",
        'hideauthors'       : "css=#params_hide_authors",
        'allowchanges'      : "css=#params_allow_changes",
        'allowcomments'     : "css=#params_allow_comments",
        'lockpage'          : "css=#state",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'summary'           : "css=#hubForm input[name='revision[summary]']",
        'preview'           : "css=#hubForm [name='preview']",
        'submit'            : "css=#hubForm [name='submit']",
    }


class GroupsWikiNewForm2(PreviewFormBase):
    """
    GroupsWikiNewForm that embeds the pagetext inside of an iframe
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiNewForm2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiNewForm_Locators = self.load_class('GroupsWikiNewForm_Locators')
        Upload = self.load_class('Upload2')
        UploadList2 = self.load_class('UploadList2')

        # update this object's locator
        self.locators.update(GroupsWikiNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.parent         = Select(self,{'base':'parent'})
        self.templates      = Select(self,{'base':'templates'})
        self.title          = Text(self,{'base':'title'})
        self.pagetext       = IframeWrap(TextArea(self,{'base':'pagetext'}),
                                         ['pagetextframe'])
        self.upload         = Upload(self,{'base':'upload'})
        self.uploadlist     = UploadList2(self,{'base':'uploadlist'})
        self.access         = Select(self,{'base':'access'})
        self.authors        = TextAC(self,{'base':'authors',
                                           'aclocatorid':'authorsac',
                                           'choicelocatorid':'authorsacchoices',
                                           'tokenlocatorid':'authorsactoken',
                                           'deletelocatorid':'authorsacdelete'})
        self.hideauthors    = Checkbox(self,{'base':'hideauthors'})
        self.allowchanges   = Checkbox(self,{'base':'allowchanges'})
        self.allowcomments  = Checkbox(self,{'base':'allowcomments'})
        self.lockpage       = Checkbox(self,{'base':'lockpage'})
        self.tags           = TextAC(self,{'base':'tags',
                                           'aclocatorid':'tagsac',
                                           'choicelocatorid':'tagsacchoices',
                                           'tokenlocatorid':'tagsactoken',
                                           'deletelocatorid':'tagsacdelete'})
        self.summary        = Text(self,{'base':'summary'})

        self.fields = ['parent','templates','title','pagetext','upload',
                       'access','authors','hideauthros','allowchanges',
                       'allowcomments','lockpage','tags','summary']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def create_wiki_page(self, data):
        """create a new wiki page based on setting in data"""

        self.populate_form(data)
        self.submit_form()


    def get_uploaded_files(self):
        """return a list of files uploaded to the wiki page"""

        return self.uploadlist.get_uploaded_files()


    def delete_file(self,filename):
        """delete a file uploaded to the wiki page"""

        return self.uploadlist.delete_file(filename)


class GroupsWikiNewForm2_Locators_Base(object):
    """locators for GroupsWikiNewForm2 object"""

    locators = {
        'base'              : "css=#hubForm",
        'parent'            : "css=#parent",
        'templates'         : "css=#templates",
        'title'             : "css=#title",
        'pagetext'          : "css=body",
        'pagetextframe'     : "css=label[for='pagetext'] iframe",
        'upload'            : "css=#file-uploader",
        'uploadlist'        : "css=#file-uploader-list",
        'access'            : "css=#params_mode",
        'authors'           : "css=#params_authors",
        'authorsac'         : "css=#token-input-params_authors",
        'authorsacchoices'  : "css=.token-input-dropdown-acm",
        'authorsactoken'    : "css=.token-input-token-acm",
        'authorsacdelete'   : "css=.token-input-delete-token-acm",
        'hideauthors'       : "css=#params_hide_authors",
        'allowchanges'      : "css=#params_allow_changes",
        'allowcomments'     : "css=#params_allow_comments",
        'lockpage'          : "css=#state",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'summary'           : "css=#hubForm input[name='revision[summary]']",
        'preview'           : "css=#hubForm [name='preview']",
        'submit'            : "css=#hubForm [name='submit']",
    }


class GroupsWikiNewForm3(PreviewFormBase):
    """
    GroupsWikiNewForm
        TextArea widget for pagetext
        Upload3 file upload widget with embedded iframes
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiNewForm3,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiNewForm_Locators = self.load_class('GroupsWikiNewForm_Locators')
        Upload = self.load_class('Upload3')
        UploadListRow = self.load_class('UploadListRow')

        # update this object's locator
        self.locators.update(GroupsWikiNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.parent         = Select(self,{'base':'parent'})
        self.templates      = Select(self,{'base':'templates'})
        self.title          = Text(self,{'base':'title'})
        self.pagetext       = TextArea(self,{'base':'pagetext'})

        self.upload         = Upload(self,{'base':'fileuploader',
                                           'uploadframe':'uploadframe',
                                           'browse':'browse',
                                           'upload':'upload',
                                           'fileframe':'fileframe',
                                           'uploadlist':'uploadlist',
                                           'uploadlistrow':'uploadlistrow'},
                                     UploadListRow,{})

        self.access         = Select(self,{'base':'access'})
        self.authors        = TextAC(self,{'base':'authors',
                                           'aclocatorid':'authorsac',
                                           'choicelocatorid':'authorsacchoices',
                                           'tokenlocatorid':'authorsactoken',
                                           'deletelocatorid':'authorsacdelete'})
        self.hideauthors    = Checkbox(self,{'base':'hideauthors'})
        self.allowchanges   = Checkbox(self,{'base':'allowchanges'})
        self.allowcomments  = Checkbox(self,{'base':'allowcomments'})
        self.lockpage       = Checkbox(self,{'base':'lockpage'})
        self.tags           = TextAC(self,{'base':'tags',
                                           'aclocatorid':'tagsac',
                                           'choicelocatorid':'tagsacchoices',
                                           'tokenlocatorid':'tagsactoken',
                                           'deletelocatorid':'tagsacdelete'})
        self.summary        = Text(self,{'base':'summary'})

        self.fields = ['parent','templates','title','pagetext','upload',
                       'access','authors','hideauthros','allowchanges',
                       'allowcomments','lockpage','tags','summary']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def create_wiki_page(self, data):
        """create a new wiki page based on setting in data"""

        self.populate_form(data)
        self.submit_form()


    def get_uploaded_files(self):
        return self.upload.get_uploaded_files()


    def delete_file(self,filename):
        return self.upload.delete_file(filename)


class GroupsWikiNewForm3_Locators_Base(object):
    """locators for GroupsWikiNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'parent'            : "css=#parent",
        'templates'         : "css=#templates",
        'title'             : "css=#title",
        'pagetext'          : "css=#pagetext",

        'fileuploader'      : "css=#file-uploader",
        'uploadframe'       : "css=#filer",
        'browse'            : "css=#upload",
        'upload'            : "css=#adminForm input[type='submit']",
        'fileframe'         : "css=#imgManager",
        'uploadlist'        : "css=#filelist",
        'uploadlistrow'     : "css=#filelist tr",

        'access'            : "css=#params_mode",
        'authors'           : "css=#params_authors",
        'authorsac'         : "css=#token-input-params_authors",
        'authorsacchoices'  : "css=.token-input-dropdown-acm",
        'authorsactoken'    : "css=.token-input-token-acm",
        'authorsacdelete'   : "css=.token-input-delete-token-acm",
        'hideauthors'       : "css=#params_hide_authors",
        'allowchanges'      : "css=#params_allow_changes",
        'allowcomments'     : "css=#params_allow_comments",
        'lockpage'          : "css=#state",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'summary'           : "css=#hubForm input[name='revision[summary]']",
        'preview'           : "css=#hubForm [name='preview']",
        'submit'            : "css=#hubForm [name='submit']",
    }


