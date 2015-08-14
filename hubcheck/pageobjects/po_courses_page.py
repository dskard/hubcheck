from hubcheck.pageobjects.po_generic_page import GenericPage

class CoursesPage(GenericPage):
    """courses page"""

    def __init__(self,browser,catalog):
        super(CoursesPage,self).__init__(browser,catalog)
        self.path = "/courses"

        # load hub's classes
        CoursesPage_Locators = self.load_class('CoursesPage_Locators')
        Courses = self.load_class('Courses')

        # update this object's locator
        self.locators.update(CoursesPage_Locators.locators)

        # setup page object's components
        self.courses = Courses(self,{'base':'courses'})

    def goto_faq(self):
        return self.courses.goto_faq()

    def goto_guidelines(self):
        return self.courses.goto_guidelines()

    def goto_create_course(self):
        return self.courses.goto_create_course()

    def goto_browse_list(self):
        return self.courses.goto_browse_list()

    def search_courses(self,searchtext):
        return self.courses.search_courses(searchtext)

    def get_popular_courses(self):
        return self.courses.get_popular_courses()

    def goto_popular_group(self,group_name):
        return self.courses.goto_popular_group(group_name)

    def has_info_no_popular_courses(self):
        return self.courses.has_info_no_popular_courses()


class CoursesPage_Locators_Base(object):
    """locators for CoursesPage object"""

    locators = {
        'courses' : "css=#content",
    }
