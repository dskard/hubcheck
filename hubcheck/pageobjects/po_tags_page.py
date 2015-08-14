from hubcheck.pageobjects.po_generic_page import GenericPage

class TagsPage(GenericPage):
    """tags page"""

    def __init__(self,browser,catalog):
        super(TagsPage,self).__init__(browser,catalog)
        self.path = "/tags"

        # load hub's classes
        TagsPage_Locators = self.load_class('TagsPage_Locators')
        Tags              = self.load_class('Tags')

        # update this object's locator
        self.locators.update(TagsPage_Locators.locators)

        # setup page object's components
        self.tags = Tags(self,{'base':'tags'})

    def goto_faq(self):
        self.tags.goto_faq()

    def search_for_content(self,termlist):
        return self.tags.search_for_content(termlist)

    def search_for_tags(self,terms):
        return self.tags.search_for_tags(terms)

    def get_recently_used_tags(self):
        return self.tags.get_recently_used_tags()

    def get_top_100_tags(self):
        return self.tags.get_top_100_tags()

    def goto_recently_used_tag(self,tagname):
        return self.tags.goto_recently_used_tag(tagname)

    def goto_top_100_tag(self,tagname):
        return self.tags.goto_top_100_tag(tagname)

    def goto_all_tags(self):
        return self.tags.goto_all_tags()

class TagsPage_Locators_Base(object):
    """locators for TagsPage object"""

    locators = {
        'tags' : "css=#content",
    }
