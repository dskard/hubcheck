import datetime
import hubcheck
import logging
import os
import re
import sys
import time
import unittest
import pytest

from hubcheck.exceptions import NoSuchFileAttachmentError
from hubcheck.exceptions import NoSuchMemberException
from hubcheck.exceptions import NoSuchTagException


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.pageobjects,
               pytest.mark.hcunit_groups
             ]


GROUPID = "hcunittestgroupbase"
GROUPDATA = {
    'groupid'       : GROUPID,
    'title'         : "hubcheck unit test group base",
    'tags'          : ['hubcheck','hc'],
    'public_desc'   : 'hubcheck unit test public description',
    'private_desc'  : 'hubcheck unit test private description',
    'join_policy'   : 'Invite Only',
    'privacy'       : 'Hidden',
}


IMAGENAME = 'app2.png'
IMAGEPATH = os.path.join(hubcheck.conf.settings.data_dir,'images',IMAGENAME)
DOCNAME   = 'report.docx'
DOCPATH   = os.path.join(hubcheck.conf.settings.data_dir,'uploads',DOCNAME)

ARTICLEAUTHORS = ['author1','author2']

ARTICLEID1 = "hcunitgroupswikibasepagewiki"
ARTICLEDATA1 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID1,
    'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
    'upload'        : IMAGEPATH,
    'access'        : 'Wiki page anyone can edit',
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID2 = "hcunitgroupswikibasepageknowledgebase"
ARTICLEDATA2 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID2,
    'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
    'upload'        : IMAGEPATH,
    'access'        : 'Knowledge article with specific authors',
    'authors'       : ARTICLEAUTHORS,
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID3 = 'sdfhalkjhfdskjhsdfsdfa'

ARTICLEID4 = "hcunitgroupswikibasepageknowledgebase2"
ARTICLEDATA4 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID4,
    'pagetext'      : "test page text\n[[File(%s)]]" % (DOCNAME),
    'upload'        : DOCPATH,
    'access'        : 'Knowledge article with specific authors',
    'authors'       : ARTICLEAUTHORS,
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID5 = "hcunitgroupswikideletewiki"
ARTICLEDATA5 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID5,
    'pagetext'      : "test page text",
    'upload'        : None,
    'access'        : 'Wiki page anyone can edit',
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID6 = "hcunitgroupswikideletewikitobedeleted"
ARTICLEDATA6 = {
    'title'         : ARTICLEID6,
    'pagetext'      : "test page text",
    'access'        : 'Wiki page anyone can edit',
}

ARTICLEID7 = "hcunitgroupswikieditwiki"
ARTICLEDATA7 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID7,
    'pagetext'      : "test page text",
    'upload'        : None,
    'access'        : 'Wiki page anyone can edit',
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID8 = "hcunitgroupswikirenamewiki"
ARTICLEDATA8 = {
    'parent'        : None,
    'template'      : None,
    'title'         : ARTICLEID8,
    'pagetext'      : "test page text",
    'upload'        : None,
    'access'        : 'Wiki page anyone can edit',
    'lockpage'      : False,
    'tags'          : ['hcunit','hc'],
    'summary'       : 'test summary text',
}

ARTICLEID9 = "hcunitgroupswikirenamewikitoberenamed"
ARTICLEDATA9 = {
    'title'         : ARTICLEID9,
    'pagetext'      : "test page text",
    'access'        : 'Wiki page anyone can edit',
}

def pretest_setup_groups(browser,catalog,utils,testdata):

    username,password = testdata.find_account_for('groupmanager')

    utils.account.login_as(username,password)
    utils.groups.create_group(GROUPID,GROUPDATA)
    utils.account.logout()


def pretest_setup_groups_wiki(browser,catalog,utils,testdata):

    username,password = testdata.find_account_for('groupmanager')

    utils.account.login_as(username,password)
    utils.groups.create_group(GROUPID,GROUPDATA)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID1,ARTICLEDATA1)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID2,ARTICLEDATA2)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID4,ARTICLEDATA4)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID5,ARTICLEDATA5)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID6,ARTICLEDATA6)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID7,ARTICLEDATA7)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID8,ARTICLEDATA8)
    utils.groups.create_group_wiki(GROUPID,ARTICLEID9,ARTICLEDATA9)
    utils.account.logout()

