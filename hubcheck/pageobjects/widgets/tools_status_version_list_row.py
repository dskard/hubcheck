from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

class ToolsStatusVersionListRow(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(ToolsStatusVersionListRow,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        ToolsStatusVersionListRow_Locators = \
            self.load_class('ToolsStatusVersionListRow_Locators')

        # update this object's locator
        self.locators.update(ToolsStatusVersionListRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.version      = TextReadOnly(self,{'base':'version'})
        self.released     = TextReadOnly(self,{'base':'released'})
        self.subversion   = TextReadOnly(self,{'base':'subversion'})
        self.published    = TextReadOnly(self,{'base':'published'})
        self.edit         = Link(self,{'base':'edit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of properties for this row"""

        published_classes = self.published.get_attribute('class')

        published = None
        if 'toolunpublished' in published_classes:
            published = False
        elif 'toolpublished' in published_classes:
            published = True

        properties = {
            'version'    : self.version.value,
            'released'   : self.released.value,
            'subversion' : self.subversion.value,
            'published'  : published,
        }

        return properties


    def goto_edit(self):

        self.edit.click()


class ToolsStatusVersionListRow_Locators_Base(object):
    """locators for ToolsStatusVersionListRow object"""

    locators = {
        'base'           : "css=tr",
        'version'        : "css=td:nth-of-type(1)",
        'released'       : "css=td:nth-of-type(2)",
        'subversion'     : "css=td:nth-of-type(3)",
        'published'      : "css=td:nth-of-type(4) span",
        'edit'           : "css=td:nth-of-type(5) .action-link a",
    }
