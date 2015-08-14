from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import TextReadOnly

class SupportTicketViewPage(GenericPage):
    """support ticket view"""

    def __init__(self,browser,catalog,ticketid=''):
        super(SupportTicketViewPage,self).__init__(browser,catalog)
        self.ticketid = str(ticketid)
        self.path = "/support/ticket/%s" % (self.ticketid)

        # load hub's classes
        SupportTicketViewPage_Locators = self.load_class('SupportTicketViewPage_Locators')
        TicketContent     = self.load_class('TicketContent')
        TicketCommentForm = self.load_class('TicketCommentForm')
        ItemList          = self.load_class('ItemList')
        TicketComment     = self.load_class('TicketComment')

        # update this object's locator
        self.locators.update(SupportTicketViewPage_Locators.locators)

        # setup page object's components
        self.ticket       = TicketContent(self,{'base':'ticket-content'})
        self.status       = TextReadOnly(self,{'base':'ticket-status'})
        self.commentlist  = ItemList(self,
                                 {
                                    'base' : 'comment-list',
                                    'row'  : 'comment-item',
                                 }, TicketComment, {})
        self.commentform  = TicketCommentForm(self,{'base':'comment-form'})

    def add_comment(self,data):
        return self.commentform.add_comment(data)

    def get_ticket_author(self):
        return self.ticket.get_commenter()

    def get_ticket_body(self):
        return self.ticket.get_body()

    def get_ticket_content(self):
        return self.ticket

    def get_nth_comment(self,n):
        return self.commentlist.get_row_by_position(n)

    def get_status(self):
        return self.status.value

    def get_ticket_status(self):
        return self.commentform.get_status()


class SupportTicketViewPage_Locators_Base(object):
    """locators for SupportTicketViewPage object"""

    locators = {
        'ticket-content'   : "css=.ticket",
        'ticket-status'    : "css=.ticket-status",
        'comment-list'     : "css=.comments",
        'comment-item'     : "css=.comment",
        'comment-form'     : "css=#commentform",
    }
