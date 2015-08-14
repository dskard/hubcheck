from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class SortOrderOptions(BasePageWidget):

    def __init__(self, owner, locatordict):

        super(SortOrderOptions,self).__init__(owner,locatordict)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def select(self,option):

        if not option in self.locators.keys():
            raise ValueError("invalid button: %s" % (option))
        if option == 'base':
            raise ValueError("invalid button: %s" % (option))

        link = Link(self,self.locators[option])
        link.detach_from_owner()
        link.click()
