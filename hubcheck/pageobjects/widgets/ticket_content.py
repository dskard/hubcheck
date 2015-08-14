from hubcheck.pageobjects.widgets.ticket_comment_base import TicketCommentBase

class TicketContent(TicketCommentBase):
    def __init__(self, owner, locatordict={}):
        super(TicketContent,self).__init__(owner,locatordict)

        # load hub's classes
        TicketContent_Locators = self.load_class('TicketContent_Locators')

        # update this object's locator
        self.locators.update(TicketContent_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()

class TicketContent_Locators_Base_1(object):
    """locators for TicketContent object"""

    locators = {
        'base'      : "css=.ticket",
        'commenter' : "css=.ticket-title strong a",
        'body'      : "css=.ticket-content p:nth-of-type(2)",
    }

class TicketContent_Locators_Base_2(object):
    """locators for TicketContent object"""

    locators = {
        'base'      : "css=.ticket",
        'commenter' : "css=.entry-title strong a",
        'body'      : "css=.entry-body",
    }

