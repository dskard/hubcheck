from hubcheck.pageobjects.po_hubucoursemanage import HubUCourseManagePage

class HubUCourseManageMembershipPage(HubUCourseManagePage):
    """hub u course manager membership page"""

    def __init__(self,browser,catalog,groupid=''):
        super(HubUCourseManageMembershipPage,self).__init__(browser,catalog,groupid)

        # load hub's classes
        HubUCourseManageMembershipPage_Locators = self.load_class('HubUCourseManageMembershipPage_Locators')
        HubUCourseMembershipListing = self.load_class('HubUCourseMembershipListing')

        # update this object's locator
        self.locators.update(HubUCourseManageMembershipPage_Locators.locators)

        # setup page object's components
        self.course_listing = HubUCourseMembershipListing(self,{'base':'listing'})

    def goto_page(self):
        super(HubUCourseManageMembershipPage,self).goto_page()
        self.tabs.membership.click()

    def update_enrollment(self):
        return self.course_listing.update_enrollment()

    def select_imported(self):
        return self.course_listing.select_imported()

    def select_invited(self):
        return self.course_listing.select_invited()

    def select_members(self):
        return self.course_listing.select_members()

    def get_footer_members_count(self):
        return self.course_listing.get_footer_members_count()

    def get_footer_total_count(self):
        return self.course_listing.get_footer_total_count()

    def count_imported_rows(self):
        return self.course_listing.count_imported_rows()

    def count_invited_rows(self):
        return self.course_listing.count_invited_rows()

    def count_member_rows(self):
        return self.course_listing.count_member_rows()

    def count_total_rows(self):
        return self.course_listing.count_total_rows()

    def prepare_to_send_email(self):
        return self.course_listing.prepare_to_send_email()

class HubUCourseManageMembershipPage_Locators_Base(object):
    """locators for HubUCourseManageMembershipPage object"""

    locators = {
        'listing' : "css=.course-listing",
    }
