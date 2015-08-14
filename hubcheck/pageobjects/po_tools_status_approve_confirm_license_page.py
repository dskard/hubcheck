from hubcheck.pageobjects.po_generic_page import GenericPage
from hubcheck.pageobjects.basepageelement import Link

class ToolsStatusApproveConfirmLicensePage(GenericPage):
    def __init__(self,browser,catalog,toolname=''):
        super(ToolsStatusApproveConfirmLicensePage,self)\
            .__init__(browser,catalog)
        self.path = '/tools/%s/license?action=confirm' % (toolname)

        # load hub's classes
        ToolsStatusApproveConfirmLicensePage_Locators = \
            self.load_class(
            'ToolsStatusApproveConfirmLicensePage_Locators')
        ToolsStatusApproveLicenseForm = \
            self.load_class('ToolsStatusApproveLicenseForm')

        # update this object's locator
        self.locators.update(
            ToolsStatusApproveConfirmLicensePage_Locators.locators)

        # setup page object's components
        self.tool_status  = Link(self,{'base':'tool_status'})
        self.new_tool  = Link(self,{'base':'new_tool'})
        self.license_form = ToolsStatusApproveLicenseForm(self)

    def goto_tool_status(self):
        return self.tool_status.click()

    def goto_new_tool(self):
        return self.new_tool.click()

    def populate_form(self,data):
        return self.license_form.populate_form(data)

    def submit_form(self,data={}):
        return self.license_form.submit_form(data)


class ToolsStatusApproveConfirmLicensePage_Locators_Base(object):
    """locators for ToolsStatusApproveConfirmLicensePage object"""

    locators = {
        'tool_status'      : "css=#useroptions li:nth-of-type(1)",
        'new_tool'         : "css=#useroptions li:nth-of-type(2)",
    }