@pytest.mark.hcunit_groupsbase_page
class hcunit_groupbasepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)
        GroupsBasePage = self.catalog.load('GroupsBasePage')
        self.po = GroupsBasePage(self.browser,self.catalog,GROUPID)
        self.po.goto_page()


    def test_get_menu_items(self):
        """
        get the list of group menu items using the
        get_menu_items() function
        """

        l = len(self.po.get_menu_items())
        self.assertTrue(l != 0,"get_menu_items() returned no items")


    def test_get_options_items(self):
        """
        get the list of group manager options items using the
        get_options_items() function.
        """

        l = len(self.po.get_options_items())
        self.assertTrue(l != 0,"get_options_items() returned no items")


    def test_get_title_function(self):
        """
        get the group title using the get_title() function
        """

        self.assertFalse(self.po.get_title() == "","group page title is blank")


    def test_goto_group_page_function(self):
        """
        navigate to the group page using the title link
        """

        self.po.goto_group_page()


    def test_goto_options_item_function(self):
        """
        try clicking on each available option item
        """

        links = self.po.get_options_items()
        for link in links:
            self.po.goto_page()
            self.po.goto_options_item(link)


    def test_goto_menu_item_function(self):
        """
        try clicking on each available menu item
        """

        #FIXME:
        # trying to open the wiki tag (i think)
        # triggers the manager options menu

        links = self.po.get_menu_items()

        for link in links:
            self.po.goto_page()
            self.po.goto_menu_item(link)


    def test_is_protected_functions(self):
        """
        check if a menu item is protected
        """

        links = self.po.get_menu_items()

        for link in links:
            self.po.goto_page()
            self.po.is_menu_item_protected(link)


    def test_get_privacy_function(self):
        """
        get the group privacy setting
        """

        privacy = self.po.get_privacy()
        self.assertTrue(privacy == GROUPDATA['privacy'],
            "privacy mismatch: orginally set privacy to '%s',\
             read privacy as '%s'" % (GROUPDATA['privacy'],privacy))


    def test_get_join_policy_function(self):
        """
        get the group join policy
        """

        join_policy = self.po.get_join_policy()
        self.assertTrue(join_policy == GROUPDATA['join_policy'],
            "join policy mismatch: origianlly set join\
             policy to '%s', read join policy as '%s'" \
             % (GROUPDATA['join_policy'],join_policy))


    @hubcheck.utils.hub_version('1.0','1.1.5')
    def test_get_create_date_function_1(self):
        """
        get the create date of the group

        date format for hubzero version <= 1.1.5
        """

        create_date_text = self.po.get_create_date()
        create_date = datetime.datetime.strptime(create_date_text,'%d %b, %Y')
        self.assertTrue(create_date.date() <= datetime.datetime.today().date(),
            "create date = %s, today = %s" % (create_date.date(),
                                              datetime.datetime.today().date()))


    @hubcheck.utils.hub_version(min_version='1.2')
    def test_get_create_date_function_2(self):
        """
        get the create date of the group

        date format changed for hubzero 1.2
        """

        create_date_text = self.po.get_create_date()
        create_date = datetime.datetime.strptime(create_date_text,'%d %b %Y')
        self.assertTrue(create_date.date() <= datetime.datetime.today().date(),
            "create date = %s, today = %s" % (create_date.date(),
                                              datetime.datetime.today().date()))


    def test_group_exists_function_1(self):
        """
        check that the group_exists() function returns True for a group
        that exists
        """

        exists = self.po.group_exists()
        self.assertTrue(exists,"group_exists() returned '%s' for\
                                a group that should exist. expected\
                                True" % (exists))


    def test_group_exists_function_2(self):
        """
        check that the group_exists() function returns False for a group
        that does not exists
        """

        GroupsBasePage = self.catalog.load('GroupsBasePage')
        self.po = GroupsBasePage(self.browser,self.catalog,'hctestgroupthisgroupshouldneverexist')
        self.po.goto_page()
        exists = self.po.group_exists()
        self.assertFalse(exists,"group_exists() returned '%s' for\
                                a group that should exist. expected\
                                False" % (exists))


