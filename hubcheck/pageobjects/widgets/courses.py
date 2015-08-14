from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link

class Courses(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(Courses,self).__init__(owner,locatordict)

        # load hub's classes
        object_locators = self.load_class('Courses_Locators')
        PopularList = self.load_class('PopularList')
        PopularItem = self.load_class('PopularItem')
        TextSearchBox = self.load_class('TextSearchBox')

        # update this object's locator defaults
        self.locators.update(object_locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.faq              = Link(self,{'base':'faq'})
        self.guidelines       = Link(self,{'base':'guidelines'})
        self.create           = Link(self,{'base':'create'})
        self.browse           = Link(self,{'base':'browse'})
        self.course_search    = TextSearchBox(self,
                                    {'base'   : 'searchcourses',
                                     'text'   : 'searchi',
                                     'submit' : 'searchb'})
        self.popular_courses  = PopularList(self,
                                    {'base' : 'popularitem',
                                     'item' : 'popularitem'},
                                    PopularItem,
                                    {'title'        : 'pi_title',
                                     'description'  : 'pi_description',
                                     'logo'         : 'pi_logo'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def goto_faq(self):
        """click the faq link"""

        self.faq.click()


    def goto_guidelines(self):
        """click the guidelines link"""

        self.guidelines.click()


    def goto_create_course(self):
        """click the create group link"""

        self.create.click()


    def goto_browse_list(self):
        """click the browse all courses link"""

        self.browse.click()


    def search_courses(self,terms):
        """perform a search for courses using the provided terms"""

        return self.course_search.search_for(terms)


    def get_popular_courses(self):
        """return the list of popular course names"""

        courses = [course.value()['title'] \
                    for course in iter(self.popular_courses)]

        return courses


    def goto_popular_course(self,course_name):
        """click the course in the popular course list"""

        return self.popular_courses.goto_course(course_name)


    def has_info_no_popular_courses(self):
        """check if the 'no popular courses' info block is displayed"""

        return self.is_displayed(locator=self.locators['popularinfo'])


class Courses_Locators_Base(object):
    """locators for Courses object"""

    locators = {
        'base'                : "css=#content",
        'faq'                 : "css=#introduction li:nth-of-type(1) a",
        'guidelines'          : "css=#introduction li:nth-of-type(2) a",
        'create'              : "css=#useroptions .add",
        'searchcourses'       : "css=form.search",
        'searchi'             : "css=#gsearch",
        'searchb'             : "css=.search [type='submit']",
        'browse'              : "css=.browse a",
        'popularinfo'         : "css=.section > div:nth-of-type(4) .info",
        'popularitem'         : "css=.section > div:nth-of-type(4) .group-list",
        'pi_title'            : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//h3//a",
        'pi_description'      : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'details-w-logo')]//p",
        'pi_logo'             : "xpath=//*[contains(@class,'group-list')]/../../div[%s]//*[contains(@class,'logo')]//img",
    }
