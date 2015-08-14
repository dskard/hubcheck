from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class GroupsWikiMenu1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsWikiMenu1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiMenu_Locators = self.load_class('GroupsWikiMenu_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.article  = Link(self,{'base':'article'})
        self.edit     = Link(self,{'base':'edit'})
        self.comments = Link(self,{'base':'comments'})
        self.history  = Link(self,{'base':'history'})
        self.delete   = Link(self,{'base':'delete'})
        self.mainpage = Link(self,{'base':'mainpage'})
        self.index    = Link(self,{'base':'index'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_article(self):
        """click the article menu link"""

        self.article.click()


    def goto_edit(self):
        """click the edit menu link"""

        self.edit.click()


    def goto_comments(self):
        """click the comments menu link"""

        self.comments.click()


    def goto_history(self):
        """click the history menu link"""

        self.history.click()


    def goto_delete(self):
        """click the delete  menu link"""

        self.delete.click()


    def goto_mainpage(self):
        """click the main page menu link"""

        self.mainpage.click()


    def goto_index(self):
        """click the index menu link"""

        self.index.click()


class GroupsWikiMenu1_Locators_Base(object):
    """locators for GroupsWikiMenu object"""

    locators = {
        'base'     : "css=#sub-menu",
        'article'  : "css=.page-text",
        'edit'     : "css=.page-edit",
        'comments' : "css=.page-comments",
        'history'  : "css=.page-history",
        'delete'   : "css=.page-delete",
        'mainpage' : "css=.page-main",
        'index'    : "css=.page-index",
    }


class GroupsWikiMenu1_Locators_Base_2(object):
    """
        locators for GroupsWikiMenu object

        used by nees62
    """

    locators = {
        'base'     : "css=#page_content",
        'article'  : "css=.page-text",
        'edit'     : "css=.page-edit",
        'comments' : "css=.page-comments",
        'history'  : "css=.page-history",
        'delete'   : "css=.page-delete",
        'mainpage' : "css=.home",
        'index'    : "css=.page-index",
    }


class GroupsWikiMenu2(BasePageWidget):
    """
        removed mainpage link
        added search link
    """

    def __init__(self, owner, locatordict={}):
        super(GroupsWikiMenu2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiMenu_Locators = self.load_class('GroupsWikiMenu_Locators')

        # update this object's locator
        self.locators.update(GroupsWikiMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.article  = Link(self,{'base':'article'})
        self.edit     = Link(self,{'base':'edit'})
        self.comments = Link(self,{'base':'comments'})
        self.history  = Link(self,{'base':'history'})
        self.delete   = Link(self,{'base':'delete'})
        self.search   = Link(self,{'base':'search'})
        self.index    = Link(self,{'base':'index'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_article(self):
        """click the article menu link"""

        self.article.click()


    def goto_edit(self):
        """click the edit menu link"""

        self.edit.click()


    def goto_comments(self):
        """click the comments menu link"""

        self.comments.click()


    def goto_history(self):
        """click the history menu link"""

        self.history.click()


    def goto_delete(self):
        """click the delete menu link"""

        self.delete.click()


    def goto_search(self):
        """click the search menu link"""

        self.search.click()


    def goto_index(self):
        """click the index menu link"""

        self.index.click()


class GroupsWikiMenu2_Locators_Base(object):
    """locators for GroupsWikiMenu object"""

    locators = {
        'base'     : "css=#sub-menu",
        'article'  : "css=.page-text",
        'edit'     : "css=.page-edit",
        'comments' : "css=.page-comments",
        'history'  : "css=.page-history",
        'delete'   : "css=.page-delete",
        'search'   : "css=.page-search",
        'index'    : "css=.page-index",
    }



