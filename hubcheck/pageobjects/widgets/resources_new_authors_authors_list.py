from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.exceptions import NoSuchUserException
from selenium.common.exceptions import NoSuchElementException
import re

class ResourcesNewAuthorsAuthorsList(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewAuthorsAuthorsList,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewAuthorsAuthorsList_Locators = \
            self.load_class('ResourcesNewAuthorsAuthorsList_Locators')

        # update this object's locator
        self.locators.update(ResourcesNewAuthorsAuthorsList_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.submit     = Button(self,{'base':'submit'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _get_author(self,rowEle):

        column = self.find_element(self.locators['nameorg'],rowEle)
        org = self.find_element(self.locators['organization'],rowEle)
        authorname = re.sub(org.text,'',column.text)
        return authorname


    def _get_author_row(self,author):

        rows = []
        try:
            rows = self.find_elements_in_owner(self.locators['author_row'])
        except NoSuchElementException:
            # there are no authors
            rows = []

        for rowEle in rows:
            authorname = self._get_author(rowEle)
            if authorname == author:
                return rowEle
        raise NoSuchUserException("could not find author: '%s'" % (author))


    def get_authors(self):
        """return the list of authors"""

        names = []
        rows = []

        try:
            rows = self.find_elements_in_owner(self.locators['author_row'])
        except NoSuchElementException:
            # there are no authors
            rows = []

        for rowEle in rows:
            authorname = self._get_author(rowEle)
            names.append(authorname)
        return names


    def author_role(self,author,role=None):
        """adjust the role for an author, returning the old role"""

        rowEle = self._get_author_row(author)
        roleEle = self.find_element(self.locators['role'],rowEle)

        #FIXME: shenanigans begin
        roleid = roleEle.get_attribute('id')
        key = "roleid-%s" % (roleid)
        self.locators[key] = "css=#%s" % (roleid)
        obj = Select(self,{'base':key})
        obj.detach_from_owner()
        #FIXME: shenanigans end

        oldrole = obj.selected()
        if role:
            obj.value = role
            # click the "save changes" button
            self.submit.click()
        del obj
        del self.locators[key]
        return oldrole


    def move_author_up(self,author):
        """increase the author's position"""

        rowEle = self._get_author_row(author)
        b = self.find_element(self.locators['up'],rowEle)
        b.click()


    def move_author_down(self,author):
        """decrease the author's position"""

        rowEle = self._get_author_row(author)
        b = self.find_element(self.locators['down'],rowEle)
        b.click()


    def delete_author(self,author):
        """remove an author from the list"""

        rowEle = self._get_author_row(author)
        b = self.find_element(self.locators['trash'],rowEle)
        b.click()


    def author_organization(self,author,org=None):
        """set an author's organization"""

        rowEle = self._get_author_row(author)
        orgEle = self.find_element(self.locators['organization'],rowEle)

        #FIXME: shenanigans begin
        orgName = orgEle.get_attribute('name')
        key = "orgName-%s" % (orgName)
        self.locators[key] = "css=[name='%s']" % (orgName)
        obj = Text(self,key)
        obj.detach_from_owner()
        #FIXME: shenanigans end

        oldorg = obj.value
        if org:
            obj.value = org
            # click the "save changes" button
            self.submit.click()
        del obj
        del self.locators[key]
        return oldorg


class ResourcesNewAuthorsAuthorsList_Locators_Base(object):
    """locators for ResourcesNewAuthorsAuthorsList object"""

    locators = {
        'base'              : "css=#authors-list",
        'author_row'        : "css=#authors-list .list tbody tr",
        'nameorg'           : "css=td:nth-of-type(1)",
        'organization'      : "css=input[placeholder='Organization']",
        'role'              : "css=select",
        'up'                : "css=.u a",
        'down'              : "css=.d a",
        'trash'             : "css=.t a",
        'submit'            : "css=#authors-list [type='submit']",
    }
