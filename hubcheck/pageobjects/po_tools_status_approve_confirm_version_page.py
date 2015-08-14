from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Text

class ToolsStatusApproveConfirmVersionPage(GenericPage):
    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusApproveConfirmVersionPage,self)\
            .__init__(browser,catalog)
        self.path = '/tools/%s/status' % (toolname)

        # load hub's classes
        ToolsStatusApproveConfirmVersionPage_Locators = \
            self.load_class(
            'ToolsStatusApproveConfirmVersionPage_Locators')
        ToolsStatusApproveVersionForm = \
            self.load_class('ToolsStatusApproveVersionForm')
        ToolsStatusVersionListRow = \
            self.load_class('ToolsStatusVersionListRow')
        ItemList = self.load_class('ItemList')

        # update this object's locator
        self.locators.update(
            ToolsStatusApproveConfirmVersionPage_Locators.locators)

        # setup page object's components
        self.version_form = ToolsStatusApproveVersionForm(self)
        self.version_list = ItemList(self,
                                {
                                    'base'     : 'listbase',
                                    'row'      : 'vlrow',
                                }, ToolsStatusVersionListRow,
                                {
                                    'version'    : 'vlrow_version',
                                    'released'   : 'vlrow_released',
                                    'subversion' : 'vlrow_subversion',
                                    'published'  : 'vlrow_published',
                                    'edit'       : 'vlrow_edit',
                                })
        self.version_list.row_start = 0
        self.version_list.row_offset = 2


class ToolsStatusApproveConfirmVersionPage_Locators_Base(object):
    """locators for LoginPage object"""

    locators = {
        'listbase'         : "css=#tktlist",
        'vlrow'            : "css=#tktlist tbody tr:nth-of-type({row_num})",
        'vlrow_version'    : "css=#tktlist tbody tr:nth-of-type({row_num}) td:nth-of-type(1)",
        'vlrow_released'   : "css=#tktlist tbody tr:nth-of-type({row_num}) td:nth-of-type(2)",
        'vlrow_subversion' : "css=#tktlist tbody tr:nth-of-type({row_num}) td:nth-of-type(3)",
        'vlrow_published'  : "css=#tktlist tbody tr:nth-of-type({row_num}) td:nth-of-type(4) span",
        'vlrow_edit'       : "css=#tktlist tbody tr:nth-of-type({row_num}) td:nth-of-type(5) .action-link a",
    }

