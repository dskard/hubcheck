from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Checkbox
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextReadOnly

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from datetime import datetime

class HubUCourseMembershipListing(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(HubUCourseMembershipListing,self).__init__(owner,locatordict)

        # load hub's classes
        HubUCourseMembershipListing_Locators = self.load_class('HubUCourseMembershipListing_Locators')
        HubUCourseMembershipListingMemberRow = self.load_class('HubUCourseMembershipListingMemberRow')
        HubUCourseMembershipListingDetailRow = self.load_class('HubUCourseMembershipListingDetailRow')

        # update this object's locator
        self.locators.update(HubUCourseMembershipListing_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.member_row    = HubUCourseMembershipListingMemberRow(self,{'base':'enrollee_row'})
        self.detail_row    = HubUCourseMembershipListingDetailRow(self,{'base':'detail_row'})
        self.action        = Select(self,{'base':'action'})
        self.action_submit = Button(self,{'base':'action_submit'})
        self.get_enroll    = Link(self,{'base':'get_enroll'},self._onClick)
        self.export_enroll = Link(self,{'base':'export_enroll'})
        self.members       = TextReadOnly(self,{'base':'members'})
        self.total         = TextReadOnly(self,{'base':'total'})

        self.member_data  = {}

        # update the component's locators with this objects overrides
        self._updateLocators()


    def update_enrollment(self):
        """click the update enrollment link"""

        self.get_enroll.click()


    def select_imported(self):
        """check the checkboxes of all imported course members"""

        count = 0
        imported_cbs = self.find_elements(self.locators['imported_cb'])
        for cb in imported_cbs:
            cb.click()
            count += 1
        return count


    def select_invited(self):
        """check the checkboxes of all invited course members"""

        count = 0
        invited_cbs = self.find_elements(self.locators['invited_cb'])
        for cb in invited_cbs:
            cb.click()
            count += 1
        return count


    def select_members(self):
        """check the checkboxes of all member course members"""

        count = 0
        member_cbs = self.find_elements(self.locators['member_cb'])
        for cb in member_cbs:
            cb.click()
            count += 1
        return count


    def get_footer_members_count(self):
        """retrieve the number of members in the group from the footer"""

        return self.members.value


    def get_footer_total_count(self):
        """retrieve the total number of people in the group from the footer"""

        return self.total.value


    def count_imported_rows(self):
        """retrieve the number of imported rows in the table"""

        return len(self.find_elements(self.locators['imported_row']))


    def count_invited_rows(self):
        """retrieve the number of invited rows in the table"""

        return len(self.find_elements(self.locators['invited_row']))


    def count_member_rows(self):
        """retrieve the number of member rows in the table"""

        return len(self.find_elements(self.locators['member_row']))


    def count_total_rows(self):
        """retrieve the number of total rows in the table"""

        return len(self.find_elements(self.locators['enrollee_row']))


    def prepare_to_send_email(self):
        """select the 'Send Email' action and goto the email page"""

        self.action.choose('Send Email')
        self.action_submit.click()


    def retrieve_members(self,save_cb=None, continue_cb=None, reverse=False):
        """return a list of member data from the table that match the specified criteria"""

        self.member_data = {}
        total = int(self.total.value)

        if reverse == False:
            start = 1
            end = total + 1
            step = 1
        else:
            start = total
            end = 1 - 1
            step = -1

        for index in xrange(start,end,step):
            didx = index*2
            midx = didx-1

            # FIXME: move the css code into locator file
            mlocator = self.locators['traversal_row'] % midx
            dlocator = self.locators['traversal_row'] % didx

            self.member_row.locator = mlocator
            name = self.member_row.name.text()

            # open the hidden detail row
            self.member_row.name.click()

            self.detail_row.locator = dlocator
            enroll_id = self.detail_row.enroll_id.value
            enroll_date = self.detail_row.enroll_date.value
            import_date = self.detail_row.import_date.value
            invite_sent = self.detail_row.invite_sent.value
            invite_accept = self.detail_row.invite_accept.value

            # close the detail row
            self.member_row.name.click()

            save = True
            cont = True

            mdata = {
                'name'          : name,
                'enroll_id'     : enroll_id,
                'enroll_date'   : enroll_date,
                'import_date'   : import_date,
                'invite_sent'   : invite_sent,
                'invite_accept' : invite_accept,
            }

            if continue_cb:
                cont = continue_cb(mdata)

            if not cont:
                break

            if save_cb:
                save = save_cb(mdata)

            if save:
                self.member_data[midx] = {
                    'name'          : name,
                    'enroll_id'     : enroll_id,
                    'enroll_date'   : enroll_date,
                    'import_date'   : import_date,
                    'invite_sent'   : invite_sent,
                    'invite_accept' : invite_accept,
                    '__mlocator__'  : mlocator,
                    '__dlocator__'  : dlocator,
                }

        return self.member_data


    def find_by_import_date(self,dtobj):
        """retrieve table data that matches the specified datetime object"""

        # date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

        def callback(name, enroll_id, enroll_date, import_date, invite_sent, invite_accept):
            import_date_dt = datetime.strptime(import_date, '%b %d, %Y')
            return import_date_dt == dtobj

        return self.retrieve_members(callback)


    def select_retrieved_members(self):
        """check the 'select' box of members retrieved from the 'retrieve_members' method"""

        for [k,v] in self.member_data.items():
            self.member_row.locator = v['__mlocator__']
            self.member_row.cb_email.value = True


    def _onClick(self):
        """callback function for updating enrollments"""

        try:
            # wait for the page to refresh
            wait = WebDriverWait(self._browser, 30)
            wait.until(lambda browser :
                       browser.find_element_by_id("course-notice").is_displayed())
        except TimeoutException:
            # browser.save_screenshot_as_base64
            # self._browser.save_screenshot_as_file("need_help.submitted-1.png")
            raise TimeoutException("Timeout while waiting to retrieve new enrollments")

        # FIXME: check if the notice text is
        # "Enrollment Updates\n\nThere are no new enrollments or enrollment changes at this time."
        #e = self.find_element(self.locators['notice'])
        #ticket_number = e.text
        #return ticket_number
        return True


class HubUCourseMembershipListing_Locators_Base(object):
    """locators for HubUCoursMembershipListing object"""

    # the member_row only works for imported members
    # invited members have css=tr.invited
    locators = {
        'base'          : "css=.course-listing",
        'enrollee_row'  : "css=.member-details",
        'imported_row'  : "css=.impoted",
        'invited_row'   : "css=.invited",
        'member_row'    : "css=.member",
        'imported_cb'   : "css=.imported input[name='enrollee[]']",
        'invited_cb'    : "css=.invited input[name='enrollee[]']",
        'member_cb'     : "css=.member input[name='enrollee[]']",
        'detail_row'    : "css=.listing-details",
        'traversal_row' : "css=tbody > tr:nth-child(%d)",
        'action'        : "css=.manage-select",
        'action_submit' : "css=.manage-submit",
        'get_enroll'    : "css=#pec-enrollments",
        'export_enroll' : "css=.txt",
        'members'       : "css=.nanohubu-members",
        'total'         : "css=.nanohubu-total-in-list",
        'notice'        : "css=#course-notice",
    }
