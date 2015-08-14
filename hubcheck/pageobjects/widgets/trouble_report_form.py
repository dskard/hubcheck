from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import Upload
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class TroubleReportForm(BasePageWidget):
    def __init__(self, owner, locatordict={}, refreshCaptchaCB=None):
        super(TroubleReportForm,self).__init__(owner,locatordict)

        # load hub's classes
        TroubleReportForm_Locators = self.load_class('TroubleReportForm_Locators')
        Captcha2 = self.load_class('Captcha2')

        # update this object's locator
        self.locators.update(TroubleReportForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username        = Text(self,{'base':'username'})
        self.name            = Text(self,{'base':'name'})
        self.email           = Text(self,{'base':'email'})
        self.problem         = TextArea(self,{'base':'problem'})
        self.upload          = Upload(self,{'base':'upload','browselocatorid':'upload'})
        self.submit          = Button(self,{'base':'submit'},self._onClick)
        self.ticketlink      = Link(self,{'base':'ticket_link'})
        self.captcha         = Captcha2(self,{'base':'captcha'},refreshCaptchaCB)

        self.fields = ['username','name','email','problem','upload','captcha']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsLoggedIn(self,widgets=None,cltype='LoggedIn'):

        widgets = [self.username, self.name, self.email,
                   self.problem, self.upload, self.submit]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsLoggedOut(self,widgets=None,cltype='LoggedOut'):

        widgets = [self.username, self.name, self.email,
                   self.problem, self.upload, self.submit,
                   self.captcha]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsSubmitted(self,widgets=None,cltype=''):

        widgets = [self.ticketlink]
        self._checkLocators(widgets,cltype)


    def submit_ticket(self, data):

        self.populate_form(data)
        # submit the ticket
        ticket_number = self.submit.click()
        self.logger.debug('ticket_number = %s' % (ticket_number))
        return ticket_number


    def populate_form(self, data):

        # data is either a dictionary or string
        if isinstance(data,dict):
            for k,v in data.items():
                if v is None:
                    # no value to set
                    continue
                if not k in self.fields:
                    # bail, the key is not a field
                    raise ValueError("invalid form field: %s" % (k))
                # find the widget in the object's dictionary and set its value
                widget = getattr(self,k)
                widget.value = v
        else:
            self.problem.value = data


    def _onClick(self):

        # FIXME: change the webdriverwait to an ec
        #        that returns the element

        # wait for the page to refresh
        message = "while waiting for ticket to be submitted"
        wait = WebDriverWait(self._browser, 60)
        wait.until(lambda browser :
                   browser.find_element_by_id("trSuccess").is_displayed(),
                   message=message)

        ticket_number = self.ticketlink.text()
        return ticket_number


    def goto_ticket(self):

        e = self.find_element(self.locators['ticket_link'])
        e.click()


class TroubleReportForm_Locators_Base(object):
    """locators for TroubleReportForm object"""

    locators = {
        'base'              : "css=#troublereport",
        'username'          : "css=#trLogin",
        'name'              : "css=#trName",
        'email'             : "css=#trEmail",
        'problem'           : "css=#trProblem",
        'upload'            : "css=#trUpload",
        'submit'            : "css=#send-form",
        'captcha'           : "css=label[for='captcha-answer']",
        'ticket_link'       : "css=div[id='trSuccess'] > div > p:nth-child(1) > span > a",
    }
