from hubcheck.pageobjects.basepagewidget import BasePageWidget

class ItemListItem(BasePageWidget):

    def __init__(self, owner, locatordict={}, row_number=0):

        # initialize variables
        self._row_number = row_number

        super(ItemListItem,self).__init__(owner,locatordict)


    def _updateLocators(self):

        # reset the locators dictionary to include the locator templates
        super(ItemListItem,self)._updateLocators()

        # format all locator templates
        for k,v in self.locators.items():
            if v is not None:
                self.locators[k] = v.format(row_num=self._row_number)

        # update this object's children
        self.update_locators_in_widgets()


    def update_row_number(self,row_number):

        self._row_number = row_number
        self._updateLocators()


    def value(self):
        """return a dictionary of values to represent the row"""
        pass
