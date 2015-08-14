from hubcheck.pageobjects.basepagewidget import BasePageWidget

class ItemList(BasePageWidget):

    def __init__(self, owner, locatordict, row_class, *args):

        # initialize __rowlocatorid because it is used in _updateLocators()
        # set the locatorid for the result row
        #
        # example list of locators:
        # {
        #   'row'      : '',
        # }
        #
        # users can optionally set the following variables
        # row_start     the row to start iteration at, usually 0, but
        #               may be set to 1 when searching for every nth
        #               row starting from row 1.
        # row_offset    the number of rows in to skip when iterating.

        self.__current_row = 0
        self.__rows = None
        self.__row_class = row_class
        self.__row_class_args = args
        self.row_start = 0
        self.row_offset = 1

        super(ItemList,self).__init__(owner,locatordict)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        # None

        # update the component's locators with this objects overrides
        self._updateLocators()


    def clear_rows(self):

        self.__current_row = self.row_start
        self.__rows = None


    def __iter__(self):

        self.clear_rows()
        return self


    def next(self):

        if self.__rows is None:
            self.logger.debug('looking for rows matching %s' % (self.locators['row']))
            self.__rows = self.find_elements(self.locators['row'])

        self.__current_row += self.row_offset
        self.logger.debug('current_row = %s' % (self.__current_row))
        self.logger.debug('self.__rows = %s' % (self.__rows))
#        self.logger.debug('text = %s' % (self.__rows.text))

        if self.__current_row > len(self.__rows):
            # reset our counter, stop iterating
            self.__current_row = self.row_start
            raise StopIteration

        return self.get_row_by_position(self.__current_row-1)


    def get_row_by_position(self,row_number):
        """
        return the n-th row, where n < maxrows, and negative
        index value wrap like list indicies
        """

        if self.__rows is None:
            self.logger.debug('rbpos looking for rows matching %s' % (self.locators['row']))
            self.__rows = self.find_elements(self.locators['row'])
            self.logger.debug('self.__rows = %s' % (self.__rows))

        nrows = len(self.__rows)
        if (row_number+1) > nrows:
            raise IndexError("while attempting to retrieve row by position,"\
                + " row_number == %d, max rows is %d" % (row_number,nrows))

        # if row_number is out of range on the negative side, wrap around
        if row_number < 0:
            row_number = row_number % nrows

        # css and xpath use indicies starting from 1,
        # not 0 as was requested by this function.
        row_number = row_number + 1

        result = self.__row_class(self.owner,*self.__row_class_args,row_number=row_number)

        # make the result compatible with the iframewrap design pattern
        if self.iframe_tracker is not None:
            self.iframe_tracker.wrap_new_object(result)

        result.detach_from_owner()
        return result


    def get_row_by_property(self,prop,val,compare=None):
        """return the first row whose property prop matches value val

           prop is the name of the property to match
           val is the value that the property must match
           compare is the comparison function to use to determine the match
        """

        if compare is None:
            compare = lambda x,y: x == y

        self.logger.debug('rbprop looking for rows matching %s' \
                            % (self.locators['row']))
        rows = self.find_elements(self.locators['row'])
        self.logger.debug('num rows = %d' % (len(rows)))

        result = None

        # create a default row object, using the first row
        r = self.__row_class(self.owner,*self.__row_class_args,row_number=1)
        r.detach_from_owner()

        # make the result compatible with the iframewrap design pattern
        if self.iframe_tracker is not None:
            self.iframe_tracker.wrap_new_object(r)

        # css row indicies start at 1
        for row_number in xrange(1,len(rows)+1):
            # update the default row object to point to the current row
            r.update_row_number(row_number)

            # check if our current row matches the property constraint
            if compare(r.value()[prop],val):
                result = r
                break

        # if no rows matched, clean up our default row object
        if result is None:
            del r

        return result


    def num_rows(self):
        """return the number of rows"""

        self.logger.debug('numrows looking for rows matching %s' \
                            % (self.locators['row']))
        rows = self.find_elements(self.locators['row'])
        self.logger.debug('rows = %s' % (rows))

        for r in rows:
            self.logger.debug('r.text() = %s' % r.get_attribute('innerHTML'))

        return len(rows)


#class ItemList_Locators_Base(object):
#    """locators for ItemList object"""
#
#    locators = {
#        'base'           : "css=#taglist",
#        'row'            : "css=tbody tr",
#    }
