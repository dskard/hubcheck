from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Radio

class RegisterFormBase(FormBase):
    def __init__(self, owner, locatordict={}):
        super(RegisterFormBase,self).__init__(owner,locatordict)

        # load hub's classes
        RegisterForm_Locators = self.load_class('RegisterForm_Locators')

        # update this object's locator
        self.locators.update(RegisterForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.username        = Text(self,{'base':'username'})
        self.password        = Text(self,{'base':'password'})
        self.passwordconfirm = Text(self,{'base':'passwordconfirm'})
        self.firstname       = Text(self,{'base':'firstname'})
        self.middlename      = Text(self,{'base':'middlename'})
        self.lastname        = Text(self,{'base':'lastname'})
        self.email           = Text(self,{'base':'email'})
        self.emailconfirm    = Text(self,{'base':'emailconfirm'})

        self.fields = ['username','password','passwordconfirm','firstname',
                       'middlename','lastname','email','emailconfirm']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def register_account(self,data):
        self.submit_form(data)

class RegisterForm1(RegisterFormBase):
    def __init__(self, owner, locatordict={}):
        super(RegisterForm1,self).__init__(owner,locatordict)

class RegisterForm2(RegisterFormBase):
    def __init__(self, owner, locatordict={}):
        super(RegisterForm2,self).__init__(owner,locatordict)

        # load hub's classes
        RegisterForm_Locators = self.load_class('RegisterForm_Locators')
        Captcha1 = self.load_class('Captcha1')

        # update this object's locator
        self.locators.update(RegisterForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.updates         = Checkbox(self,{'base':'updates'})
        self.captcha         = Captcha1(self,{'base':'captcha'})
        self.usageagreement  = Checkbox(self,{'base':'usageagreement'})

        self.fields += ['updates','captcha','usageagreement']

        # update the component's locators with this objects overrides
        self._updateLocators()

class RegisterForm3(RegisterFormBase):
    def __init__(self, owner, locatordict={}):
        super(RegisterForm3,self).__init__(owner,locatordict)

        # load hub's classes
        RegisterForm_Locators = self.load_class('RegisterForm_Locators')
        Captcha1 = self.load_class('Captcha1')

        # update this object's locator
        self.locators.update(RegisterForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        self.captcha         = Captcha1(self,{'base':'captcha'})
        self.usageagreement  = Checkbox(self,{'base':'usageagreement'})
        self.neesaffiliate   = Select(self,{'base':'neesaffiliate'})
        self.citizen         = Radio(self,{'Yes' : 'citizen_yes',
                                           'No'  : 'citizen_no'})
        self.countryorigin   = Select(self,{'base':'countryorigin'})
        self.resident        = Radio(self,{'Yes' : 'resident_yes',
                                           'No'  : 'resident_no'})
        self.countryresident = Select(self,{'base':'countryresident'})
        self.gender          = Radio(self,{'Male'    : 'gender_male',
                                           'Female'  : 'gender_female',
                                           'Refused' : 'gender_refused'})
        self.disability      = Radio(self,{'Yes'     : 'disability_yes',
                                           'No'      : 'disability_no',
                                           'Refused' : 'disability_refused'})
        self.hispanic        = Radio(self,{'Yes'     : 'hispanic_yes',
                                           'No'      : 'hispanic_no',
                                           'Refused' : 'hispanic_refused'})
        self.race_nativeamerican = Checkbox(self,{'base':'race_nativeamerican'})
        self.race_asian          = Checkbox(self,{'base':'race_asian'})
        self.race_black          = Checkbox(self,{'base':'race_black'})
        self.race_pacificisland  = Checkbox(self,{'base':'race_pacificisland'})
        self.race_white          = Checkbox(self,{'base':'race_white'})
        self.race_refused        = Checkbox(self,{'base':'race_refused'})

        self.fields += ['captcha','usageagreement','neesaffiliate','citizen',
                        'countryorigin','resident','countryresident','gender',
                        'disability','hispanic','race_nativeamerican',
                        'race_asian','race_black','race_pacificisland',
                        'race_white','race_refused']

        # update the component's locators with this objects overrides
        self._updateLocators()

class RegisterForm_Locators_Base(object):
    """locators for RegisterForm object"""

    locators = {
        'base'                  : "css=#hubForm",
        'username'              : "css=#userlogin",
        'password'              : "css=#password",
        'passwordconfirm'       : "css=#password2",
        'firstname'             : "css=input[name='name[first]']",
        'middlename'            : "css=input[name='name[middle]']",
        'lastname'              : "css=input[name='name[last]']",
        'email'                 : "css=#email",
        'emailconfirm'          : "css=#email2",
        'updates'               : "css=#mailPreferenceOption",
        'submit'                : "css=#hubForm .submit input[type='submit']",
#        'submitbase'            : "css=#content",
#        'accountcreated'        : "css=.passed",
        'neesaffiliate'         : "css=#nees_affiliation",
        'citizen_yes'           : "css=#corigin_usyes",
        'citizen_no'            : "css=#corigin_usno",
        'countryorigin'         : "css=#corigin",
        'resident_yes'          : "css=#cresident_usyes",
        'resident_no'           : "css=#cresident_usno",
        'countryresident'       : "css=#cresident",
        'gender_male'           : "css=input[name='sex'][value='male']",
        'gender_female'         : "css=input[name='sex'][value='female']",
        'gender_refused'        : "css=input[name='sex'][value='refused']",
        'disability_yes'        : "css=#disabilityyes",
        'disability_no'         : "css=#disabilityno",
        'disability_refused'    : "css=#disabilityrefused",
        'hispanic_yes'          : "css=#hispanicyes",
        'hispanic_no'           : "css=#hispanicno",
        'hispanic_refused'      : "css=#hispanicrefused",
        'race_nativeamerican'   : "css=#racenativeamerican",
        'race_nativetribe'      : "css=#racenativetribe",
        'race_asian'            : "css=#raceasian",
        'race_black'            : "css=#raceblack",
        'race_pacificisland'    : "css=#racehawaiian",
        'race_white'            : "css=#racewhite",
        'race_refused'          : "css=#racerefused",
        'captcha'               : "css=.captcha-block",
        'usageagreement'        : "css=#usageAgreement",
    }
