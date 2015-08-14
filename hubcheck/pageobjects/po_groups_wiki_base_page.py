from hubcheck.pageobjects.po_groups_base import GroupsBasePage

import re

class GroupsWikiBasePage(GroupsBasePage):
    """groups wiki base page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiBasePage,self).__init__(browser,catalog,groupid)
        self.update_articleid(articleid)

        # load hub's classes
        GroupsWikiBasePage_Locators = self.load_class('GroupsWikiBasePage_Locators')
        GroupsWiki                  = self.load_class('GroupsWiki')

        # update this object's locator
        self.locators.update(GroupsWikiBasePage_Locators.locators)

        # setup page object's components
        self.wikibase     = GroupsWiki(self,{'base':'wikibase'})

    def convert_title_to_articleid(self,title):
        return re.sub(r'\s','',title)

    def update_articleid(self,articleid):
        self.articleid = articleid
        self.path = "/groups/%s/wiki/%s" % (self.groupid,self.articleid)

    def get_wiki_title(self):
        return self.wikibase.get_wiki_title()

    def goto_new_wiki_page(self):
        return self.wikibase.goto_new_wiki_page()

    def goto_wikimenu_article(self):
        return self.wikibase.goto_wikimenu_article()

    def goto_wikimenu_edit(self):
        return self.wikibase.goto_wikimenu_edit()

    def goto_wikimenu_comments(self):
        return self.wikibase.goto_wikimenu_comments()

    def goto_wikimenu_history(self):
        return self.wikibase.goto_wikimenu_history()

    def goto_wikimenu_delete(self):
        self.wikibase.goto_wikimenu_delete()

    def goto_wikimenu_mainpage(self):
        self.wikibase.goto_wikimenu_mainpage()

    def goto_wikimenu_index(self):
        self.wikibase.goto_wikimenu_index()

class GroupsWikiBasePage_Locators_Base(object):
    """locators for GroupsWikiBasePage object"""

    locators = {
        'wikibase' : "css=#page_main"
    }
