from hubcheck.pageobjects.po_hubucoursemanage import HubUCourseManagePage

#import re
#
#notifications = {
#    'emails_sent'     : u'You successfully sent \d+ emails.',
#}

class HubUCourseManageDashboardPage(HubUCourseManagePage):
    """hub u course manager dashboard"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseManageDashboardPage,self).__init__(browser,catalog,groupid)

        # load hub's classes
        HubUCourseManageDashboardPage_Locators = self.load_class('HubUCourseManageDashboardPage_Locators')
        DashboardTickets    = self.load_class('DashboardTickets')
        DashboardMembership = self.load_class('DashboardMembership')

        # update this object's locator
        self.locators.update(HubUCourseManageDashboardPage_Locators.locators)

        # setup page object's components
        self.ticket_count     = DashboardTickets(self,{'base':'tickets'})
        self.membership_count = DashboardMembership(self,{'base':'membership'})

    def goto_page(self):
        super(HubUCourseManageDashboardPage,self).goto_page()
        self.tabs.dashboard.click()

    def active_members_count(self):
        return self.membership_count.active_members_count()

    def pending_invitees_count(self):
        return self.membership_count.pending_invitees_count()

    def closed_tickets_count(self):
        return self.ticket_count.closed_tickets_count()

    def open_tickets_count(self):
        return self.ticket_count.open_tickets_count()

    def unassigned_tickets_count(self):
        return self.ticket_count.unassigned_tickets_count()

    def open_this_week_count(self):
        return self.ticket_count.open_this_week_count()

    def avg_lifetime_count(self):
        return self.ticket_count.avg_lifetime_count()

#    def check_for_notification(self,notification):
#        """do not use this function, use the notification specific one"""
#        r = notifications[notification]
#        e = self.find_element(self.locators['notification'])
#        return (re.search(r,e.text) != None)
#
#    def is_notification_emails_sent(self):
#        return self.check_for_notification('emails_sent')

class HubUCourseManageDashboardPage_Locators_Base(object):
    """locators for HubUCourseManageDashboardPage object"""

    locators = {
        'menu'          : "css=#course-menu",
        'logout'        : "css=#logout",
        'tickets'       : "css=#dashboard .support",
        'membership'    : "css=#dashboard .membership",
#        'notification'  : "css=#course-notice",
    }

