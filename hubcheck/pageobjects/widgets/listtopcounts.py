from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ListTopCounts(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ListTopCounts,self).__init__(owner,locatordict)

        # load hub's classes
        # ListPageNavBase_Locators = self.load_class('ListPageNavBase_Locators')
        ListTopCounts_Locators = ListTopCounts_Locators_Base

        # update this object's locator
        self.locators.update(ListTopCounts_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.caption = TextReadOnly(self,{'base':'caption'})
        self.counts  = TextReadOnly(self,{'base':'counts'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_caption(self):
        """return the whole caption string"""

        return self.caption.value


    def get_caption_description(self):
        """return the caption description"""

        return self.caption.value[0:-(len(self.counts.value))].strip()


    def get_caption_counts(self):
        """return a 3-tuple of the beginning shown, end shown, total resources"""

        countstxt = self.counts.value

        if countstxt.strip() == 'No records found':
            return (0,0,0)

        pattern = re.compile("\((\d+) - (\d+) of (\d+)\)")
        (beginshown,endshown,total) = pattern.match(countstxt).groups()
        return (int(beginshown),int(endshown),int(total))


class ListTopCounts_Locators_Base(object):
    """locators for ListTopCounts object"""

    locators = {
        'base'          : "css=.entries",
        'caption'       : "css=.entries caption",
        'counts'        : "css=.entries caption span",
    }
