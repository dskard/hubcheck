from hubcheck.pageobjects.basepagewidget import BasePageWidget

class MembersDashboardTable1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersDashboardTable1,self).__init__(owner,locatordict)

        # load hub's classes
        MembersDashboardTable1_Locators     = self.load_class('MembersDashboardTable_Locators')
#        MembersDashboardMyContributions     = self.load_class('MembersDashboardMyContributions')
#        MembersDashboardMyGroups            = self.load_class('MembersDashboardMyGroups')
#        MembersDashboardMyHUBIntroduction   = self.load_class('MembersDashboardMyHUBIntroduction')
#        MembersDashboardMyMessages          = self.load_class('MembersDashboardMyMessages')
#        MembersDashboardMyProjects          = self.load_class('MembersDashboardMyProjects')
#        MembersDashboardMyQuestions         = self.load_class('MembersDashboardMyQuestions')
        MembersDashboardMySessions          = self.load_class('MembersDashboardMySessions')
#        MembersDashboardMySubmissions       = self.load_class('MembersDashboardMySubmissions')
#        MembersDashboardMyTickets           = self.load_class('MembersDashboardMyTickets')
#        MembersDashboardMyTools             = self.load_class('MembersDashboardMyTools')
#        MembersDashboardMyWishes            = self.load_class('MembersDashboardMyWishes')
#        MembersDashboardResources           = self.load_class('MembersDashboardResources')

        # update this object's locator
        self.locators.update(MembersDashboardTable1_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
#        self.my_contributions       = MembersDashboardMyContributions(self,{'base':'my_contributions'})
#        self.my_groups              = MembersDashboardMyGroups(self,{'base':'my_groups'})
#        self.my_hub_introduction    = MembersDashboardMyHUBIntroduction(self,{'base':'my_hub_intro'})
#        self.my_messages            = MembersDashboardMyMessages(self,{'base':'my_messages'})
#        self.my_projects            = MembersDashboardMyProjects(self,{'base':'my_projects'})
#        self.my_questions           = MembersDashboardMyQuestions(self,{'base':'my_questions'})
        self.my_sessions            = MembersDashboardMySessions(self,{'base':'my_sessions'})
#        self.my_submissions         = MembersDashboardMySubmissions(self,{'base':'my_submissions'})
#        self.my_tickets             = MembersDashboardMyTickets(self,{'base':'my_tickets'})
#        self.my_tools               = MembersDashboardMyTools(self,{'base':'my_tools'})
#        self.my_wishes              = MembersDashboardMyWishes(self,{'base':'my_wishes'})
#        self.resources              = MembersDashboardResources(self,{'base':'resources'})

        # update the component's locators with this objects overrides
        self._updateLocators()


class MembersDashboardTable1_Locators_Base(object):
    """locators for MembersProfileForm object"""

    locators = {
        'base'              : "css=#droppables",
        'my_contributions'  : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Contributions')]/..",
        'my_groups'         : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Groups')]/..",
        'my_hub_into'       : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'MyHUB Introduction')]/..",
        'my_messages'       : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Messages')]/..",
        'my_projects'       : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Projects')]/..",
        'my_questions'      : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Questions')]/..",
        'my_sessions'       : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Sessions')]/..",
        'my_submissions'    : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Submissions')]/..",
        'my_tickets'        : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Tickets')]/..",
        'my_tools'          : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Tools')]/..",
        'my_wishes'         : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Wishes')]/..",
        'resources'         : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'Resources')]/..",
    }