@pytest.mark.hcunit_groupsdelete_page
class hcunit_groupsdeletepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)
        GroupsDeletePage = self.catalog.load('GroupsDeletePage')
        self.po = GroupsDeletePage(self.browser,self.catalog,GROUPID)
        self.po.goto_page()


    def test_populate_form_function_1(self):
        """
        try populating the form with no data
        """

        self.po.populate_form({})


    def test_populate_form_function_2(self):
        """
        try populating the form with data
        """

        data = {
            'message'       : "hubcheck unit test delete group %s" % (GROUPID),
            'confirm'       : True,
        }
        self.po.populate_form(data)

    @pytest.mark.skipif(True,reason="hubzero tickets #5267, #4053")
    def test_submit_form_function_1(self):
        """
        try submitting a blank form
        """

        self.po.submit_form()


    @pytest.mark.skipif(True,reason="hubzero tickets #5267, #4053")
    def test_submit_form_function_2(self):
        """
        try submitting a blank form
        """

        self.po.submit_form({})


    @pytest.mark.skipif(True,reason="hubzero tickets #5267, #4053")
    def test_submit_form_function_3(self):
        """
        try submitting a form with data
        """

        data = {
            'message'       : "hubcheck unit test invite to group %s" % (GROUPID),
            'confirm'       : True,
        }
        self.po.submit_form(data)


@pytest.mark.hcunit_groupsinvite_page
class hcunit_groupsinvitepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)
        GroupsInvitePage = self.catalog.load('GroupsInvitePage')
        self.po = GroupsInvitePage(self.browser,self.catalog,GROUPID)
        self.po.goto_page()


    def test_populate_form_function_1(self):
        """
        try to populate the form with no data
        """

        self.po.populate_form({})


    def test_populate_form_function_2(self):
        """
        try to populate the form with data
        """

        data = {
            'name'          : "h%d" % (time.time()),
            'message'       : "hubcheck unit test invite to group %s" % (GROUPID),
        }
        self.po.populate_form(data)


    def test_submit_form_function_1(self):
        """
        try to submit a blank form
        """

        self.po.submit_form()


    def test_submit_form_function_2(self):
        """
        try to submit a blank form
        """

        self.po.submit_form({})


    def test_submit_form_function_3(self):
        """
        try to submit the form with data
        """

        data = {
            'name'          : "h%d" % (time.time()),
            'message'       : "hubcheck unit test invite to group %s" % (GROUPID),
        }
        self.po.submit_form(data)


@pytest.mark.hcunit_groupsnew_page
class hcunit_groupsnewpage(hubcheck.testcase.TestCase):

#    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

#        if self.__class__.run_pretest_setup is True:
#            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
#            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('registeredworkspace')

        self.utils.account.login_as(self.username,self.password)
        GroupsNewPage = self.catalog.load('GroupsNewPage')
        self.po = GroupsNewPage(self.browser,self.catalog)
        self.po.goto_page()


    def test_create_group_function_1(self):
        """
        try to submit the form with no data
        """

        self.po.create_group({})


    def test_create_group_function_2(self):
        """
        try to submit the form with data
        """

        groupid = "h%d" % (time.time())
        data = {
            'groupid'       : groupid,
            'title'         : "hubcheck unit test groups new page %s" % (groupid),
            'tags'          : ['hubcheck','hc'],
            'public_desc'   : 'hubcheck unit test public description',
            'private_desc'  : 'hubcheck unit test private description',
            'join_policy'   : 'Invite Only',
            'privacy'       : 'Hidden',
        }
        self.po.create_group(data)


