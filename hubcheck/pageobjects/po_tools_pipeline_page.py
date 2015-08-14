from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class ToolsPipelinePage(GenericPage):
    """page that lists all tool resources"""

    def __init__(self,browser,catalog):
        super(ToolsPipelinePage,self).__init__(browser,catalog)
        self.path = "/tools/pipeline"

        # load hub's classes
        ToolsPipelinePage_Locators = self.load_class('ToolsPipelinePage_Locators')
        ToolsPipelineSearchForm = self.load_class('ToolsPipelineSearchForm')

        # update this object's locator
        self.locators.update(ToolsPipelinePage_Locators.locators)

        # setup page object's components
        self.form = ToolsPipelineSearchForm(self,{'base':'form'})

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


    def get_current_page_number(self):
        return self.form.get_current_page_number()


    def get_link_page_numbers(self):
        return self.form.get_link_page_numbers()


    def search_result_rows(self):
        return self.form.search_result_rows()


class ToolsPipelinePage_Locators_Base(object):
    """locators for ToolsPipelinePage object"""

    locators = {
        'form'      : "css=.main form",
    }
