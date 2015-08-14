from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class DashboardTickets(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(DashboardTickets,self).__init__(owner,locatordict)

        # load hub's classes
        DashboardTickets_Locators = self.load_class('DashboardTickets_Locators')

        # update this object's locator defaults
        self.locators.update(DashboardTickets_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.closed_tickets       = TextReadOnly(self,{'base':'closed'})
        self.open_tickets         = TextReadOnly(self,{'base':'open'})
        self.unassigned_tickets   = TextReadOnly(self,{'base':'unassigned'})
        self.open_this_week       = TextReadOnly(self,{'base':'thisweek'})
        self.avg_lifetime         = TextReadOnly(self,{'base':'lifetime'})
        self.course_tickets       = Link(self,{'base':'course_tickets'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def closed_tickets_count(self):
        """return the value of the closed tickets column"""

        return self.closed_tickets.value


    def open_tickets_count(self):
        """return the value of the open tickets column"""

        return self.open_tickets.value


    def unassigned_tickets_count(self):
        """return the value of the unassigned tickets column"""

        return self.unassigned_tickets.value


    def open_this_week_count(self):
        """return the value of the open this week column"""

        return self.open_this_week.value


    def avg_lifetime_count(self):
        """return the value of the average lifetime column as a 3-tuple"""

        text = self.avg_lifetime.value
        pattern = re.compile('(\d+) days (\d+) hours (\d+) minutes')
        days,hours,minutes = pattern.match(text).groups()
        # [days,junk,hours,junk,minutes,junk] = avg_lifetime.split(' ')
        return days,hours,minutes


class DashboardTickets_Locators_Base(object):
    """locators for DashboardTickets object"""

    locators = {
        'base'              : "css=#dashboard .support",
        'closed'            : "css=.closed .count",
        'open'              : "css=.open .count",
        'unassigned'        : "css=.unassigned .count",
        'thisweek'          : "css=.thisweek .count",
        'lifetime'          : "css=.lifetime .count",
        'course_tickets'    : "css=.top-link",
    }

