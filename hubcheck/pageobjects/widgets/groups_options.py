from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from selenium.webdriver.common.action_chains import ActionChains

class GroupsOptions(BasePageWidget):
    def __init__(self, owner, locatordict=None):
        super(GroupsOptions,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsOptions_Locators = self.load_class('GroupsOptions_Locators')

        # update this object's locator
        self.locators.update(GroupsOptions_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.invite     = Link(self,{'base':'invite'})
        self.edit       = Link(self,{'base':'edit'})
        self.customize  = Link(self,{'base':'customize'})
        self.manage     = Link(self,{'base':'manage'})
        self.delete     = Link(self,{'base':'delete'})

        self._links = ['invite','edit','customize','manage','delete']

        # update the component's locators with this objects overrides
        self._updateLocators()

    def _checkLocators(self,widgets=None,cltype=''):

        base = self.owner.find_element(self.locators['base'])

        # hover mouse over the group manager toolbar to expand it
        actionProvider = ActionChains(self.owner._browser)\
                         .move_to_element(base)
        actionProvider.perform()

        # check for locators
        super(GroupsOptions,self)._checkLocators(widgets,cltype)


    def get_options_items(self):
        """return the available group management options"""

        return self._links


    def goto_options_item(self,link):
        """click on a group management option link"""

        if not link in self._links:
            raise ValueError("invalid link name: '%s'",link)

        base = self.owner.find_element(self.locators['base'])

        # hover mouse over the group manager toolbar to expand it
        actionProvider = ActionChains(self.owner._browser)\
                         .move_to_element(base)
        self.logger.debug("moving mouse over options dropdown")
        actionProvider.perform()
        # move the mouse to the correct link and click it
        loc = self.locators[link]
        e = self.owner.find_element(loc,base)
        # moving to the element does not work in this case
        # I think because the browser's popup window for the url
        # blocks the element? either way, we can click the element
        # just by having the options menu open.
        #actionProvider = ActionChains(self.owner._browser)\
        #                 .move_to_element(e)
        #actionProvider.perform()
        self.owner.wait_for_page_element_displayed(loc)
        self.logger.debug("clicking drowdown menu option '%s': %s" % (link,loc))
        e.click()


class GroupsOptions_Locators_Base(object):
    """locators for GroupsOptions object"""

    locators = {
        'base'      : "css=#group_options",
        'invite'    : "css=#group_options .group-invite",
        'edit'      : "css=#group_options .group-edit",
        'customize' : "css=#group_options .group-customize",
        'manage'    : "css=#group_options .group-pages",
        'delete'    : "css=#group_options .group-delete",
    }

