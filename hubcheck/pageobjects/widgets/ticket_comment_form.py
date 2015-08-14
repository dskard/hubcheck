from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Upload
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox

class TicketCommentForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(TicketCommentForm,self).__init__(owner,locatordict)

        # load hub's classes
        TicketCommentForm_Locators = self.load_class('TicketCommentForm_Locators')

        # update this object's locator
        self.locators.update(TicketCommentForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tags            = TextAC(self,{'base':'tags',
                                            'aclocatorid':'tagsac',
                                            'choicelocatorid':'tagsacchoices',
                                            'tokenlocatorid':'tagsactoken',
                                            'deletelocatorid':'tagsacdelete'})
        self.group           = TextAC(self,{'base':'group',
                                            'aclocatorid':'groupac',
                                            'choicelocatorid':'groupacchoices',
                                            'tokenlocatorid':'groupactoken',
                                            'deletelocatorid':'groupacdelete'})
        self.assignee        = Select(self,{'base':'assignee'})
        self.severity        = Select(self,{'base':'severity'})
        self.status          = Select(self,{'base':'statusdd'})
        self.messages        = Select(self,{'base':'messages'})
        self.private         = Checkbox(self,{'base':'private'})
        self.comment         = TextArea(self,{'base':'comment'})
        self.upload          = Upload(self,{'browselocatorid':'upload'})
        self.desc            = Text(self,{'base':'desc'})
        self.mailsubmitter   = Checkbox(self,{'base':'mailsubmitter'})
        self.mailowner       = Checkbox(self,{'base':'mailowner'})
        self.cc              = TextAC(self,{'base':'cc',
                                            'aclocatorid':'ccac',
                                            'choicelocatorid':'ccacchoices',
                                            'tokenlocatorid':'ccactoken',
                                            'deletelocatorid':'ccacdelete'})

        self.fields = ['tags', 'groups', 'assignee', 'severity', 'status',
                       'messages', 'private', 'comment', 'upload', 'desc',
                       'mailsubmitter', 'mailowner', 'cc']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsTicketOwner(self,widgets=None,cltype='TicketOwner'):

        widgets = [self.status,self.comment,self.upload,self.desc,self.submit]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsTicketCommenter(self,widgets=None,cltype='TicketCommenter'):

        self._checkLocators(widgets,cltype)


    def add_comment(self,data):

        self.submit_form(data)


    def get_status(self):

        return self.status.value


class TicketCommentForm_Locators_Base(object):
    """locators for TicketCommentForm object"""

    locators = {
        'base'           : "css=#commentform",
        'tags'           : "css=#actags",
        'tagsac'         : "css=#token-input-actags",
        'tagsacchoices'  : "css=.token-input-dropdown-act",
        'tagsactoken'    : "css=.token-input-token-act",
        'tagsacdelete'   : "css=.token-input-delete-token-act",
        'group'          : "css=#acgroup",
        'groupac'        : "css=#token-input-acgroup",
        'groupacchoices' : "css=.token-input-dropdown-acg",
        'groupactoken'   : "css=.token-input-token-acg",
        'groupacdelete'  : "css=.token-input-delete-token-acg",
        'assignee'       : "css=#ticketowner",
        'severity'       : "css=[id='ticket[severity]']",
        'statusdd'       : "css=#status",
        'messages'       : "css=#messages",
        'private'        : "css=#make-private",
        'comment'        : "css=#comment",
        'upload'         : "css=#upload",
        # 'desc'           : "css=input[name='description']",
        'desc'           : "css=#field-description",
        'mailsubmitter'  : "css=#email_submitter",
        'mailowner'      : "css=#email_owner",
        'cc'             : "css=#acmembers",
        'ccac'           : "css=#token-inputacmembers",
        'ccacchoices'    : "css=.token-input-dropdown-acm",
        'ccactoken'      : "css=.token-input-token-acm",
        'ccacdelete'     : "css=.token-input-delete-token-acm",
        'submit'         : "css=#commentform .submit input[type='submit']",
    }


class TicketCommentForm_Locators_Base_2(object):
    """locators for TicketCommentForm object"""

    locators = {
        'base'           : "css=#commentform",
        'tags'           : "css=#actags",
        'tagsac'         : "css=#token-input-actags",
        'tagsacchoices'  : "css=.token-input-dropdown-act",
        'tagsactoken'    : "css=.token-input-token-act",
        'tagsacdelete'   : "css=.token-input-delete-token-act",
        'group'          : "css=#acgroup",
        'groupac'        : "css=#token-input-acgroup",
        'groupacchoices' : "css=.token-input-dropdown-acg",
        'groupactoken'   : "css=.token-input-token-acg",
        'groupacdelete'  : "css=.token-input-delete-token-acg",
        'assignee'       : "css=#ticketowner",
        'severity'       : "css=[id='ticket[severity]']",
        'statusdd'       : "css=#status",
        'messages'       : "css=#messages",
        'private'        : "css=#make-private",
        'comment'        : "css=#comment",
        'upload'         : "css=#ajax-uploader [name='file']",
        # 'desc'           : "css=input[name='description']",
        'desc'           : "css=#field-description",
        'mailsubmitter'  : "css=#email_submitter",
        'mailowner'      : "css=#email_owner",
        'cc'             : "css=#acmembers",
        'ccac'           : "css=#token-inputacmembers",
        'ccacchoices'    : "css=.token-input-dropdown-acm",
        'ccactoken'      : "css=.token-input-token-acm",
        'ccacdelete'     : "css=.token-input-delete-token-acm",
        'submit'         : "css=#commentform .submit input[type='submit']",
    }
