from selenium.common.exceptions import NoSuchElementException
from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.widgets.item_list import ItemList

class TicketCommentList(ItemList):
    def __init__(self, owner, locatordict={}):
        super(TicketCommentList,self).__init__(owner,locatordict)

        # load hub's classes
        TicketCommentList_Locators = self.load_class('TicketCommentList_Locators')
        self.TicketComment = self.load_class('TicketComment')

        # update this object's locator
        self.locators.update(TicketCommentList_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def count_comments(self):

        return self.num_rows()


    def get_nth_comment(self,n):

        return self.get_row_by_position(n)


class TicketCommentList_Locators_Base(object):
    """locators for TicketCommentList object"""

    locators = {
        'base'             : "css=.comments",
        'comment-item'     : "css=.comment",
        'ci-base'          : "css=.comment:nth-of-type({row_num})",
        'ci-commenter'     : "css=.comment:nth-of-type({row_num}) .comment-head strong a",
        'ci-body'          : "css=.comment:nth-of-type({row_num}) .comment-body",
        'ci-changes'       : "css=.comment:nth-of-type({row_num}) .changes",
        'ci-notifications' : "css=.comment:nth-of-type({row_num}) .notifications",
    }


