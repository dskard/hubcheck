from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class Footer(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Footer,self).__init__(owner,locatordict)

        # load hub's classes
        Footer_Locators = self.load_class('Footer_Locators')

        # update this object's locator
        self.locators.update(Footer_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.aboutus    = Link(self,{'base':'aboutus'})
        self.contactus  = Link(self,{'base':'contactus'})
        self.termsofuse = Link(self,{'base':'termsofuse'})
        self.members    = Link(self,{'base':'members'})
        self.groups     = Link(self,{'base':'groups'})
        self.myaccount  = Link(self,{'base':'myaccount'})
        self.questions  = Link(self,{'base':'questions'})
        self.ideas      = Link(self,{'base':'ideas'})
        self.kb         = Link(self,{'base':'kb'})
        self.resources  = Link(self,{'base':'resources'})
        self.tools      = Link(self,{'base':'tools'})
        self.upload     = Link(self,{'base':'upload'})

        # update the component's locators with this objects overrides
        self._updateLocators()

class Footer_Locators_Base(object):
    """locators for Header object"""

    locators = {
        'base'          : "css=#footer",
        'aboutus'       : "xpath=//a[text()='About us']",
        'contactus'     : "xpath=//a[text()='Contact us']",
        'termsofuse'    : "xpath=//a[text()='Terms of Use']",
        'members'       : "xpath=//a[text()='Members']",
        'groups'        : "xpath=//a[text()='Groups']",
        'myaccount'     : "xpath=//a[text()='My Account']",
        'questions'     : "xpath=//a[text()='Questions & Answers']",
        'ideas'         : "xpath=//a[text()='Ideas & Discussions']",
        'kb'            : "xpath=//a[text()='Knowledge Base']",
        'resources'     : "xpath=//a[text()='Resources']",
        'tools'         : "xpath=//a[text()='Tools']",
        'upload'        : "xpath=//a[text()='Upload your own']",
    }
