import unittest
import pytest
import sys
import hubcheck
import logging


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.pageobjects,
               pytest.mark.hcunit_courses
             ]


@pytest.mark.hcunit_courses_page
class hcunit_coursespage(hubcheck.testcase.TestCase):

    def setUp(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        CoursesPage = self.catalog.load('CoursesPage')
        self.po = CoursesPage(self.browser,self.catalog)
        self.po.goto_page()


    def test_goto_faq(self):
        """
        click the faq link
        """

        self.po.goto_faq()
        # self.assertFalse(po.is_on_page())


    def test_goto_guidelines(self):
        """
        click the guidelines link
        """

        self.po.goto_guidelines()
        # self.assertFalse(po.is_on_page())


    def test_goto_create_course(self):
        """
        click the create course link
        """

        self.po.goto_create_course()
        # self.assertFalse(po.is_on_page())


    def test_goto_browse_list(self):
        """
        click the browse courses link
        """

        self.po.goto_browse_list()
        # self.assertFalse(po.is_on_page())


    def test_search_courses(self):
        """
        try entering text into the courses search box
        and click the search button
        """

        self.po.search_courses('searchtext')
        # self.assertFalse(po.is_on_page())


    def test_get_popular_courses(self):
        """
        get the list of popular courses
        """

        popular_courses = self.po.get_popular_courses()


    def test_has_info_no_popular_courses(self):
        """
        check for the 'no popular courses' info block
        """

        num_courses = self.po.courses.popular_courses.num_items()
        has_info = self.po.has_info_no_popular_courses()

        if num_courses == 0:
            self.assertTrue(has_info,"no courses are disaplyed and\
                the 'no_popular_courses' info block is not displayed")
        else:
            self.assertFalse(has_info,"%s courses are disaplyed and\
                the 'no_popular_courses' info block is displayed"\
                % (num_courses))


    def test_goto_popular_courses(self):
        """
        try clicking all of the popular courses links
        """

        pageurl1 = self.po.current_url()
        for course in self.po.get_popular_courses():
            self.po.goto_popular_course(course)
            pageurl2 = self.po.current_url()
            self.assertTrue(pageurl1 != pageurl2,
                "after pressing popular course link '%s',\
                 on %s, url did not change" % (course,pageurl2))
            self.browser._browser.back()


