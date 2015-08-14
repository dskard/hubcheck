from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Text

class HubUCourseLogin(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseLogin,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseLogin_Locators = self.load_class('HubUCourseLogin_Locators')

        # update this object's locator
        self.locators.update(HubUCourseLogin_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username = Text(self,{'base':'username'})
        self.password = Text(self,{'base':'password'})
        self.remember = Checkbox(self,{'base':'remember'})
        self.submit   = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def login_as(self,username,password,remember=False):
        """login to the website as the specified user"""

        self.username.value = username
        self.password.value = password
        self.remember.value = remember
        self.submit.click()

class HubUCourseLogin_Locators_Base(object):
    """locators for HubUCourseLogin object"""

    locators = {
        'base'          : "css=#course-login",
        'username'      : "css=#course-login [name='username']",
        'password'      : "css=#course-login [name='passwd']",
        'remember'      : "css=#course-login [name='remember']",
        'submit'        : "css=#course-login input[type='submit']",
    }

