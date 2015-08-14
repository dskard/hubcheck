import pprint

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button

class FormBase(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(FormBase,self).__init__(owner,locatordict)

        # load hub's classes
        FormBase_Locators = self.load_class('FormBase_Locators')

        # update this object's locator
        self.locators.update(FormBase_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.submit = Button(self,{'base':'submit'})

        self.fields = []

        # update the component's locators with this objects overrides
        self._updateLocators()


    def populate_form(self, data):
        """populate the form with data from the data parameter"""

        if hasattr(data,'items'):
            # convert dictionaries to lists
            # so we can support filling out forms in order
            data = data.items()

        self._po.wait_for_page_element_displayed(
            loc=self.locators['base'])

        self.logger.debug('form data = %s' % (pprint.pformat(data)))


        for (k,v) in data:
            if v is None:
                continue
            if not k in self.fields:
                # bail, the key is not a field
                raise ValueError("invalid form field: %s" % (k))
            # find the widget in the object's dictionary and set its value
            widget = getattr(self,k)
            widget.value = v


    def submit_form(self,data={}):
        """submit the form, fill in data if it is provided"""

        self.populate_form(data)

        # we use a page marker to tell when the form has been submitted.  some
        # websites lead back to the original page, which makes it hard to tell
        # that the form submission has completed by using elements available on
        # the page. we use a page load marker to help us with that task.

        self._po.set_page_load_marker()
        result = self.submit.click()
        self._po.wait_for_page_load_marker()

        return result


class FormBase_Locators_Base(object):
    """locators for FormBase object"""

    locators = {
        'base'   : "css=#hubForm",
        'submit' : "css=[type='submit']",
    }

class PreviewFormBase(FormBase):
    def __init__(self, owner, locatordict={}):
        super(PreviewFormBase,self).__init__(owner,locatordict)

        # load hub's classes
        PreviewFormBase_Locators = self.load_class('PreviewFormBase_Locators')

        # update this object's locator
        self.locators.update(PreviewFormBase_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.preview  = Button(self,{'base':'preview'})
        self.submit   = Button(self,{'base':'submit'})

        self.fields = []

        # update the component's locators with this objects overrides
        self._updateLocators()


    def preview_page(self):
        """preview the page before submitting"""

        return self.preview.click()


class PreviewFormBase_Locators_Base(object):
    """locators for PreviewFormBase object"""

    locators = {
        'base'    : "css=#hubForm",
        'submit'  : "css=#hubForm [type='submit']",
        'preview' : "css=#hubForm [name='preview']",
    }
