from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly


class MembersDashboardMySessions(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(MembersDashboardMySessions,self).__init__(owner,locatordict)

        # load hub's classes
        MembersDashboardMySessions_Locators = self.load_class('MembersDashboardMySessions_Locators')
        ItemList = self.load_class('ItemList')
        MembersDashboardMySessionsItem = self.load_class('MembersDashboardMySessionsItem')
        MembersDashboardMySessionsStorage = self.load_class('MembersDashboardMySessionsStorage')

        # update this object's locator
        self.locators.update(MembersDashboardMySessions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = TextReadOnly(self,{'base':'title'})
        self.close = Link(self,{'base':'close'})

        self.session_list = ItemList(self,
                                {
                                    'base' : 'listbase',
                                    'row'  : 'item',
                                }, MembersDashboardMySessionsItem,
                                {})

        self.storage = MembersDashboardMySessionsStorage(self,{'base':'storage'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def session_items(self):
        """return the next session item object"""

        return iter(self.session_list)


    def count_sessions(self):
        """return the number of sessions available in the widget"""

        return self.session_list.num_rows()


    def get_session_titles(self):
        """return a list of the session titles"""

        titles = []

        for i in self.session_items():
            titles.append(i.get_title())

        return titles


    def get_session_numbers(self):
        """return a list of the session numbers"""

        snums = []

        for i in self.session_items():
            snums.append(i.get_session_number())

        return snums


    def get_session_by_position(self,position):
        """return the n-th session in the list"""

        return self.session_list.get_row_by_position(position)


    def get_session_by_session_number(self,session_number):
        """return the n-th session in the list"""

        session_number = int(session_number)

        session_item = None
        for i in self.session_items():
            item_session_number = i.get_session_number()
            self.logger.debug('comparing %d with %d'
                % (item_session_number,session_number))
            if item_session_number == session_number:
                session_item = i
                break

        return session_item


    def manage_storage(self):
        """navigate to the storage management page"""

        return self.storage.goto_manage()


    def storage_amount(self):
        """return the percentage of used storage and total storage"""

        return self.storage.storage_meter()


class MembersDashboardMySessions_Locators_Base(object):
    """locators for MembersDashboardMySessions object"""

    locators = {
        'base'      : "xpath=//div[contains(@class,'draggable')]//h3[contains(text(),'My Sessions')]/..",
        'title'     : "css=.handle",
        'close'     : "css=.close",
        'listbase'  : "css=.session-list",
        'item'      : "css=.session",
        'storage'   : "css=.session-storage",
    }
