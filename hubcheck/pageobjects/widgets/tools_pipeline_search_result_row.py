from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

class ToolsPipelineSearchResultRow(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(ToolsPipelineSearchResultRow,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        ToolsPipelineSearchResultRow_Locators = \
            self.load_class('ToolsPipelineSearchResultRow_Locators')

        # update this object's locator
        self.locators.update(ToolsPipelineSearchResultRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title        = Link(self,{'base':'title'})
        self.details      = TextReadOnly(self,{'base':'details'})
        self.alias        = Link(self,{'base':'alias'})
        self.status       = Link(self,{'base':'status'})
        self.time         = TextReadOnly(self,{'base':'time'})
        self.resource     = Link(self,{'base':'resource'})
        self.history      = Link(self,{'base':'history'})
        self.wiki         = Link(self,{'base':'wiki'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocators(self,widgets=None,cltype=''):

        widgets = [self.title,self.details,self.alias,self.status,
                   self.time,self.resource,self.history,self.wiki]
        super(ToolsPipelineSearchResultRow,self)._checkLocators(widgets,cltype)


    def value(self):
        """return a dictionary of properties for this row"""

        properties = {
            'title'     : self.title.text(),
            'details'   : self.details.value,
            'alias'     : self.alias.text(),
            'status'    : self.status.text(),
            'time'      : self.time.value,
        }

        return properties


    def goto_title(self):

        self.title.click()


    def get_details(self):

        return self.details.value


    def goto_alias(self):

        self.alias.click()


    def goto_status(self):

        self.status.click()


    def get_time(self):

        return self.time.value


    def goto_resource(self):

        self.resource.click()


    def goto_history(self):

        self.history.click()


    def goto_wiki(self):

        self.wiki.click()


class ToolsPipelineSearchResultRow_Locators_Base(object):
    """locators for ToolsPipelineSearchResultRow object"""

    locators = {
        'base'           : "css=tr",
        'title'          : "css=.entry-title",
        'details'        : "css=.entry-details",
        'alias'          : "css=.entry-alias",
        'status'         : "css=.entry-status",
        'time'           : "css=.entry-time",
        'resource'       : "css=.entry-page",
        'history'        : "css=.entry-history",
        'wiki'           : "css=.entry-wiki",
    }
