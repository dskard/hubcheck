from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly
import hubcheck.utils
import re

class PopularList(BasePageWidget):

    def __init__(self, owner, locatordict, item_class, item_class_locatordict):

        # example list of locators:
        # {
        #   'item'   : '',
        # }
        #
        self.__current = 0
        self.__items = None
        self.__item_class = item_class
        self.__item_class_locatordict = item_class_locatordict

        super(PopularList,self).__init__(owner,locatordict)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        # None

        # update the component's locators with this objects overrides
        self._updateLocators()


    def __iter__(self):

        return self


    def next(self):

        if self.__items is None:
            self.__items = self.find_elements(self.locators['item'])

        self.__current += 1

        if self.__current > len(self.__items):
            raise StopIteration

        return self.get_item_by_position(self.__current-1)


    def get_item_by_position(self,item_number):
        """return the n-th item, where n < maxitems, and negative\
           index value wrap like list indicies"""

        if self.__items is None:
            self.__items = self.find_elements(self.locators['item'])

        nitems = len(self.__items)
        if (item_number+1) > nitems:
            raise IndexError("while attempting to retrieve item by position,\
                item_number == %d, max items is %d" % (item_number,nitems))

        # if item_number is out of range on the negative side, wrap around
        if item_number < 0:
            item_number = item_number % nitems

        # css and xpath use indicies starting from 1,
        # not 0 as was requested by this function.
        item_number = item_number + 1

        result = self.__item_class(self.owner,self.__item_class_locatordict,item_number)
        result.detach_from_owner()
        return result


    def get_item_by_property(self,prop,val):
        """return the n-th item"""

        if self.__items is None:
            self.__items = self.find_elements(self.locators['item'])

        result = None

        for item_number in xrange(len(self.__items)):
            r = self.get_item_by_position(item_number)
            if r.value()[prop] == val:
                result = r
                break
            del r

        return result


    def num_items(self):

        if self.__items is None:
            self.__items = self.find_elements(self.locators['item'])

        return len(self.__items)


#class PopularList_Locators_Base(object):
#    """locators for PopularList object"""
#
#    locators = {
#        'item'     : "css=",
#    }
