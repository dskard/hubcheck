from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class TagsViewPage(GenericPage):
    """tags view"""

    def __init__(self,browser,catalog):
        super(TagsViewPage,self).__init__(browser,catalog)
        self.path = "/tags/browse"

        TagsViewPage_Locators = self.load_class('TagsViewPage_Locators')
        TagsViewForm = self.load_class('TagsViewForm')

        self.locators.update(TagsViewPage_Locators.locators)

        self.form     = TagsViewForm(self,{'base':'form'})
        self.moretags = Link(self,{'base':'moretags'})

    def search_for(self,terms):
        return self.form.search_for(terms)

    def goto_page_number(self,pagenumber):
        return self.form.goto_page_number(pagenumber)

    def goto_page_relative(self,relation):
        return self.form.goto_page_relative(relation)

    def get_caption_counts(self):
        return self.form.get_caption_counts()

    def get_pagination_counts(self):
        return self.form.get_pagination_counts()

    def goto_more_tags(self):
        return self.moretags.click()

    def get_current_page_number(self):
        return self.form.get_current_page_number()

    def get_link_page_numbers(self):
        return self.form.get_link_page_numbers()

    def rows(reset=False):
        return self.form.rows

class TagsViewPage_Locators_Base_1(object):
    """locators for TagsViewPage object"""

    locators = {
        'form'      : "css=#main form",
        'moretags'  : "css=.tag",
    }

class TagsViewPage_Locators_Base_2(object):
    """locators for TagsViewPage object"""

    locators = {
        'form'      : "css=.main",
        'moretags'  : "css=.tag",
    }
