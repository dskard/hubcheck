from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
import re

class TicketSave(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TicketSave,self).__init__(owner,locatordict)

        # load hub's classes
        TicketSave_Locators = self.load_class('TicketSave_Locators')

        # update this object's locator
        self.locators.update(TicketSave_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.ticket = TextReadOnly(self,{'base':'ticket'})
        self.track  = Link(self,{'base':'track'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_ticket_number(self):

        self.logger.debug('ticket.value = \'%s\'' % (self.ticket.value))

        pattern = re.compile("(\d+)")
        matches = pattern.search(self.ticket.value)
        ticket_number = None

        if matches:
            ticket_number = matches.group(1)

        self.logger.info('ticket number = %s' % (ticket_number))

        return ticket_number


    def goto_tracking_system(self):

        return self.track.click()


class TicketSave_Locators_Base(object):
    """
    locators for TicketSave object

    still used on old hub installations like:
    c3bio.org
    pharmahub.org
    water-hub.org
    """

    locators = {
        'base'           : "css=.main",
        'ticket'         : "css=.main strong",
        'track'          : "xpath=//a[text()='our tracking system']",
    }


class TicketSave_Locators_Base_3(object):
    """
    locators for TicketSave object

    updated ticket and track locators
    """

    locators = {
        'base'           : "css=#main",
        'ticket'         : "css=#ticket-number",
        'track'          : "css=#messagebox a",
    }

