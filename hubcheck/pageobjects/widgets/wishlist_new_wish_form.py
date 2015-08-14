from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextArea
from hubcheck.pageobjects.basepageelement import TextAC

class WishlistNewWishForm(BasePageWidget):
    def __init__(self, owner, locatordict={}, refreshCaptchaCB=None):
        super(WishlistNewWishForm,self).__init__(owner,locatordict)

        # load hub's classes
        WishlistNewWishForm_Locators = self.load_class('WishlistNewWishForm_Locators')

        # update this object's locator
        self.locators.update(WishlistNewWishForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.anonymous       = Checkbox(self,{'base':'anonymous'})
        self.private         = Checkbox(self,{'base':'private'})
        self.subject         = Text(self,{'base':'subject'})
        self.problem         = TextArea(self,{'base':'problem'})
        self.tags            = TextAC(self,{'base':'tags',
                                            'aclocatorid':'tagsac',
                                            'choicelocatorid':'tagsacchoices',
                                            'tokenlocatorid':'tagsactoken',
                                            'deletelocatorid':'tagsacdelete'})
        self.submit          = Button(self,{'base':'submit'})

        self.fields = ['anonymous','private','subject','problem','tags']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        widgets = [self.anonymous, self.subject, self.problem,
                   self.tags, self.submit]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        widgets = [self.anonymous, self.private, self.subject,
                   self.problem, self.tags, self.submit]
        self._checkLocators(widgets,cltype)

    def submit_wish(self,data):
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
            self.subject.value = data

        # submit the wish
        self.submit.click()


class WishlistNewWishForm_Locators_Base(object):
    """locators for WishlistNewWishForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'anonymous'         : "css=[name='anonymous']",
        'private'           : "css=[name='private']",
        'subject'           : "css=#subject",
        'problem'           : "css=[name='about']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'submit'            : "css=#send-wish",
    }
