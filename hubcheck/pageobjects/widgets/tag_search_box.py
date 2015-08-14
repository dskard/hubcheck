from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import TextAC

class TagSearchBox(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TagSearchBox,self).__init__(owner,locatordict)

        # load hub's classes
        TagSearchBox_Locators = self.load_class('TagSearchBox_Locators')

        # update this object's locator
        self.locators.update(TagSearchBox_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tags            = TextAC(self,{'base':'tags',
                                            'aclocatorid':'tagsac',
                                            'choicelocatorid':'tagsacchoices',
                                            'tokenlocatorid':'tagsactoken',
                                            'deletelocatorid':'tagsacdelete'})
        self.submit          = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def search_for(self,terms):
        """perform a search for resources tagged with terms"""

        self.tags.remove_all()
        for t in terms:
            self.tags.send_keys(t+'\n',timeout=-1)
        self.submit.click()


class TagSearchBox_Locators_Base_1(object):
    """locators for TagSearchBox object"""

    locators = {
        'base'           : "css=.data-entry",
        'tags'           : "css=#actags",
        'tagsac'         : "css=#maininput-actags",
        'tagsacchoices'  : "css=.autocompleter-choices",
        'tagsactoken'    : "css=.bit-box",
        'tagsacdelete'   : "css=.closebutton",
        'submit'         : "css=.entry-search-submit",
    }

class TagSearchBox_Locators_Base_2(object):
    """locators for TagSearchBox object"""

    locators = {
        'base'           : "css=.data-entry",
        'tags'           : "css=#actags",
        'tagsac'         : "css=#token-input-actags",
        'tagsacchoices'  : "css=.token-input-dropdown-act",
        'tagsactoken'    : "css=.token-input-token-act",
        'tagsacdelete'   : "css=.token-input-delete-token-act",
        'submit'         : "css=.entry-search-submit",
    }