@pytest.mark.hcunit_groupsoverview_page
class hcunit_groupsoverviewpage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        # create the group page if necessary
        self.utils.account.login_as(self.username,self.password)

        GroupsOverviewPage = self.catalog.load('GroupsOverviewPage')
        self.po = GroupsOverviewPage(self.browser,self.catalog,GROUPID)
        self.po.goto_page()


    def test_get_tags_function(self):
        """
        retrieve tags using the get_tags() function
        """

        tags = self.po.get_tags()
        self.assertTrue(len(tags) == 2,"tags = %s" % (tags))


    def test_click_tags_function(self):
        """
        click on tags using the click_tags() function
        """

        tags = self.po.get_tags()
        self.po.click_tag(tags[1]['name'])


    def test_click_tags_function_bad_tag(self):
        """
        try to click a tag that does not exist
        """

        with self.assertRaises(NoSuchTagException) as cm:
            self.po.click_tag('not a real tag')


    def test_get_member_names_function(self):
        """
        retrieve the group member names using get_member_names() function
        """

        displayedMembers = self.po.get_member_names()
        self.assertTrue(len(displayedMembers) > 0,
            "displayedMembers = %s" % (displayedMembers))


    def test_goto_member_profile_function(self):
        """
        click the member name link
        """

        displayedMembers = self.po.get_member_names()
        self.po.goto_member_profile(displayedMembers[0])


    def test_goto_member_profile_function_no_member(self):
        """
        try going to a member profile that does not exist
        """

        with self.assertRaises(NoSuchMemberException) as cm:
            self.po.goto_member_profile('not a real user')


