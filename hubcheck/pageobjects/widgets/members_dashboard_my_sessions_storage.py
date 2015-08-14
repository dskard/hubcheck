from hubcheck.pageobjects.widgets.storage_meter import StorageMeter


class MembersDashboardMySessionsStorage(StorageMeter):
    def __init__(self, owner, locatordict={}):
        super(MembersDashboardMySessionsStorage,self).__init__(owner,locatordict)

        # load hub's classes
        MembersDashboardMySessionsStorage_Locators = self.load_class('MembersDashboardMySessionsStorage_Locators')

        # update this object's locator
        self.locators.update(MembersDashboardMySessionsStorage_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()
