from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class TagsBrowsePage(GenericPage):
    """tags browse"""

    def __init__(self,browser,catalog):
        super(TagsBrowsePage,self).__init__(browser,catalog)
        self.path = "/tags/browse"

        TagsBrowsePage_Locators = self.load_class('TagsBrowsePage_Locators')
        TagsBrowseForm = self.load_class('TagsBrowseForm')

        self.locators.update(TagsBrowsePage_Locators.locators)

        self.form     = TagsBrowseForm(self,{'base':'form'})
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

    def search_result_rows(self):
        return self.form.search_result_rows()

class TagsBrowsePage_Locators_Base_1(object):
    """locators for TagsBrowsePage object"""

    locators = {
        'form'      : "css=#main form",
        'moretags'  : "css=.tag",
    }

class TagsBrowsePage_Locators_Base_2(object):
    """locators for TagsBrowsePage object"""

    locators = {
        'form'      : "css=.main",
        'moretags'  : "css=.tag",
    }
