from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly, Link

class GroupsWiki(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(GroupsWiki,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWiki_Locators = self.load_class('GroupsWiki_Locators')
        GroupsWikiMenu = self.load_class('GroupsWikiMenu')

        # update this object's locator
        self.locators.update(GroupsWiki_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.newpage  = Link(self,{'base':'newpage'})
        self.title    = TextReadOnly(self,{'base':'title'})
        self.wikimenu = GroupsWikiMenu(self,{'base':'wikimenu'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_wiki_title(self):
        """return the group wiki title"""

        return self.title.value


    def goto_new_wiki_page(self):
        """click the new wiki page link"""

        return self.newpage.click()


    def goto_wikimenu_article(self):
        """click the wiki menu article link"""

        return self.wikimenu.goto_article()


    def goto_wikimenu_edit(self):
        """click the wiki menu edit link"""

        return self.wikimenu.goto_edit()


    def goto_wikimenu_comments(self):
        """click the wiki menu comments link"""

        return self.wikimenu.goto_comments()


    def goto_wikimenu_history(self):
        """click the wiki menu history link"""

        return self.wikimenu.goto_history()


    def goto_wikimenu_delete(self):
        """click the wiki menu delete link"""

        self.wikimenu.goto_delete()


    def goto_wikimenu_mainpage(self):
        """click the wiki menu main page link"""

        self.wikimenu.goto_mainpage()


    def goto_wikimenu_index(self):
        """click the wiki menu index link"""

        self.wikimenu.goto_index()


class GroupsWiki_Locators_Base(object):
    """locators for GroupsWiki object"""

    locators = {
        'base'     : "css=#page_content",
        'newpage'  : "css=#page_content .add",
        'title'    : "css=#sub-content-header h2",
        'wikimenu' : "css=#sub-menu",
    }

class GroupsWiki_Locators_Base_2(object):
    """locators for GroupsWiki object"""

    locators = {
        'base'     : "css=#page_main",
        'newpage'  : "css=#page_main .add",
        'title'    : "css=#sub-content-header h2",
        'wikimenu' : "css=#page_content",
    }

class GroupsWiki_Locators_Base_3(object):
    """locators for GroupsWiki object"""

    locators = {
        'base'     : "css=#page_content",
        'newpage'  : "css=#page_content .add",
        'title'    : "css=#sub-content-header h2",
        'wikimenu' : "css=#page_content .sub-menu",
    }

