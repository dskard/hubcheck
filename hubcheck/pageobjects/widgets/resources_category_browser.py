from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class ResourcesCategoryBrowser(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(ResourcesCategoryBrowser,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesCategoryBrowser_Locators = self.load_class('ResourcesCategoryBrowser_Locators')

        # update this object's locator
        self.locators.update(ResourcesCategoryBrowser_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _massage_category_names(self,category):
        # as a convenience to the user, we massage the category name
        # to help find the category element.

        ## first we search for the original name (in the calling function),
        ## then we search for the lowercase version,
        ## try stripping the trailing "s" off
        ## and try searching for the lowercase version without the trailing s
        #r = [ category.lower() ]
        #if category.endswith('s'):
        #    # also try combinations where we only strip the last 's'
        #    r += [ category[0:-1], category.lower()[0:-1] ]
        #return r

        # 1) convert to lower case
        # 2) remove spaces
        # 3) if category does not end with 'ies', remove the last character

        r = [category]
        category = category.lower()
        category = category.replace(" ","")
        if not category.endswith('ies'):
            category = category[0:-1]
        r += [category]
        return r


    def _is_category_displayed(self,category):

        categories = self._massage_category_names(category)
        for c in categories:
            if self.is_displayed(self.locators['category'] % c):
                return c
        return None


    def goto_category_by_browse(self,category):
        """click on category link"""

        c = self._is_category_displayed(category)

        if not c:
           raise ValueError("cannot find category: '%s'" % (category))

        key = "goto_category_%s" % c
        value = self.locators['catmore'] % c
        self.locators[key] = value
        l = Link(self,key)
        l.detach_from_owner()
        l.click()
        del self.locators[key]


    def goto_category_by_title(self,category):
        """click on category title"""

        c = self._is_category_displayed(category)

        if not c:
           raise ValueError("cannot find category: %s" % (category))

        key = "goto_category_%s" % c
        value = self.locators['cattitlelink'] % c
        self.locators[key] = value
        l = Link(self,key)
        l.detach_from_owner()
        l.click()
        del self.locators[key]


    def get_category_titles(self):
        """return list of category titles"""

        elist = self.find_elements(self.locators['cattitles'])
        return [e.text for e in elist]


    def get_category_classes(self):
        """return list of category classes"""

        elist = self.find_elements(self.locators['catclasses'])
        return [e.get_attribute('class') for e in elist]


class ResourcesCategoryBrowser_Locators_Base(object):
    """locators for ResourcesCategoryBrowser object"""

    locators = {
        'base'          : "css=#content",
        'category'      : "css=.%s",
        'catmore'       : "css=.%s .read-more",
        'cattitles'     : "css=.four.columns.second.third.fourth h3 a",
        'cattitlelink'  : "css=.%s h3 a",
        'catclasses'    : "xpath=//div[contains(@class,'four columns second third fourth')]//h3//a/../..",
    }
