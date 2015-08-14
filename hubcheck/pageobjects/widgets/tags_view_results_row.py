from hubcheck.pageobjects.widgets.item_list_item import ItemListItem
from hubcheck.pageobjects.basepageelement import TextReadOnly, Link

class TagsViewResultsRow(ItemListItem):

    def __init__(self, owner, locatordict={}, row_number=0):

        super(TagsViewResultsRow,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        TagsViewResultsRow_Locators = self.load_class('TagsViewResultsRow_Locators')

        # update this object's locator
        self.locators.update(TagsViewResultsRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.title = Link(self,{'base':'title'})
        self.text  = TextReadOnly(self,{'base':'text'})
        self.href  = TextReadOnly(self,{'base':'href'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary with the title, text, and href properties of the tag"""

        return({ 'title' : self.title.text(),
                 'text'  : self.text.value,
                 'href'  : self.href.value   })


    def goto_resource(self):
        """click the resource link"""

        self.title.click()


class TagsViewResultsRow_Locators_Base(object):
    """locators for TagsViewResultsRow object"""

    locators = {
        'base'           : "css=.results li:nth-of-type({row_num})",
        'title'          : "css=.results li:nth-of-type({row_num}) .title",
        'text'           : "css=.results li:nth-of-type({row_num}) p:nth-of-type(2)",
        'href'           : "css=.results li:nth-of-type({row_num}) .href",
    }
