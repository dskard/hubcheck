from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class Support(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Support,self).__init__(owner,locatordict)

        # load hub's classes
        Support_Locators = self.load_class('Support_Locators')

        # update this object's locator
        self.locators.update(Support_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.quicklink_kb       = Link(self,{'base':'quicklink_kb'})
        self.quicklink_report   = Link(self,{'base':'quicklink_report'})
        self.quicklink_track    = Link(self,{'base':'quicklink_track'})

        self.content_resources  = Link(self,{'base':'content_resources'})
        self.content_tags       = Link(self,{'base':'content_tags'})
        self.content_search     = Link(self,{'base':'content_search'})

        self.community_questions = Link(self,{'base':'community_questions'})
        self.community_wishlist  = Link(self,{'base':'community_wishlist'})
        self.community_topics    = Link(self,{'base':'community_topics'})

        self.support_kb         = Link(self,{'base':'support_kb'})
        self.support_report     = Link(self,{'base':'support_report'})
        self.support_track      = Link(self,{'base':'support_track'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_quicklink_kb(self):
        """click the knowledgebase link"""

        self.quicklink_kb.click()


    def goto_quicklink_report(self):
        """click the report problems link"""

        self.quicklink_report.click()


    def goto_quicklink_track(self):
        """click the track tickets link"""

        self.quicklink_track.click()


    def goto_content_resources(self):

        self.content_resources.click()


    def goto_content_tags(self):

        self.content_tags.click()


    def goto_content_search(self):

        self.content_search.click()


    def goto_community_questions(self):

        self.community_questions.click()


    def goto_community_wishlist(self):

        self.community_wishlist.click()


    def goto_community_topics(self):

        self.community_topics.click()


    def goto_support_kb(self):

        self.support_kb.click()


    def goto_support_report(self):

        self.support_report.click()


    def goto_support_track(self):

        self.support_track.click()


    # FIXME: missing the category titles
    #        in /resources we use ResourceCategoryBrowser
    #        which has the extra function goto_category_by_browse()


class Support_Locators_Base(object):
    """locators for Support object"""

    locators = {
        'base'                  : "css=#content",
        'quicklink_kb'          : "css=.aside li:nth-of-type(1) a",
        'quicklink_report'      : "css=.aside li:nth-of-type(2) a",
        'quicklink_track'       : "css=.aside li:nth-of-type(3) a",
        'content_resources'     : "css=.presentation p a",
        'content_tags'          : "css=.tag p a",
        'content_search'        : "css=.search p a",
        'community_questions'   : "css=.feedback p a",
        'community_wishlist'    : "css=.idea p a",
        'community_topics'      : "css=.wiki p a",
        'support_kb'            : "css=.series p a",
        'support_report'        : "css=.note p a",
        'support_track'         : "css=.ticket p a",
    }

class Support2(Support):
    def __init__(self, owner, locatordict=None):
        super(Support2,self).__init__(owner,locatordict)

        # setup page object's components
        self.quicklink_faq      = Link(self,{'base':'quicklink_faq'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_quicklink_faq(self):
        """click the faq link"""

        self.quicklink_faq.click()


class Support2_Locators_Base(object):
    """locators for Support object"""

    locators = {
        'base'                  : "css=#content",
        'quicklink_faq'         : "css=.aside li:nth-of-type(1) a",
        'quicklink_kb'          : "css=.aside li:nth-of-type(2) a",
        'quicklink_report'      : "css=.aside li:nth-of-type(3) a",
        'quicklink_track'       : "css=.aside li:nth-of-type(4) a",
        'content_resources'     : "css=.presentation p a",
        'content_tags'          : "css=.tag p a",
        'content_search'        : "css=.search p a",
        'community_questions'   : "css=.feedback p a",
        'community_wishlist'    : "css=.idea p a",
        'community_topics'      : "css=.wiki p a",
        'support_kb'            : "css=.series p a",
        'support_report'        : "css=.note p a",
        'support_track'         : "css=.ticket p a",
    }


class Support3(BasePageWidget):
    """This is an old style support page object
       from osr-1.1.0 time frame, with no quicklinks
    """

    def __init__(self, owner, locatordict=None):
        super(Support3,self).__init__(owner,locatordict)

        # load hub's classes
        Support_Locators = self.load_class('Support_Locators')

        # update this object's locator
        self.locators.update(Support_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.header_kb          = Link(self,{'base':'header_kb'})
        self.kb_kb              = Link(self,{'base':'kb_kb'})
        self.kb_tools           = Link(self,{'base':'kb_tools'})
        self.header_answers     = Link(self,{'base':'header_answers'})
        self.answers_kb         = Link(self,{'base':'answers_kb'})
        self.answers_ask        = Link(self,{'base':'answers_ask'})
        self.answers_search     = Link(self,{'base':'answers_search'})
        self.header_report      = Link(self,{'base':'header_report'})
        self.report_problems    = Link(self,{'base':'report_problems'})
        self.report_tickets     = Link(self,{'base':'report_tickets'})
        self.feedback_report    = Link(self,{'base':'feedback_report'})
        self.feedback_share     = Link(self,{'base':'feedback_share'})
        self.feedback_suggest   = Link(self,{'base':'feedback_suggest'})

        # update the component's locators with this objects overrides
        self._updateLocators()


class Support3_Locators_Base_1(object):
    """locators for Support object"""

    locators = {
        'base'                  : "css=#content",
        'header_kb'             : "css=#kb h3 a",
        'kb_kb'                 : "css=#kb p a:nth-of-type(2)",
        'kb_tools'              : "css=#kb p a:nth-of-type(1)",
        'header_answers'        : "css=#na h3 a",
        'answers_kb'            : "css=#na p a:nth-of-type(1)",
        'answers_ask'           : "css=#na p a:nth-of-type(2)",
        'answers_search'        : "css=#na p a:nth-of-type(3)",
        'header_report'         : "css=#rp h3 a",
        'report_problems'       : "css=#rp p a:nth-of-type(1)",
        'report_tickets'        : "css=#rp p a:nth-of-type(2)",
        'feedback_report'       : "css=.farright li a:nth-of-type(1)",
        'feedback_share'        : "css=.farright li a:nth-of-type(2)",
        'feedback_suggest'      : "css=.farright li a:nth-of-type(3)",
    }