@pytest.mark.hcunit_groups_page
class hcunit_groupspage(hubcheck.testcase.TestCase):

    def setUp(self):

        self.browser.get(self.https_authority)

        GroupsPage = self.catalog.load('GroupsPage')
        self.po = GroupsPage(self.browser,self.catalog)
        self.po.goto_page()


    @hubcheck.utils.hub_version('1.0','1.1.2')
    def test_goto_faq_function(self):
        """
        click the faq link
        """

        self.po.groups.goto_faq()
        # self.assertFalse(po.is_on_page())


    @hubcheck.utils.hub_version('1.0','1.1.2')
    def test_goto_guidelines_function(self):
        """
        click the guidelines link
        """

        self.po.groups.goto_guidelines()
        # self.assertFalse(po.is_on_page())


    @hubcheck.utils.hub_version(min_version='1.1.4')
    def test_goto_need_help_function(self):
        """
        click the need_help link
        """

        self.po.groups.goto_need_help()
        # self.assertFalse(po.is_on_page())


    def test_goto_create_groups_function(self):
        """
        click the create group link
        """

        self.po.groups.goto_create_group()
        # self.assertFalse(po.is_on_page())


    def test_goto_browse_list_function(self):
        """
        click the browse groups link
        """

        self.po.groups.goto_browse_list()
        # self.assertFalse(po.is_on_page())


    def test_search_groups_function(self):
        """
        search for a group name
        """

        self.po.groups.search_groups('searchtext')
        # self.assertFalse(po.is_on_page())


    def test_get_popular_groups_function(self):
        """
        retrieve the list of popular groups
        """

        popular_groups = self.po.groups.get_popular_groups()


    def test_has_info_no_popular_groups(self):
        """
        check if the 'no popular groups' info box is showing
        """

        num_groups = self.po.groups.popular_groups.num_items()
        has_info = self.po.groups.has_info_no_popular_groups()

        if num_groups == 0:
            self.assertTrue(has_info,"no groups are disaplyed and\
                the 'no_popular_groups' info block is not displayed")
        else:
            self.assertFalse(has_info,"%s groups are disaplyed and\
                the 'no_popular_groups' info block is displayed"\
                % (num_groups))


    def test_goto_popular_groups_function(self):
        """
        click the link of all popular groups
        """

        pageurl1 = self.po.current_url()
        for group in self.po.groups.get_popular_groups():
            self.po.groups.goto_popular_group(group)
            pageurl2 = self.po.current_url()
            self.assertTrue(pageurl1 != pageurl2,
                "after pressing popular group link '%s',\
                 on %s, url did not change" % (group,pageurl2))
            self.browser._browser.back()


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikiarticle_page
class hcunit_groupswikiarticlepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups_wiki(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)
        GroupsWikiArticlePage = self.catalog.load('GroupsWikiArticlePage')
        self.po1 = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,ARTICLEID1)
        self.po2 = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,ARTICLEID2)
        self.po3 = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,ARTICLEID3)
        self.po4 = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,ARTICLEID4)


    def test_get_tags_function(self):
        """
        retrieve tags using the get_tags() function
        """

        self.po1.goto_page()
        tags = self.po1.get_tags()
        self.assertTrue(len(tags) == len(ARTICLEDATA1['tags']))
        for t in tags:
            self.assertTrue(t['name'] in ARTICLEDATA1['tags'],
                "tag \"%s\" not in \"%s\"" % (t['name'],ARTICLEDATA1['tags']))


    def test_click_tag_function(self):
        """
        click on each tag using the click_tags function
        """

        self.po1.goto_page()
        tags = self.po1.get_tags()
        for t in tags:
            if not self.po1.is_on_page():
                self.po1.goto_page()
            self.po1.set_page_load_marker()
            self.po1.click_tag(t['name'])
            self.po1.wait_for_page_to_load()
            self.assertFalse(self.po1.is_on_page())


    def test_get_page_text_function(self):
        """
        get wiki article page text using get_page_text function
        """

        self.po1.goto_page()
        text = self.po1.get_page_text()
        self.assertFalse(text == '',
            "page text for %s appears to be empty" % (ARTICLEID1))


    def test_get_authors_function_wiki_page(self):
        """
        retrieve wiki page authors
        """

        self.po1.goto_page()
        authors = self.po1.get_authors()
        self.assertTrue(authors == [],
            "authors list not empty: %s" % authors)


    def test_get_authors_function_knowledge_base(self):
        """
        retrieve knowledge base articles
        """

        self.po2.goto_page()
        authors = self.po2.get_authors()
        self.assertTrue(len(authors) == len(ARTICLEDATA2['authors']))
        # it takes a lot of time to figure out the correct names that
        # should be in the list of authors. so we'll bail on that for now.
        # for a in authors:
        #     self.assertTrue(a in ARTICLEDATA2['authors'],
        #         "author \"%s\" not in \"%s\"" % (a,ARTICLEDATA2['authors']))


    def test_is_created_function_created_page(self):
        """
        check if a wiki page is created
        """

        self.po1.goto_page()
        isCreated = self.po1.is_created()
        self.assertTrue(isCreated,
            "page %s appears not to exist, but it should" % (ARTICLEID1))


    def test_is_created_function_new_page(self):
        """
        check if a new wiki page is created
        """

        self.po3.goto_page()
        isCreated = self.po3.is_created()
        self.assertFalse(isCreated,
            "page %s appears to exist, but should not" % (ARTICLEID3))


    def test_create_page_function(self):
        """
        create a new wiki page
        """

        self.po3.goto_page()
        self.po3.create_page()
        # FIXME: check that we at least changed pages


    def test_download_attachment_function(self):
        """
        download an image attachment on a wiki page
        """

        self.po1.goto_page()
        imagename = os.path.basename(ARTICLEDATA1['upload'])
        self.po1.download_attachment(imagename)


    def test_is_file_attached_function(self):
        """
        check if a file is attached to a wiki page
        """

        self.po4.goto_page()
        self.assertTrue(self.po4.is_file_attached(ARTICLEDATA4['upload']))


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikibase_page
class hcunit_groupswikibasepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups_wiki(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)

        GroupsWikiBasePage = self.catalog.load('GroupsWikiBasePage')
        self.po = GroupsWikiBasePage(self.browser,self.catalog,GROUPID,ARTICLEID1)
        self.po.goto_page()


    def test_get_wiki_title_function(self):
        """
        check locators for the groups wiki base page
        """

        title = self.po.get_wiki_title()
        self.assertTrue(title == ARTICLEID1,
            "title = %s, ARTICLEID1 = %s" % (title,ARTICLEID1))


    def test_goto_new_wiki_page_function(self):
        """
        click the new wiki link
        """

        self.po.goto_new_wiki_page()
        self.assertFalse(self.po.is_on_page())


    def test_goto_wikimenu_article_function(self):
        """
        click the wiki menu article link
        """

        self.po.goto_wikimenu_article()
        self.assertTrue(self.po.is_on_page())


    def test_goto_wikimenu_edit_function(self):
        """
        click the wiki menu edit link
        """

        self.po.goto_wikimenu_edit()
        self.assertFalse(self.po.is_on_page())


    def test_goto_wikimenu_comments_function(self):
        """
        click the wiki menu comments link
        """

        self.po.goto_wikimenu_comments()
        self.assertFalse(self.po.is_on_page())


    def test_goto_wikimenu_history_function(self):
        """
        click the wiki menu history link
        """

        self.po.goto_wikimenu_history()
        self.assertFalse(self.po.is_on_page())


    def test_goto_wikimenu_delete_function(self):
        """
        click the wiki menu delete link
        """

        self.po.goto_wikimenu_delete()
        self.assertFalse(self.po.is_on_page())


    @hubcheck.utils.hub_version('1.0','1.1.2')
    def test_goto_wikimenu_mainpage_function(self):
        """
        click the wiki menu main_page link
        """

        self.po.goto_wikimenu_mainpage()
        self.assertFalse(self.po.is_on_page())


    def test_goto_wikimenu_index_function(self):
        """
        click the wiki menu index link
        """

        self.po.goto_wikimenu_index()
        self.assertFalse(self.po.is_on_page())


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikidelete_page
class hcunit_groupswikideletepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups_wiki(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)

        GroupsWikiDeletePage = self.catalog.load('GroupsWikiDeletePage')
        self.po1 = GroupsWikiDeletePage(self.browser,self.catalog,GROUPID,ARTICLEID5)
        self.po2 = GroupsWikiDeletePage(self.browser,self.catalog,GROUPID,ARTICLEID6)


    def test_confirm_delete_function(self):
        """
        confirm wiki page delete
        """

        self.po1.goto_page()
        self.po1.confirm_delete()
        self.assertTrue(self.po1.form.confirm.value)


    def test_submit_function(self):
        """
        use the submit_form function to delete a wiki page
        """

        self.po1.goto_page()
        self.po1.submit_form()


    def test_delete_wiki_page_function(self):
        """
        use the delete_wiki_page function to delete a wiki page
        """

        self.po2.goto_page()
        self.po2.delete_wiki_page()


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikiedit_page
class hcunit_groupswikieditpage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups_wiki(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)


    def test_goto_rename_function(self):
        """
        click the rename wiki page link
        """

        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        po.goto_page()
        po.goto_rename()
        self.assertFalse(po.is_on_page())


    def test_edit_wiki_page_function(self):
        """
        edit the wiki page using the edit_wiki_page function
        """

        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        po.goto_page()
        newtitle = "edited hc unit - edit wiki page function: %d" % time.time()
        pagetext = 'edited test page text'
        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : newtitle,
            # the is_file_attached function doesn't seem to be able to handle downloading images
            # probably because image files are shown in a lightbox, might need to open the link
            # in an other tab or window, then check for download, then close the tab.
            # 'pagetext'      : "%s\n[[Image(%s)]]" % (pagetext,IMAGENAME),
            # 'upload'        : IMAGEPATH,
            'pagetext'      : "%s\n[[File(%s)]]" % (pagetext,DOCNAME),
            'upload'        : DOCPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hcunit','hc'],
            'summary'       : 'edited test summary text',
        }
        po.edit_wiki_page(data)
        GroupsWikiArticlePage = self.catalog.load('GroupsWikiArticlePage')
        po = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        # self.assertTrue(po.get_page_text() == pagetext,
        adjusted_pagetext = "%s %s" % (pagetext,DOCNAME)
        self.assertTrue(re.search(re.escape(pagetext),po.get_page_text()) is not None,
            "get_page_text() == \'%s\'\npagetext == \'%s\'" \
            % (po.get_page_text(),pagetext))
        self.assertTrue(po.get_wiki_title() == newtitle,
            "get_wiki_title() == \'%s\'\nnewtitle == \'%s\'" \
            % (po.get_wiki_title(),newtitle))
        # self.assertTrue(po.is_file_attached(IMAGEPATH),
        self.assertTrue(po.is_file_attached(DOCPATH),
            "file imagepath does not appear to be attached to the wiki page")
        # should probably have a function that knows how to
        # compare an article page with a dictionary of values


    def test_populate_form_function(self):
        """
        populate the edit wiki page form
        """

        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        po.goto_page()
        newtitle = "edited populate hc unit - edit wiki page function: %d" % time.time()
        pagetext = 'edited populate test page text'
        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : newtitle,
            'pagetext'      : "%s\n[[Image(%s)]]" % (pagetext,IMAGENAME),
            'upload'        : IMAGEPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hcunit','hc'],
            'summary'       : 'edited test summary text',
        }
        po.populate_form(data)


    def test_preview_function(self):
        """
        click the preview button
        """

        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        po.goto_page()
        po.preview_page()


    def test_submit_function(self):
        """
        click the submit button
        """

        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,ARTICLEID7)
        po.goto_page()
        po.submit_form()


    def test_get_uploaded_files_function(self):
        """
        upload files to the wiki page through the edit form
        """

        # create a new wiki page that we can upload files into
        GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        po = GroupsWikiNewPage(self.browser,self.catalog,GROUPID)
        po.goto_page()
        articleid = "hcunitgroupswikieditgetuploadedfiles%d" % (time.time())
        articledata = {
            'title'         : articleid,
            'pagetext'      : "test page text",
            'access'        : 'Wiki page anyone can edit',
        }
        po.create_wiki_page(articledata)

        # edit the wiki page, upload files
        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,articleid)
        po.goto_page()

        imagenames = ['app2.png','app2.jpg','app2.gif']
        uploadfiles = []

        for imagename in imagenames:
            uploadfiles.append(
                os.path.join(hubcheck.conf.settings.data_dir,'images',imagename))

        data = { 'upload' : uploadfiles, }

        po.populate_form(data)
        # FIXME:
        # this wait needs to be inside of populate_form
        # after each image is uploaded
        #po.wait_for_page_to_load()

        # check the uploaded files
        filenames = po.get_uploaded_files()
        self.assertTrue(len(filenames) == 3)
        for imagename in imagenames:
            self.assertTrue(imagename in filenames,
                "missing image: \"%s\" in %s" % (imagename,filenames))


    def test_delete_file_function(self):
        """
        delete files attached to a wiki page through the edit form
        """

        # create a new wiki page that we can upload files into
        GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        po = GroupsWikiNewPage(self.browser,self.catalog,GROUPID)
        po.goto_page()
        articleid = "hcunitgroupswikieditgetdeletedfiles%d" % (time.time())
        articledata = {
            'title'         : articleid,
            'pagetext'      : "test page text",
            'access'        : 'Wiki page anyone can edit',
        }
        po.create_wiki_page(articledata)

        # edit the wiki page, upload files
        GroupsWikiEditPage = self.catalog.load('GroupsWikiEditPage')
        po = GroupsWikiEditPage(self.browser,self.catalog,GROUPID,articleid)
        po.goto_page()

        imagenames = ['app2.png','app2.jpg','app2.gif']
        uploadfiles = []

        for imagename in imagenames:
            uploadfiles.append(
                os.path.join(hubcheck.conf.settings.data_dir,'images',imagename))

        data = { 'upload' : uploadfiles, }

        po.populate_form(data)

        # check the uploaded files
        for imagename in imagenames:
            numUploadedFiles= len(po.get_uploaded_files())
            po.delete_file(imagename)
            newNumUploadedFiles = len(po.get_uploaded_files())
            self.assertTrue(newNumUploadedFiles == (numUploadedFiles-1),
                "Before delete, # files = %d. After delete, # files = %d" \
                % (numUploadedFiles,newNumUploadedFiles))


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikinew_page
class hcunit_groupswikinewpage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)

        GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        self.po = GroupsWikiNewPage(self.browser,self.catalog,GROUPID)
        self.po.goto_page()


    @pytest.mark.hcunit_groupswikicreatefunction
    def test_create_wiki_page_function(self):
        """
        create a new wiki page
        """

        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : 'hc unit - create wiki page function: %d' % time.time(),
            'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
            'upload'        : IMAGEPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hubcheck','hc'],
            'summary'       : 'test summary text',
        }
        self.po.create_wiki_page(data)


    def test_populate_wiki_page_function(self):
        """
        populate the form to create a new wiki page
        """

        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : 'hc unit - populate wiki page function: %d' % time.time(),
            'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
            'upload'        : IMAGEPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hubcheck','hc'],
            'summary'       : 'test summary text',
        }
        self.po.populate_form(data)


    def test_preview_function(self):
        """
        click the preview button
        """

        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : 'hc unit - do preview function: %d' % time.time(),
            'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
            'upload'        : IMAGEPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hubcheck','hc'],
            'summary'       : 'test summary text',
        }
        self.po.populate_form(data)
        self.po.preview_page()


    def test_submit_function(self):
        """
        populate the new wiki page form and submit it
        """

        data = {
            'parent'        : None,
            'template'      : None,
            'title'         : 'hc unit - do submit function: %d' % time.time(),
            'pagetext'      : "test page text\n[[Image(%s)]]" % (IMAGENAME),
            'upload'        : IMAGEPATH,
            'access'        : 'Wiki page anyone can edit',
            'lockpage'      : False,
            'tags'          : ['hubcheck','hc'],
            'summary'       : 'test summary text',
        }
        self.po.populate_form(data)
        self.po.submit_form()


    def test_get_uploaded_files_function(self):
        """
        upload files and attach them to a new wiki page
        """

        imagenames = ['app2.png','app2.jpg','app2.gif']
        uploadfiles = []

        for imagename in imagenames:
            uploadfiles.append(
                os.path.join(hubcheck.conf.settings.data_dir,'images',imagename))

        data = { 'upload' : uploadfiles, }

        self.po.populate_form(data)

        GroupsWikiNewPage = self.catalog.load('GroupsWikiNewPage')
        self.po = GroupsWikiNewPage(self.browser,self.catalog,GROUPID)

        filenames = self.po.get_uploaded_files()
        self.assertTrue(len(filenames) == 3,
            "expected 3 file, only found %s: %s" % (len(filenames),filenames))
        for imagename in imagenames:
            self.assertTrue(imagename in filenames,
                "missing image: \"%s\" in %s" % (imagename,filenames))


    @pytest.mark.hcunit_groupswikicreatedeleteattachment
    def test_delete_file_function(self):
        """
        delete a file attached to a new wiki page form
        """

        imagenames = ['app2.png','app2.jpg','app2.gif']
        uploadfiles = []

        for imagename in imagenames:
            uploadfiles.append(
                os.path.join(hubcheck.conf.settings.data_dir,'images',imagename))

        data = { 'upload' : uploadfiles }

        self.po.populate_form(data)

        # make sure the files were properly uploaded
        numUploadedFiles = len(self.po.get_uploaded_files())
        self.assertTrue(numUploadedFiles == len(uploadfiles),
            "wrong number of files uploaded: received %s, expected %s" \
            % (numUploadedFiles,len(uploadfiles)))

        # test deleting files
        for imagename in imagenames:
            numUploadedFiles = len(self.po.get_uploaded_files())
            self.po.delete_file(imagename)
            newNumUploadedFiles = len(self.po.get_uploaded_files())
            self.assertTrue(newNumUploadedFiles == (numUploadedFiles-1),
                "Before delete, # files = %d. After delete, # files = %d" \
                % (numUploadedFiles,newNumUploadedFiles))


