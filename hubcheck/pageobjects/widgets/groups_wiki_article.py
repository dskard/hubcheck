from hubcheck.exceptions import NoSuchFileAttachmentError

from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly

import re
import time

class GroupsWikiArticle(BasePageWidget):
    def __init__(self, owner, locatordict):
        super(GroupsWikiArticle,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsWikiArticle_Locators = self.load_class('GroupsWikiArticle_Locators')
        TagsList = self.load_class('TagsList')

        # update this object's locator
        self.locators.update(GroupsWikiArticle_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.pagetext       = TextReadOnly(self,{'base':'pagetext'})
        self.timestamp      = TextReadOnly(self,{'base':'timestamp'})
        self.tags           = TagsList(self,{'base':'tags'})
        self.authors        = TextReadOnly(self,{'base':'authors'})
        self.create         = Link(self,{'base':'create'})

        # update the component's locators with this objects overrides
        self._updateLocators()

    def _checkLocatorsWikiPage(self,widgets=None,cltype='WikiPage'):

        widgets = [self.pagetext,self.timestamp,self.tags]
        super(GroupsWikiArticle,self)._checkLocators(widgets,cltype)


    def _checkLocatorsKnowledgeBase(self,widgets=None,cltype='KnowledgeBase'):

        widgets = [self.pagetext,self.timestamp,self.tags,self.authors]
        super(GroupsWikiArticle,self)._checkLocators(widgets,cltype)


    def _checkLocatorsNewPage(self,widgets=None,cltype='NewPage'):

        widgets = [self.create]
        super(GroupsWikiArticle,self)._checkLocators(widgets,cltype)


    def get_tags(self):

        return self.tags.get_tags()


    def click_tag(self,tagname):

        return self.tags.click_tag(tagname)


    def get_page_text(self):

        return self.pagetext.value


    def get_authors(self):

        # e = self.find_element(self.locators['authors'])
        # authortext = re.sub(r'by ','',e.text)
        # authortext = re.sub(r', ',',',authortext)
        # authorlist = authortext.split(',')
        # return authorlist
        authorlist = []
        authorElements = self.find_elements(self.locators['authorlink'])
        for authorElement in authorElements:
            authorlist.append(authorElement.text)
        return authorlist


    def is_created(self):

        return not self.create.is_present()


    def create_page(self):

        return self.create.click()


    def download_attachment(self,attachment):

        wikipagetext = self.find_element(self.locators['pagetext'])
        links = self.find_elements(self.locators['links'],wikipagetext)
        download_element = None
        for link in links:
            href = link.get_attribute('href')
            if re.search(attachment,href):
                download_element = link
                break
        else:
            raise NoSuchFileAttachmentError(
                    "attachment not found on page: %s" % (attachment))

        download_element.click()


    # this should probably be called is_file_downloadable
    # and is_file_attached, should just look to see if the
    # file is on the page.
    def is_file_attached(self,filepath):

        # filepath should be the full path to a real file on disk
        # because we download a copy and compare md5sum hashes to
        # see if that exact file is attached to the wiki.
        import os
        import md5
        def md5sum_of_file(filename):
            f = open(filename, 'r')
            data = f.read()
            f.close()
            m = md5.new()
            m.update(data)
            digest = m.digest()
            return digest

        fname = os.path.basename(filepath)

        self.download_attachment(fname)

        # wait for file to be downloaded
        # FIXME: should consider using webdriver wait?
        # outfile = os.path.join(os.getcwd(),fname)
        outfile = os.path.join(self._po.downloaddir,fname)
        count = 0
        while count < 5:
            time.sleep(2)
            if os.path.exists(outfile):
                break
            count = count + 1

        # if the file wasn't downloaded, bail.
        if os.path.exists(outfile) == False:
            raise ValueError("file was not downloaded: %s" % (outfile))

        # compare the md5sum of the file we uploaded
        # to the md5sum of the file we downloaded
        inDigest = md5sum_of_file(filepath)
        outDigest = md5sum_of_file(outfile)

        # remove the downloaded file
        os.remove(outfile)

        return (inDigest == outDigest)


class GroupsWikiArticle_Locators_Base(object):
    """locators for GroupsWikiArticle object"""

    locators = {
        'base'       : "css=#page_content",
        'pagetext'   : "css=.wikipage",
        'timestamp'  : "css=.timestamp",
        'tags'       : "css=.article-tags",
        'authors'    : "css=.topic-authors",
        'authorlink' : "css=.topic-authors a",
        'create'     : "xpath=//a[text()='create it?']",
        'links'      : "css=#page_content a",
    }

class GroupsWikiArticle_Locators_Base_2(object):
    """locators for GroupsWikiArticle object"""

    locators = {
        'base'       : "css=#page_content",
        'pagetext'   : "css=.main",
        'timestamp'  : "css=.timestamp",
        'tags'       : "css=.article-tags",
        'authors'    : "css=.topic-authors",
        'authorlink' : "css=.topic-authors a",
        'create'     : "xpath=//a[text()='create it?']",
        'links'      : "css=#page_content a",
    }
