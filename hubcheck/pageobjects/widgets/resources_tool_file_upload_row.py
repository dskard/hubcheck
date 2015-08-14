from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem
from selenium.webdriver.common.action_chains import ActionChains

class ResourcesToolFileUploadRow(ItemListItem):

    def __init__(self, owner, locatordict={}, row_number=0):

        super(ResourcesToolFileUploadRow,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        ResourcesToolFileUploadRow_Locators = self.load_class('ResourcesToolFileUploadRow_Locators')

        # update this object's locator
        self.locators.update(ResourcesToolFileUploadRow_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name     = TextReadOnly(self,{'base':'name'})
        self.show     = Link(self,{'base':'show'},self._onClickShow)
        self.delete   = Link(self,{'base':'delete'},self._onClickDelete)

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _onClickShow(self):
        self.show.wait_until_invisible()


    def _onClickDelete(self):
        self.delete.wait_until_invisible()


    def rename(self,name):
        """rename the uploaded document"""
        # use action chains to double click on the name,
        # and fill in a new value
        # the documentation above the widget says the user
        # needs to double click, but it appears a single
        # click will work. it also says tab or enter
        # save, but i don't think these keys do anything
        e = self.name.wait_until_visible()
        ActionChains(self._browser)\
            .double_click(e)\
            .perform()

        t = Text(self,{'base':'rename_text'})
        s = Button(self,{'base':'rename_save'})

        t.wait_until_visible()
        t.value = name
        s.click()
        s.wait_until_not_present()

        del t
        del s


    def value(self):
        """return a dictionary with the name and size properties"""

        # show text looks like this:
        # <filename>, <size> <units>
        # simulink.jpg, 41.99 Kb
        size = self.show.text().split(',')[1].strip()

        return({'name':self.name.text(), 'size':size})


class ResourcesToolFileUploadRow_Locators_Base(object):
    """locators for ResourcesToolFileUploadRow object"""

    locators = {
        'base'           : "css=.list tr:nth-of-type({row_num})",
        'name'           : "css=.list tr:nth-of-type({row_num}) .ftitle",
        'show'           : "css=.list tr:nth-of-type({row_num}) .caption a",
        'delete'         : "css=.list tr:nth-of-type({row_num}) .t a",
        'rename_text'    : "css=.ftitle .resultItem",
        'rename_save'    : "css=.ftitle button:nth-of-type(1)",
        'rename_cancel'  : "css=.ftitle button:nth-of-type(2)",
    }
