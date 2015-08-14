from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.basepageelement import Select

import hubcheck.conf

import os
import json
import re

class Captcha2(BasePageWidget):
    def __init__(self, owner, locatordict={}, refreshCB=None):
        super(Captcha2,self).__init__(owner,locatordict)

        # load hub's classes
        Captcha2_Locators = self.load_class('Captcha2_Locators')

        # update this object's locator defaults
        self.locators.update(Captcha2_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.refreshCB   = refreshCB
        self.answer      = BasePageWidget(self,{'base':'captcha-answer'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    @property
    def value(self):
        """get the value of the captcha"""

        self.question = TextReadOnly(self.owner,self.locatordict)
        text = self.question.value
        self.question.detach_from_owner()
        return text

    @value.setter
    def value(self, val):
        """set the value of the captcha"""

        if val:
            self.solve()


    def refresh(self):
        """refresh the captcha"""

        if self.refreshCB:
            self.refreshCB()
        else:
            self._browser.refresh()


    def solve(self):
        """solve the captcha"""

        handler = {
            'input' : Text,
            'select' : Select,
        }

        captchaInfo = os.path.join(hubcheck.conf.settings.data_dir,'captcha.json')
        with open(captchaInfo,'r') as f:
            captchadict = json.load(f)
        f.close()

        pattern = re.compile("Please answer the question:\nREQUIRED\n\n(.+)")
        count = 0
        solved = False

        while count < 10:
            count = count + 1

            # grab the captcha question
            t = self.value
            try:
                q = pattern.search(t).group(1)
            except:
                # yikes, no question text found!
                # refresh the browser and try again
                self.logger.debug("Could not parse question from CAPTCHA: %s" % (t))
                self.refresh()
                continue

            # have we seen this question before
            if captchadict.has_key(q) == False:
                # question not in dictionary
                # refresh the browser and try again
                self.logger.debug("Question not in dictionary: %s" % (q))
                self.refresh()
                continue

            # fill in the answer for the captcha
            self.answer.detach_from_owner()
            self.answer = handler[captchadict[q]['tag_name']](self,{'base':'captcha-answer'})
            self.answer.value = captchadict[q]['options'][captchadict[q]['answeridx']]
            solved = True
            break

        return solved

class Captcha2_Locators_Base(object):
    """locators for Captcha2 object"""

    locators = {
        'base'              : "css=label[for='captcha-answer']",
        'captcha-answer'    : "css=#captcha-answer",
    }

