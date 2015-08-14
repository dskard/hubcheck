from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class Tags(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Tags,self).__init__(owner,locatordict)

        # load hub's classes
        Tags_Locators = self.load_class('Tags_Locators')
        TagSearchBox = self.load_class('TagSearchBox')
        TextSearchBox = self.load_class('TextSearchBox')
        TagsList = self.load_class('TagsList')

        # update this object's locator
        self.locators.update(Tags_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.faq              = Link(self,{'base':'faq'})
        self.alltags          = Link(self,{'base':'alltags'})
        self.searchcontentbox = TagSearchBox(self,
                                    {'base'   : 'searchcontentbox',
                                     'submit' : 'searchcontentsubmit'})
        self.searchtagsbox    = TextSearchBox(self,
                                    {'base'   : 'searchtagsbox',
                                     'text'   : 'searchtagstext',
                                     'submit' : 'searchtagssubmit'})

        self.recenttags       = TagsList(self,{'base':'recenttags',
                                               'taglink':'recenttags_link'})
        self.top100tags       = TagsList(self,{'base':'top100tags',
                                               'taglink':'top100tags_link'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_faq(self):
        """click the faq link"""

        self.faq.click()


    def search_for_content(self,termslist):
        """perform a search for resources using the tags in the list termslist"""

        return self.searchcontentbox.search_for(termslist)


    def search_for_tags(self,terms):
        """perform a search for tags like those in the list terms"""

        return self.searchtagsbox.search_for(terms)


    def get_recently_used_tags(self):
        """return the list of recently used tags"""

        return self.recenttags.get_tags()


    def get_top_100_tags(self):
        """return the list of top 100 tags"""

        return self.top100tags.get_tags()


    def goto_recently_used_tag(self,tagname):
        """click a tag in the recently used list"""

        return self.recenttags.click_tag(tagname)


    def goto_top_100_tag(self,tagname):
        """click a tag in the top 100 list"""

        return self.top100tags.click_tag(tagname)


    def goto_all_tags(self):
        """click the all tags link"""

        return self.alltags.click()


class Tags_Locators_Base_1(object):
    """locators for Tags object"""

    locators = {
        'base'                : "css=#content",
        'faq'                 : "css=.aside li:nth-of-type(1) a",
        'alltags'             : "css=.browse a",
        'searchcontentbox'    : "css=form[action='/tags/view']",
        'searchcontentsubmit' : "css=form[action='/tags/view'] [type='submit']",
        'searchtagsbox'       : "css=form[action='/tags/browse']",
        'searchtagstext'      : "css=#tsearch",
        'searchtagssubmit'    : "css=form[action='/tags/browse'] [type='submit']",
        'recenttags'          : "css=.section > div:nth-of-type(5) ol",
        'recenttags_link'     : "css=.section > div:nth-of-type(5) ol a",
        'top100tags'          : "css=.section > div:nth-of-type(8) ol",
        'top100tags_link'     : "css=.section > div:nth-of-type(8) ol a",
    }

class Tags_Locators_Base_2(object):
    """locators for Tags object
       updated recenttags and top100tags locators
    """

    locators = {
        'base'                : "css=#content",
        'faq'                 : "css=.aside li:nth-of-type(1) a",
        'alltags'             : "css=.browse a",
        'searchcontentbox'    : "css=form[action='/tags/view']",
        'searchcontentsubmit' : "css=form[action='/tags/view'] [type='submit']",
        'searchtagsbox'       : "css=form[action='/tags/browse']",
        'searchtagstext'      : "css=#tsearch",
        'searchtagssubmit'    : "css=form[action='/tags/browse'] [type='submit']",
        'recenttags'          : "css=.section > div:nth-of-type(2) .tags",
        'recenttags_link'     : "css=.section > div:nth-of-type(2) .tags a",
        'top100tags'          : "css=.section > div:nth-of-type(3) .tags",
        'top100tags_link'     : "css=.section > div:nth-of-type(3) .tags a",
    }
