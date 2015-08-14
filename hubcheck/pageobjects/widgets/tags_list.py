from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.exceptions import NoSuchTagException
from selenium.common.exceptions import NoSuchElementException
import re

class TagsList(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(TagsList,self).__init__(owner,locatordict)

        # load hub's classes
        TagsList_Locators = self.load_class('TagsList_Locators')

        # update this object's locator
        self.locators.update(TagsList_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _parse_tag(self,tagstr):
        """Parse tag strings into tagname and tagcount

           This function tries to parse the text of tags from a webpage that
           includes a tagname followed by a space and a number (count). If the
           tag string ends in a space and a numeric value, all characters upto
           the last space and numeric value are returned as the tag name.

           A two element dictionary of the following form is returned:
           {
             'name' : xxx
             'count' : yyy
           }
           where xxx is the tag name and yyy is an intger tag count or None

           :Args:
            - tagstr - string representing a tagname with possible tagcount

           Examples:
           "tagname"        -> ["tagname", None]
           "tagname 1"      -> ["tagname", 1]
           "tag name 1"     -> ["tag name", 1]
           "tag name 1 1"   -> ["tag name 1", 1]
           "404"            -> ["404", None]
           "404 404"        -> ["404", 404]
           "abc 4-0-4"      -> ["abc 4-0-4", None]

           This function will not work with tags that end in
           a space and numeric value.
        """

        tagname = None
        tagcount = None

        q = tagstr.split(' ')
        if len(q) == 1:
            # no spaces, only tag name was provided
            tagname = q[0]
            tagcount = None
        else:
            if re.match('^[0-9]+$',q[-1]):
                # last word has a number
                # which probably means it is the count
                tagname = ' '.join(q[0:-1])
                try:
                    tagcount = int(q[-1])
                except ValueError:
                    # integer conversion failed, probably not a tag count
                    tagname = tagstr
                    tagcount = None
            else:
                # no count found in the tag string
                # return the whole tag string
                tagname = tagstr
                tagcount = None
        return {'name':tagname,'count':tagcount}


    def get_tags(self):
        """retrieve a list of tags
          where each element is a dictinary
          of name and count"""

        taglist = []

        try:
            taglinks = self.find_elements_in_owner(self.locators['taglink'])
        except NoSuchElementException:
            taglinks = []

        for tl in taglinks:
            tag = self._parse_tag(tl.text)
            taglist.append(tag)

        return taglist


    def click_tag(self,tagname):
        """click on a tag"""

        taglinks = self.find_elements_in_owner(self.locators['taglink'])
        for tl in taglinks:
            tag = self._parse_tag(tl.text)
            if tagname == tag['name']:
                tl.click()
                break
        else:
            # tagname does not exist
            raise NoSuchTagException("tag: \"%s\"" % tagname)


class TagsList_Locators_Base(object):
    """locators for TagsList object"""

    locators = {
        'base'      : "css=.tags",
        'taglink'   : "css=.tags a",
    }

