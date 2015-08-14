from hubcheck.pageobjects.widgets.item_list import ItemList
from hubcheck.pageobjects.basepageelement import TextReadOnly
import re

class SearchResults(ItemList):
    """Specific type of ItemList used to iterate through lists that result
       from searches.

       Provides a header_counts() function, that returns the start, stop,
       and total number of results displayed, as stated by the counts in
       the table header.
    """

    def __init__(self, owner, locatordict, row_class, row_class_locatordict):

        # initialize __rowlocatorid because it is used in _updateLocators()
        # set the locatorid for the result row
        #
        # example list of locators:
        # {
        #   'counts'   : '',
        #   'row'      : '',
        #   'substrow' : '',
        # }
        #

        super(SearchResults,self).__init__(owner,locatordict,row_class,row_class_locatordict)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.counts = TextReadOnly(self,{'base':'counts'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    #FIXME: remove this function from tags code
    def header_counts(self):

        pattern = re.compile('.*\((\d+) *- *(\d+) of (\d+)\).*')
        (start,stop,total) = pattern.match(self.counts.value).groups()
        return (int(start),int(stop),int(total))


#class SearchResults_Locators_Base(object):
#    """locators for SearchResults object"""
#
#    locators = {
#        'base'           : "css=#taglist",
#        'row'            : "css=tbody tr",
#        'substrow'       : "css=#taglist tbody tr:nth-of-type({row_num})",
#        'counts'         : "css=thead tr th span",
#    }
