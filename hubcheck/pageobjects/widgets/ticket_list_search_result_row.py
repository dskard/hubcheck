from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import TextReadOnly, Link

class TicketListSearchResultRow(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketListSearchResultRow,self).__init__(owner,locatordict)

        # load hub's classes
        TicketListSearchResultRow_Locators = self.load_class('TicketListSearchResultRow_Locators')
        TagsList = self.load_class('TagsList')

        # update this object's locator
        self.locators.update(TicketListSearchResultRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.ticketnumber = TextReadOnly(self,{'base':'ticketnumber'})
        self.summary      = Link(self,{'base':'summary'})
        self.status       = TextReadOnly(self,{'base':'status'})
        self.group        = TextReadOnly(self,{'base':'group'})
        self.tags         = TagsList(self,{'base':'tags'})
        self.assignee     = TextReadOnly(self,{'base':'assignee'})
        # self.age          = TextReadOnly(self,{'base':'age'})
        # self.comments     = TextReadOnly(self,{'base':'comments'})
        self.delete       = Link(self,{'base':'delete'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsAdmin(self,widgets=None,cltype='Admin'):

        widgets = [self.ticketnumber,self.summary,self.status,self.group,
                   self.assignee,self.delete]
                  # self.assignee,self.age,self.comments,self.delete]
        self._checkLocators(widgets,cltype)


    def _checkLocatorsNonAdmin(self,widgets=None,cltype='NonAdmin'):

        widgets = [self.ticketnumber,self.summary,self.status,self.group,
                   self.assignee]
                  # self.assignee,self.age,self.comments]
        self._checkLocators(widgets,cltype)


    def open_ticket(self):

        self.summary.click()


    def delete_ticket(self):

        self.delete.click()


class TicketListSearchResultRow_Locators_Base_1(object):
    """locators for TicketListSearchResultRow object"""

    locators = {
        'base'           : "css=#tktlist tbody tr",
        'ticketnumber'   : "css=td:nth-of-type(1)",
        'summary'        : "css=td:nth-of-type(2)",
        'status'         : "css=td:nth-of-type(3)",
        'group'          : "css=td:nth-of-type(4)",
        'assignee'       : "css=td:nth-of-type(5)",
        'age'            : "css=td:nth-of-type(6)",
        'comments'       : "css=td:nth-of-type(7)",
        'delete'         : "css=.delete",
        'tags'           : "css=.tags",
    }

class TicketListSearchResultRow_Locators_Base_2(object):
    """locators for TicketListSearchResultRow object"""

    locators = {
        'base'           : "css=#tktlist tbody tr",
        'ticketnumber'   : "css=.ticket-id",
        'summary'        : "css=.ticket-content",
        'status'         : "css=.status",
        'group'          : "css=.ticket-group",
        'assignee'       : "css=.ticket-owner",
        'activity'       : "css=.ticket-activity",
        'delete'         : "css=.delete",
        'tags'           : "css=.tags",
    }
