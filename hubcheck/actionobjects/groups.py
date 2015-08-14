# groups utilities

import pprint


class Groups(object):

    def __init__(self, browser, catalog):

        self.browser = browser
        self.catalog = catalog
        self.logger = self.browser.logger


    def create_group(self,groupid,data):

        self.logger.debug("creating user group %s: %s" \
            % (groupid, pprint.pformat(data)))

        # create the group page if necessary
        GroupsOverviewPage = self.catalog.load('GroupsOverviewPage')
        po = GroupsOverviewPage(self.browser,self.catalog,groupid)
        po.goto_page()

        if po.group_exists():
            return False

        GroupsNewPage = self.catalog.load('GroupsNewPage')
        po = GroupsNewPage(self.browser,self.catalog)
        po.goto_page()
        po.create_group(data)

        return True


    def create_group_wiki(self,groupid,articleid,data):

        self.logger.debug("creating group wiki page %s -> %s: %s" \
            % (groupid, articleid, pprint.pformat(data)))

        # create a new group wiki page if necessary
        GroupsWikiArticlePage = self.catalog.load('GroupsWikiArticlePage')
        po = GroupsWikiArticlePage(self.browser,self.catalog,groupid,articleid)
        po.goto_page()

        # check to see if the page has already been created
        if po.is_created():
            self.logger.debug("group wiki page already exists")
            return False

        # create the page
        po.create_page()

        GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        po = GroupsWikiNewPage(self.browser,self.catalog,groupid)
        po.create_wiki_page(data)

        ## we do it this way because pressing the "create it?"
        ## is broken and leads to a blank page
        ## hubzero ticket #1713
        #GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        #po = GroupsWikiNewPage(self.browser,self.catalog,groupid)
        #po.goto_page()
        #po.create_wiki_page(articledata)

        ## check the page was created
        #po = GroupsWikiArticlePage(self.browser,self.catalog,groupid,wikipagename)
        #po.goto_page()
        #self.assertTrue(po.is_created() == True, 'Wiki page not created')
        #self.assertTrue(po.get_wiki_title() == data['title'])
        #self.assertTrue(po.get_page_text() == data['pagetext'])

        return True
