from hubcheck.pageobjects.po_generic_page import GenericPage

class SupportNeedHelpPage(GenericPage):
    """Support Need Help page object"""

    def __init__(self,browser,catalog):
        super(SupportNeedHelpPage,self).__init__(browser,catalog)


    def open(self):
        return self.needhelplink.click()


    def close(self):
        return self.needhelpform.close.click()


    def submit_ticket(self,data):
        return self.needhelpform.submit_ticket(data)


    def goto_ticket(self):
        return self.needhelpform.goto_ticket()
