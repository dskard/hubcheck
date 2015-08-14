from hubcheck.pageobjects.widgets.ticket_comment_base import TicketCommentBase
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re

class TicketComment(TicketCommentBase):
    def __init__(self, owner, locatordict={}, row_number=0):
        super(TicketComment,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        TicketComment_Locators = self.load_class('TicketComment_Locators')

        # update this object's locator
        self.locators.update(TicketComment_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.changes        = TextReadOnly(self,{'base':'changes'})
        self.notifications  = TextReadOnly(self,{'base':'notifications'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_changes(self):

        try:
            text = self.changes.value
        except:
            text = None
        return text

    def get_status_changes(self):
        """ grabs the old and new status from the
            changes part of the changelog
            returns (oldstatus,newstatus)"""

        changeText = self.get_changes()
        if not changeText:
            return (None,None)
        pattern = re.compile("status changed from \"(\w+)\" to \"(\w+)\"")
        matches = pattern.search(changeText)
        if not matches:
            return (None,None)
        return matches.groups()


    def _is_new_status_x(self,x):

        (oldStatus,newStatus) = self.get_status_changes()
        if newStatus == x:
            return True
        return False


    def is_new_status_new(self):

        return self._is_new_status_x('new')


    def is_new_status_waiting(self):

        return self._is_new_status_x('waiting')


    def is_new_status_resolved(self):

        return self._is_new_status_x('resolved')


    def get_owner_changes(self):
        """grabs the old and new owners from the
           changes part of the changelog
           returns (oldowner,newowner)"""

        changeText = self.get_changes()
        if not changeText:
            return (None,None)
        pattern = re.compile("owner changed from \"(\w+)\" to \"(\w+)\"")
        matches = pattern.search(changeText)
        if not matches:
            return (None,None)
        return matches.groups()


    def get_notifications(self):

        try:
            text = self.notifications.value
        except:
            text = None
        return text


    def get_messaged_notifications(self):
        """ grabs the list of messages sent out [(type,name,email),...]"""

        notificationText = self.get_notifications()
        if not notificationText:
            return None
        pattern = re.compile('Messaged \(([^\)]+)\) (.+) - (.+)')
        return pattern.findall(notificationText)


class TicketComment_Locators_Base(object):
    """
    locators for TicketComment object
    """

    locators = {
        'base'          : "css=.comment",
        'commenter'     : "css=.comment-title a",
        'body'          : "css=.comment-content p:nth-of-type(2)",
        'attachments'   : None,
        'changes'       : "css=.changes",
        'notifications' : "css=.notifications",
    }

class TicketComment_Locators_Base_2(object):
    """
    locators for TicketComment object found on dev.hubzero.org
    """

    locators = {
        'base'          : "css=.comment",
        'commenter'     : "css=.comment-head strong a",
        'body'          : "css=.comment-body",
        'attachments'   : None,
        'changes'       : "css=.changes",
        'notifications' : "css=.notifications",
    }


class TicketComment_Locators_Base_3(object):
    """
    locators for TicketComment with attachments section
    """

    locators = {
        'base'          : "css=.comment:nth-of-type({row_num})",
        'commenter'     : "css=.comment:nth-of-type({row_num}) .comment-head strong a",
        'body'          : "css=.comment:nth-of-type({row_num}) .comment-body",
        'attachments'   : "css=.comment:nth-of-type({row_num}) .comment-attachments",
        'changes'       : "css=.comment:nth-of-type({row_num}) .changes",
        'notifications' : "css=.comment:nth-of-type({row_num}) .notifications",
    }

