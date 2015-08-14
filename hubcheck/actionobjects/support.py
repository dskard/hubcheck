# support ticket utilities

class Support(object):

    def __init__(self, browser, catalog):

        self.browser = browser
        self.catalog = catalog
        self.logger = self.browser.logger
        self.__my_account_url = '/members/myaccount'


    def open_new_support_ticket(self,data):

        self.logger.debug("opening new support ticket: %s" \
            % (pprint.pformat(data)))

        SupportTicketNewPage = self.catalog.load('SupportTicketNewPage')
        SupportTicketSavePage = self.catalog.load('SupportTicketSavePage')

        po = SupportTicketNewPage(self.browser,self.catalog)
        po.goto_page()
        po.populate_form(data)
        po.submit_ticket(data)

        po = SupportTicketSavePage(self.browser,self.catalog)
        ticket_number = po.get_ticket_number()

        return ticket_number


    def close_support_ticket_invalid(self,ticketNumber):

        self.logger.debug("closing support ticket %s as invalid" \
            % (ticketNumber))

        SupportTicketViewPage = self.catalog.load('SupportTicketViewPage')
        po = SupportTicketViewPage(self.browser,self.catalog,ticketNumber)
        po.goto_page()
        po.add_comment({'status' : 'Invalid'})

        # confirm ticket status is closed
        comment_form_status = po.get_ticket_status()
        if comment_form_status != 'Invalid':
            msg = "comment_form_status =  %s, expected 'Invalid'" \
                    % (comment_form_status)
            self.logger.debug(msg)
            raise Exception(msg)
