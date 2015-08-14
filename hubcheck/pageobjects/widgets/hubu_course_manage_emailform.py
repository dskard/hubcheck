from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextReadOnly

class HubUCourseManageEmailForm(BasePageWidget):
    """hub u course manager email"""

    def __init__(self,owner,locatordict={}):
        super(HubUCourseManageEmailForm,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseManageEmailForm_Locators = self.load_class('HubUCourseManageEmailForm_Locators')

        # update this object's locator
        self.locators.update(HubUCourseManageEmailForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.discard      = Link(self,{'base':'discard'})
        self.toaddr       = TextAC(self,{'base':'to',
                                         'aclocatorid':'toac',
                                         'choicelocatorid':'toacchoices',
                                         'tokenlocatorid':'toactoken',
                                         'deletelocatorid':'toacdelete'})
        self.fromaddr     = TextReadOnly(self,{'base':'from'})
        self.replyto      = TextReadOnly(self,{'base':'replyto'})
        self.template     = Select(self,{'base':'template'})
        self.subject      = TextReadOnly(self,{'base':'subject'})
        self.body         = TextReadOnly(self,{'base':'body'})
        self.submit       = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocators(self,widgets=None,cltype=''):

        # to see all of the widgets, you need to choose a template first
        options = self.template.options()
        self.template.choose(options[0])
        super(HubUCourseManageEmailForm,self)._checkLocators(widgets,cltype)


    def send_email(self,tolist,templateName):
        """send an email to the addresses in tolist using the template templateName"""

        if tolist != None:
            self.toaddr.value = tolist
        if templateName != None:
            self.template.value = templateName
        self.submit.click()


class HubUCourseManageEmailForm_Locators_Base(object):
    """locators for HubUCourseManageEmailForm object"""

    locators = {
        'base'          : "css=#send-invite",
        'discard'       : "css=.back",
        'to'            : "css=#to",
        'toac'          : "css=#token-input-to",
        'toacchoices'   : "css=.token-input-dropdown",
        'toactoken'     : "css=.token-input-token",
        'toacdelete'    : "css=.token-input-delete-token",
        'from'          : "css=[name='from']",
        'replyto'       : "css=[name='replyto']",
        'template'      : "css=#email-template",
        'subject'       : "css=[name='subject']",
        'body'          : "css=[name='body']",
        'submit'        : "css=#send-email-submit",
    }

