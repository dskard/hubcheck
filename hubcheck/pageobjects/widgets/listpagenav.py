from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class ListPageNavBase(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ListPageNavBase,self).__init__(owner,locatordict)

        # load hub's classes
        # ListPageNavBase_Locators = self.load_class('ListPageNavBase_Locators')
        ListPageNavBase_Locators = ListPageNavBase_Locators_Base

        # update this object's locator
        self.locators.update(ListPageNavBase_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.limit          = Select(self,{'base':'limit'})
        self.counts         = TextReadOnly(self,{'base':'counts'})
        self.current_page   = TextReadOnly(self,{'base':'currentpage'})

        self._pagenavnames = []

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_page_number(self,pagenumber):
        """click on a specific page in the pagination list"""

        # perform input validation
        pagenumber = int(pagenumber)

        if pagenumber < 1:
            raise IndexError("pagenumber out of range: expected value\
                >= 1, received %s" % (pagenumber))

        available_pages = self.get_link_page_numbers()
        if len(available_pages) == 0:
            if pagenumber != 1:
                raise IndexError("no pages available, pagenumber must be == 1")

        max_page_number = max([int(i) for i in available_pages])

        if pagenumber > max_page_number:
            raise IndexError("pagenumber out of range: expected value\
                <= %i, received %d" % (max_page_number,pagenumber))

        # click the page number link
        loctxt = self.locators['page'] % int(pagenumber)
        self.locators['_pagelink'] = loctxt
        page = Link(self,{'base':'_pagelink'})
        page.detach_from_owner()
        page.click()
        del page
        del self.locators['_pagelink']


    def goto_page_relative(self,relation):
        """go to the start, end, previous, or next page"""

        if not relation in self._pagenavnames:
            raise ValueError("relation should be one of %s" % (self._pagenavnames))
        w = getattr(self,"%spage" % (relation))
        self._po.set_page_load_marker()
        w.click()
        # clicking navigation changes the page
        self._po.wait_for_page_to_load()



    def get_pagination_counts(self):
        """return a 3-tuple of the beginning shown, end shown, total resources"""

        countstxt = self.counts.value

        if countstxt.strip() == 'No records found':
            return (0,0,0)

        pattern = re.compile("Results (\d+) - (\d+) of (\d+)")
        (beginshown,endshown,total) = pattern.match(countstxt).groups()
        return (int(beginshown),int(endshown),int(total))


    def display_limit(self,limit=None):
        """return the limit of the items shown"""

        if limit:
            self.limit.value = str(limit)
            # after changing the limit, the page refreshes
            self.limit.wait_until_present()
        return self.limit.value


    def get_current_page_number(self):
        """return the current page number"""

        return self.current_page.value


    def get_link_page_numbers(self):
        """return a list of the page numbers that are links"""

        pagelinks = self.find_elements_in_owner(self.locators['pagelinks'])
        pagenames = []
        for page in pagelinks:
            pagenames.append(page.text)
        return pagenames


    def relation_exists(self,relation):
        """check if the start, end, prev, next relation is in the html"""

        if not relation in self._pagenavnames:
            raise ValueError("relation should be one of %s" % (self._pagenavnames))
        w = getattr(self,"%spage" % (relation))
        return w.is_present()


    def relation_displayed(self,relation):
        """check if the start, end, prev, next relation is clickable"""

        if not relation in self._pagenavnames:
            raise ValueError("relation should be one of %s" % (self._pagenavnames))
        w = getattr(self,"%spage" % (relation))
        return w.is_displayed()


class ListPageNav1(ListPageNavBase):
    def __init__(self, owner, locatordict={}):
        super(ListPageNav1,self).__init__(owner,locatordict)

        # load hub's classes
        ListPageNav_Locators = self.load_class('ListPageNav_Locators')

        # update this object's locator
        self.locators.update(ListPageNav_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.startpage      = Link(self,{'base':'start'})
        self.prevpage       = Link(self,{'base':'prev'})
        self.nextpage       = Link(self,{'base':'next'})
        self.endpage        = Link(self,{'base':'end'})

        self._pagenavnames = ['start','end','next','prev']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ListPageNav2(ListPageNavBase):
    def __init__(self, owner, locatordict={}):
        super(ListPageNav2,self).__init__(owner,locatordict)

        # load hub's classes
        ListPageNav_Locators = self.load_class('ListPageNav_Locators')

        # update this object's locator
        self.locators.update(ListPageNav_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.startpage      = Link(self,{'base':'start'})
        self.endpage        = Link(self,{'base':'end'})

        self._pagenavnames = ['start','end']

        # update the component's locators with this objects overrides
        self._updateLocators()

class ListPageNavBase_Locators_Base(object):
    """locators for ListPageNavBase object"""

    locators = {
        'base'          : "css=.list-footer",
        'limit'         : "css=#limit",
        'counts'        : "css=.counter",
        'page'          : "xpath=//li[contains(@class,'page')]/a[text()='%d']",
        'pagelinks'     : "css=li.page a",
        'currentpage'   : "css=li.page strong",
    }


class ListPageNav1_Locators_Base(object):
    """locators for ListPageNav1 object"""

    locators = {
        'base'          : "css=.list-footer",
        'limit'         : "css=#limit",
        'counts'        : "css=.counter",
        'page'          : "xpath=//li[contains(@class,'page')]/a[text()='%d']",
        'pagelinks'     : "css=li.page a",
        'currentpage'   : "css=li.page strong",
        'start'         : "css=.start",
        'prev'          : "css=.prev",
        'next'          : "css=.next",
        'end'           : "css=.end",
    }

class ListPageNav2_Locators_Base(object):
    """locators for ListPageNav2 object"""

    locators = {
        'base'          : "css=.list-footer",
        'limit'         : "css=#limit",
        'counts'        : "css=.counter",
        'page'          : "xpath=//li[contains(@class,'page')]/a[text()='%d']",
        'pagelinks'     : "css=li.page a",
        'currentpage'   : "css=li.page strong",
        'start'         : "css=.start",
        'end'           : "css=.end",
    }
