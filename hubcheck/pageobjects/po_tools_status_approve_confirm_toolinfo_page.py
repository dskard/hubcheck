from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class ToolsStatusApproveConfirmToolInfoPage(GenericPage):
    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusApproveConfirmToolInfoPage,self)\
            .__init__(browser,catalog)
        self.path = '/tools/%s/license?action=confirm' % (toolname)

        # load hub's classes
        ToolsStatusApproveConfirmToolInfoPage_Locators = \
            self.load_class(
            'ToolsStatusApproveConfirmToolInfoPage_Locators')
        ToolsStatusApproveToolInfoForm = \
            self.load_class('ToolsStatusApproveToolInfoForm')

        # update this object's locator
        self.locators.update(
            ToolsStatusApproveConfirmToolInfoPage_Locators.locators)

        # setup page object's components
        self.tool_status    = Link(self,{'base':'tool_status'})
        self.new_tool       = Link(self,{'base':'new_tool'})
        self.tool_info_form = ToolsStatusApproveToolInfoForm(self)


    def goto_tool_status(self):
        return self.tool_status.click()


    def goto_new_tool(self):
        return self.new_tool.click()


    def approve_tool(self):
        return self.tool_info_form.approve_tool()


class ToolsStatusApproveConfirmToolInfoPage_Locators_Base(object):
    """locators for ToolsStatusApproveConfirmToolInfoPage object"""

    locators = {
        'tool_status'      : "css=#useroptions li:nth-of-type(1)",
        'new_tool'         : "css=#useroptions li:nth-of-type(2)",
    }

