from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Text

class Groups1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Groups1,self).__init__(owner,locatordict)

        # load hub's classes
        object_locators = self.load_class('Groups_Locators')
        PopularList = self.load_class('PopularList')
        PopularItem = self.load_class('PopularItem')
        TextSearchBox = self.load_class('TextSearchBox')

        # update this object's locator
        self.locators.update(object_locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.faq            = Link(self,{'base':'faq'})
        self.guidelines     = Link(self,{'base':'guidelines'})
        self.create         = Link(self,{'base':'create'})
        self.browse         = Link(self,{'base':'browse'})
        self.group_search   = TextSearchBox(self,
                                    {'base'   : 'searchgroups',
                                     'text'   : 'searchi',
                                     'submit' : 'searchb'})
        self.popular_groups = PopularList(self,
                                    {'base' : 'popularitem',
                                     'item' : 'popularitem'},
                                    PopularItem,
                                    {'title'        : 'pi_title',
                                     'description'  : 'pi_description',
                                     'logo'         : 'pi_logo'})


        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_faq(self):
        """click the faq link"""

        self.faq.click()


    def goto_guidelines(self):
        """click the guidelines link"""

        self.guidelines.click()


    def goto_create_group(self):
        """click the create group link"""

        self.create.click()


    def goto_browse_list(self):
        """click the browse list of groups link"""

        self.browse.click()


    def search_groups(self,terms):
        """click the search groups link"""

        return self.group_search.search_for(terms)


    def get_popular_groups(self):
        """return the list of popular group names"""

        groups = [group.value()['title'] \
                    for group in iter(self.popular_groups)]

        return groups


    def goto_popular_group(self,group_name):
        """click the group in the popular group list"""

        group = self.popular_groups.get_item_by_property('title',group_name)
        return group.goto_group()

    def has_info_no_popular_groups(self):
        """check if the 'no popular groups' info block is displayed"""

        return self.is_displayed(locator=self.locators['popularinfo'])


class Groups1_Locators_Base(object):
    """locators for Groups object"""

    locators = {
        'base'          : "css=#content",
        'faq'           : "css=#introduction li:nth-of-type(1) a",
        'guidelines'    : "css=#introduction li:nth-of-type(2) a",
        'create'        : "css=#introduction .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.browse a",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
    }


class Groups1_Locators_Base_2(object):
    """locators for Groups object"""
    # new create locator

    locators = {
        'base'          : "css=#content",
        'faq'           : "css=#introduction li:nth-of-type(1) a",
        'guidelines'    : "css=#introduction li:nth-of-type(2) a",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.browse a",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
#        'popularitem'   : "xpath=//*[contains(@class,'group-list')]/../../div[%s]",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }

class Groups1_Locators_Base_3(object):
    """locators for Groups object"""
    # new create locator

    locators = {
        'base'          : "css=#content",
        'faq'           : "css=#introduction li:nth-of-type(1) a",
        'guidelines'    : "css=#introduction li:nth-of-type(2) a",
        'create'        : "css=#useroptions .group",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.browse a",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }

class Groups1_Locators_Base_4(object):
    """locators for Groups object"""
    # new create locator

    locators = {
        'base'          : "css=#content",
        'faq'           : "css=#introduction li:nth-of-type(1) a",
        'guidelines'    : "css=#introduction li:nth-of-type(2) a",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.group-intro-browse",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }

class Groups1_Locators_Base_5(object):
    """
        locators for Groups object
        updated faq and guidelines locators for 1.1.2
    """

    locators = {
        'base'          : "css=#content",
        'faq'           : "css=.group-intro-faqs",
        'guidelines'    : "css=.group-intro-guidelines",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.group-intro-browse",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }


class Groups2(BasePageWidget):
    """
        Groups page for 1.1.5, 1.2.0
    """

    def __init__(self, owner, locatordict={}):
        super(Groups2,self).__init__(owner,locatordict)

        # load hub's classes
        object_locators = self.load_class('Groups_Locators')
        PopularList = self.load_class('PopularList')
        PopularItem = self.load_class('PopularItem')
        TextSearchBox = self.load_class('TextSearchBox')

        # update this object's locator
        self.locators.update(object_locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.need_help      = Link(self,{'base':'need_help'})
        self.create         = Link(self,{'base':'create'})
        self.browse         = Link(self,{'base':'browse'})
        self.group_search   = TextSearchBox(self,
                                    {'base'   : 'searchgroups',
                                     'text'   : 'searchi',
                                     'submit' : 'searchb'})
        self.popular_groups = PopularList(self,
                                    {'base' : 'popularitem',
                                     'item' : 'popularitem'},
                                    PopularItem,
                                    {'title'        : 'pi_title',
                                     'description'  : 'pi_description',
                                     'logo'         : 'pi_logo'})


        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_need_help(self):
        """click the guidelines link"""

        self.need_help.click()


    def goto_create_group(self):
        """click the create group link"""

        self.create.click()


    def goto_browse_list(self):
        """click the browse list of groups link"""

        self.browse.click()


    def search_groups(self,terms):
        """click the search groups link"""

        return self.group_search.search_for(terms)


    def get_popular_groups(self):
        """return the list of popular group names"""

        groups = [group.value()['title'] \
                    for group in iter(self.popular_groups)]

        return groups


    def goto_popular_group(self,group_name):
        """click the group in the popular group list"""

        group = self.popular_groups.get_item_by_property('title',group_name)
        return group.goto_group()


    def has_info_no_popular_groups(self):
        """check if the 'no popular groups' info block is displayed"""

        return self.is_displayed(locator=self.locators['popularinfo'])


class Groups2_Locators_Base_1(object):
    """
        locators for Groups object
        removed faq and guidelines links
        added need_help link
        hub version 1.1.5
    """

    locators = {
        'base'          : "css=#content",
        'need_help'     : "css=#introduction .aside .popup",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.group-intro-browse",
        'popularinfo'   : "css=.section > div:nth-of-type(4) .info",
        'popularitem'   : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }


class Groups2_Locators_Base_2(object):
    """
        locators for Groups object
        removed faq and guidelines links
        added need_help link
        locator change for popular section
        hub version 1.2.0
    """

    locators = {
        'base'          : "css=#content",
        'need_help'     : "css=#introduction .aside .popup",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.group-intro-browse",
        'popularinfo'   : "css=.section > div:nth-of-type(2) .info",
        'popularitem'   : "css=.group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }


class Groups2_Locators_Base_3(object):
    """
        locators for Groups object
        updated need_help link locator
        hub version 1.3.0
    """

    locators = {
        'base'          : "css=#content",
        'need_help'     : "css=#introduction .popup",
        'create'        : "css=#useroptions .add",
        'searchgroups'  : "css=form.search",
        'searchi'       : "css=#gsearch",
        'searchb'       : "css=.search [type='submit']",
        'browse'        : "css=.group-intro-browse",
        'popularinfo'   : "css=.section > div:nth-of-type(2) .info",
        'popularitem'   : "css=.group-list",
        'pi_title'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description': "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'       : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }


