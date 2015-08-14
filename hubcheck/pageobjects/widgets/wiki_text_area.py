from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextArea
# from hubcheck.pageobjects.widget_wikitoolbar import WikiToolbar

class WikiTextArea(BasePageWidget):
    """This widget combines a Wiki Toolbar with a TextArea widget"""
    # FIXME: this object should only take a dictionary of values, not locators and locdict

    def __init__(self, owner, locatordict={}):
        super(WikiTextArea,self).__init__(owner,locatordict)

        # load hub's classes
        WikiTextArea_Locators = self.load_class('WikiTextArea_Locators')

        # update this object's locator defaults
        self.locators.update(WikiTextArea_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.textarea   = TextArea(self, {'base':'textarea'})
        # self.toolbar    = WikiToolbar(owner, {'base':'toolbar'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    @property
    def value(self):

        return self.textarea.value


    @value.setter
    def value(self, val):

        self.textarea.value = val


class WikiTextArea_Locators_Base(object):
    locators = {
        'base'      : "css=#wykiwyg",
        'textarea'  : "css=.wiki-toolbar-content",
        'toolbar'   : "css=.wiki-toolbar",
    }


#class WikiTextArea2(BasePageWidget):
#    """This widget combines a Wiki Toolbar with a TextArea widget"""
#    # FIXME: this object should only take a dictionary of values, not locators and locdict
#
#    def __init__(self, owner, locatordict={}):
#        super(WikiTextArea,self).__init__(owner)
#
#        # load hub's classes
#        WikiTextArea_Locators = self.load_class('WikiTextArea_Locators')
#
#        # update this object's locator
#        self.locators.update(WikiTextArea_Locators.locators)
#
#        # update the locators with those from the owner
#        for k,v in locatordict.items():
#            if k in self.locators:
#                self.locators[k] = self.owner.locators[v]
#
#        # setup page object's components
#        self.textarea   = TextArea(self, 'textarea')
#        # self.toolbar    = WikiToolbar(owner, 'toolbar')
#
#        # update the component's locators with this objects overrides
#        self._updateLocators()
#
#
#    @property
#    def value(self):
#
#        return self.textarea.value
#
#
#    @value.setter
#    def value(self, val):
#
#        self.textarea.value = val
#
#
#class WikiTextArea_Locators_Base(object):
#    locators = {
#        'base'      : "css=#wykiwyg",
#        'textarea'  : "css=.wiki-toolbar-content",
#        'toolbar'   : "css=.wiki-toolbar",
#    }