@pytest.mark.hcunit_groupswiki
@pytest.mark.hcunit_groupswikirename_page
class hcunit_groupswikirenamepage(hubcheck.testcase.TestCase):

    run_pretest_setup = True

    def setUp(self):

        self.browser.get(self.https_authority)

        if self.__class__.run_pretest_setup is True:
            pretest_setup_groups_wiki(self.browser,self.catalog,self.utils,self.testdata)
            self.__class__.run_pretest_setup = False

        self.username,self.password = \
            self.testdata.find_account_for('groupmanager')

        self.utils.account.login_as(self.username,self.password)


    def test_submit_function(self):
        """
        press the submit button on the wiki rename page
        """

        GroupsWikiRenamePage = self.catalog.load('GroupsWikiRenamePage')
        po = GroupsWikiRenamePage(self.browser,self.catalog,GROUPID,ARTICLEID8)
        po.goto_page()
        po.submit_form()


    def test_rename_page_function(self):
        """
        try renaming a wiki page using the rename_page function
        """

        # rename the wiki page
        GroupsWikiRenamePage = self.catalog.load('GroupsWikiRenamePage')
        po = GroupsWikiRenamePage(self.browser,self.catalog,GROUPID,ARTICLEID9)
        po.goto_page()
        newpagename = "hcunitrenamenewpagename%d" % (time.time())
        po.rename_page(newpagename)

        # check to see if the renamed wiki page exists
        GroupsWikiArticlePage = self.catalog.load('GroupsWikiArticlePage')
        po = GroupsWikiArticlePage(self.browser,self.catalog,GROUPID,newpagename)
        po.goto_page()
        self.assertTrue(po.is_created(),
            "after renaming %s to %s, wiki page does not exist" \
            % (ARTICLEID9,newpagename))

