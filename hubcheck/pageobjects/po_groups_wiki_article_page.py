from hubcheck.pageobjects.po_groups_wiki_base_page import GroupsWikiBasePage

class GroupsWikiArticlePage(GroupsWikiBasePage):
    """groups wiki article page"""

    def __init__(self,browser,catalog,groupid,articleid):
        super(GroupsWikiArticlePage,self).__init__(browser,catalog,groupid,articleid)
        # self.path is supplied by GroupsWikiBasePage

        # load hub's classes
        GroupsWikiArticlePage_Locators = self.load_class('GroupsWikiArticlePage_Locators')
        GroupsWikiArticle              = self.load_class('GroupsWikiArticle')

        # update this object's locator
        self.locators.update(GroupsWikiArticlePage_Locators.locators)

        # setup page object's components
        self.article      = GroupsWikiArticle(self,{'base':'article'})

    def get_tags(self):
        return self.article.get_tags()

    def click_tag(self,tagname):
        return self.article.click_tag(tagname)

    def get_page_text(self):
        return self.article.get_page_text()

    def get_authors(self):
        return self.article.get_authors()

    def is_created(self):
        return self.article.is_created()

    def create_page(self):
        return self.article.create_page()

    def download_attachment(self,attachment):
        return self.article.download_attachment(attachment)

    def is_file_attached(self,filepath):
        return self.article.is_file_attached(filepath)

class GroupsWikiArticlePage_Locators_Base(object):
    """locators for GroupsWikiArticlePage object"""

    locators = {
        'article' : "css=#page_content",
    }
