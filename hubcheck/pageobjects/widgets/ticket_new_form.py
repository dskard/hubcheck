from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Upload

import re

class TicketNewForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(TicketNewForm,self).__init__(owner,locatordict)

        # load hub's classes
        TicketNewForm_Locators = self.load_class('TicketNewForm_Locators')
        Captcha1 = self.load_class('Captcha1')

        # update this object's locator
        self.locators.update(TicketNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name            = Text(self,{'base':'name'})
        self.organization    = Text(self,{'base':'organization'})
        self.email           = Text(self,{'base':'email'})
        self.os              = Select(self,{'base':'os'})
        self.webbrowser      = Select(self,{'base':'webbrowser'})
        self.problem         = TextArea(self,{'base':'problem'})
        self.attachtype      = TextReadOnly(self,{'base':'attachtype'})
        self.upload          = Upload(self,{'browselocatorid':'upload'})
        self.captcha         = Captcha1(self,{'base':'captcha'})

        self.fields += ['name', 'organization', 'email', 'os', 'webbrowser',
                        'problem', 'attachtype', 'upload', 'captcha']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        widgets = [self.name,self.organization,self.email,self.os,
                   self.webbrowser,self.problem,self.upload,
                   self.captcha]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsLoggedIn(self,widgets=None,cltype='LoggedIn'):

        widgets = [self.name,self.organization,self.email,self.os,
                   self.webbrowser,self.problem,self.upload]
        self._checkLocators(widgets,cltype)


    def get_attachment_types(self):

        return self.attachtype.value


    def submit_ticket(self,data):

        if not hasattr(data,'items'):
            data = {'problem' : data}
        return self.submit_form(data)


class TicketNewForm_Locators_Base(object):
    """locators for TicketNewForm object"""

    locators = {
        'base'           : "css=#hubForm",
        'submitbase'     : "css=#content",
        'name'           : "css=#reporter_name",
        'organization'   : "css=#reporter_org",
        'email'          : "css=#reporter_email",
        'os'             : "css=#problem_os",
        'webbrowser'     : "css=#problem_browser",
        'problem'        : "css=#problem_long",
        'attachtype'     : "css=small",
        'upload'         : "css=#trUpload",
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
        'assignee'       : "css=#problemowner",
        'severity'       : "css=[id='ticket[severity]']",
        'statusdd'       : "css=#ticket-field-status",
        'captcha'        : "css=.captcha-block",
        'submit'         : "css=#hubForm .submit input[type='submit']",
    }

class TicketNewForm2(FormBase):
    def __init__(self, owner, locatordict={}):
        super(TicketNewForm2,self).__init__(owner,locatordict)

        # load hub's classes
        TicketNewForm_Locators = self.load_class('TicketNewForm_Locators')
        Captcha2 = self.load_class('Captcha2')

        # update this object's locator
        self.locators.update(TicketNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name            = Text(self,{'base':'name'})
        self.organization    = Text(self,{'base':'organization'})
        self.email           = Text(self,{'base':'email'})
        self.os              = Select(self,{'base':'os'})
        self.webbrowser      = Select(self,{'base':'webbrowser'})
        self.problem         = TextArea(self,{'base':'problem'})
        self.attachtype      = TextReadOnly(self,{'base':'attachtype'})
        self.upload          = Upload(self,{'browselocatorid':'upload'})

        self.security        = Checkbox(self,{'base':'security'})

        self.captcha         = Captcha2(self,{'base':'captcha'})

        self.fields += ['name', 'organization', 'email', 'os', 'webbrowser',
                        'problem', 'attachtype', 'upload', 'captcha',
                        'security']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        # FIXME: need to add self.security?
        widgets = [self.name,self.organization,self.email,self.os,
                   self.webbrowser,self.problem,self.upload,
                   self.captcha,self.submit]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsLoggedIn(self,widgets=None,cltype='LoggedIn'):

        # FIXME: need to add self.security?
        widgets = [self.name,self.organization,self.email,self.os,
                   self.webbrowser,self.problem,self.upload,
                   self.submit]
        self._checkLocators(widgets)


    def get_attachment_types(self):

        return self.attachtype.value


    def submit_ticket(self,data):

        if not hasattr(data,'items'):
            data = {'problem' : data}
        return self.submit_form(data)


class TicketNewForm2_Locators_Base(object):
    """locators for TicketNewForm2 object"""

    locators = {
        'base'           : "css=#hubForm",
        'submitbase'     : "css=#content",
        'name'           : "css=#reporter_name",
        'organization'   : "css=#reporter_org",
        'email'          : "css=#reporter_email",
        'os'             : "css=#problem_os",
        'webbrowser'     : "css=#problem_browser",
        'problem'        : "css=#problem_long",
        'attachtype'     : "css=#hubForm small",
        'upload'         : "css=#trUpload",
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
        'assignee'       : "css=#problemowner",
        'severity'       : "css=[id='ticket[severity]']",
        'statusdd'       : "css=#ticket-field-status",
        'security'       : "css=#isSecurityIncident",
        'captcha'        : "css=#hubForm label[for='captcha-answer']",
        'submit'         : "css=#hubForm .submit input[type='submit']",
    }
