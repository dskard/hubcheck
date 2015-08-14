from hubcheck.pageobjects.po_generic_page import GenericPage

class SupportPage(GenericPage):
    """support page"""

    def __init__(self,browser,catalog):
        super(SupportPage,self).__init__(browser,catalog)
        self.path = "/support"

        # load hub's classes
        SupportPage_Locators = self.load_class('SupportPage_Locators')
        Support = self.load_class('Support')

        # update this object's locator
        self.locators.update(SupportPage_Locators.locators)

        # setup page object's components
        self.support = Support(self,{'base':'support'})

    def goto_quicklink_kb(self):
        self.support.goto_quicklink_kb()

    def goto_quicklink_report(self):
        self.support.goto_quicklink_report()

    def goto_quicklink_track(self):
        self.support.goto_quicklink_track()

    def goto_content_resources(self):
        self.support.goto_content_resources()

    def goto_content_tags(self):
        self.support.goto_content_tags()

    def goto_content_search(self):
        self.support.goto_content_search()

    def goto_community_questions(self):
        self.support.goto_community_questions()

    def goto_community_wishlist(self):
        self.support.goto_community_wishlist()

    def goto_community_topics(self):
        self.support.goto_community_topics()

    def goto_support_kb(self):
        self.support.goto_support_kb()

    def goto_support_report(self):
        self.support.goto_support_report()

    def goto_support_track(self):
        self.support.goto_support_track()

class SupportPage_Locators_Base(object):
    """locators for SupportPage object"""

    locators = {
        'support' : "css=#content",
    }
