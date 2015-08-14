import pytest
import sys
import time
import os
import json

import hubcheck

pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.hcunit_tools,
               pytest.mark.pageobjects,
             ]

TOOLNAME = 'hutt'
toolconfigfile = os.path.join(hubcheck.conf.settings.data_dir,
                              TOOLNAME,TOOLNAME+'.json')
with open(toolconfigfile,"r") as f:
    toolconfig = json.load(f)

TOOLDATA = [
    ('name'              , toolconfig['toolinfo']['name']),
    ('title'             , toolconfig['toolinfo']['title']),
    ('version'           , toolconfig['toolinfo']['version']),
    ('description'       , toolconfig['toolinfo']['description']),
    ('vncwidth'          , toolconfig['toolinfo']['vncwidth']),
    ('vncheight'         , toolconfig['toolinfo']['vncheight']),
    ('toolaccess'        , toolconfig['toolinfo']['toolaccess']),
    ('toolaccessgroups'  , toolconfig['toolinfo']['toolaccessgroups']),
    ('codeaccess'        , toolconfig['toolinfo']['codeaccess']),
    ('projectaccess'     , toolconfig['toolinfo']['projectaccess']),
    ('devteam'           , toolconfig['toolinfo']['devteam']),
]

TOOLFILEDATA = {}
for (k,v) in toolconfig['files'].items():
    TOOLFILEDATA.update({os.path.join(hubcheck.conf.settings.data_dir,TOOLNAME,k) : v})

TOOLPAGEDATA = toolconfig['infopage']


@pytest.mark.hcunit_tools_pipeline_page
class TestHCUnitToolsPipelinePage(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        self.testtoolname = TOOLNAME

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolmanager')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject('ToolsPipelinePage')
        self.po.goto_page()


    def test_search_for_function(self):
        """
        check that users can enter search terms on tools pipeline page
        """

        self.po.search_for(self.testtoolname)


    def test_goto_page_number_function(self):
        """
        check that users can navigate to pages
        """

        self.po.form.footer.display_limit(5)
        self.po.goto_page_number(2)


    def test_get_caption_function(self):
        """
        check users can retrieve the list top caption (description and counts)
        """

        caption = self.po.form.get_caption()
        assert caption != '', \
            'no caption returned from get_caption() function'


    def test_get_caption_description_function(self):
        """
        check users can retrieve the list top caption description
        """

        desc = self.po.form.get_caption_description()
        assert desc != '', \
            'no caption description returned'


    def test_get_caption_counts_function(self):
        """
        check users can retrieve the list top caption counts
        """

        counts = self.po.form.get_caption_counts()
        assert len(counts) == 3, \
            'counts missing elements: %s' % (counts)

        for count in counts:
            assert count >= 0, \
                'invalid count, expected positive integer: %s' % (count)


    def test_get_pagination_counts_function(self):
        """
        check that users can get the pagination counts
        from the bottom of the page
        """

        (displaystart,displayend,total) = self.po.get_pagination_counts()
        assert(displaystart)
        assert(displayend)
        assert(total)


    def test_get_current_page_number_function(self):
        """
        check that users can retrieve the current page number from pagination
        """

        pagename = self.po.get_current_page_number()
        assert pagename == "1", "expected '1', received '%s'" % (pagename)


    def test_get_current_page_number2(self):
        """
        go to the second page and check users can get the current page number
        """

        self.po.form.footer.display_limit(5)
        self.po.goto_page_number(2)
        pagenumber = self.po.get_current_page_number()
        assert pagenumber == "2", "expected '2', received '%s'" % (pagenumber)


    def test_get_link_page_numbers_function(self):
        """
        check that users can get a list of page numbers that are links
        """

        self.po.form.footer.display_limit(5)
        pagenumbers = self.po.get_link_page_numbers()
        # FIXME: should probably get a better test or relax this one
        #        to allow for hubs with no tools, or one page of tools
        assert len(pagenumbers) != 0, "there are no pages"


    def test_search_for_tool_by_alias(self):
        """
        check that users can iterate through the rows on the page
        and search for tools
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)


    def test_navigate_status_page_by_title(self):
        """
        check that users can navigate to a tool's status page
        by using the title link.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_title()


    def test_navigate_status_page_by_alias(self):
        """
        check that users can navigate to a tool's status page
        by using the alias link.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_alias()


    def test_navigate_status_page_by_status(self):
        """
        check that users can navigate to a tool's status page
        by using the status link.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_status()


    def test_navigate_resource_page(self):
        """
        check that users can navigate to a tool's resource page.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_resource()


    def test_navigate_history_page(self):
        """
        check that users can navigate to a tool's ticket/history page.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_history()


    def test_navigate_wiki_page(self):
        """
        check that users can navigate to a tool's project wiki page.
        """

        self.po.search_for(self.testtoolname)

        foundRow = None

        for i in self.po.form.search_result_rows():
            if i.value()['alias'] == self.testtoolname:
                foundRow = i
                break

        assert foundRow is not None, \
            "while iterating through search results," \
            + " did not find a row with the name %s" \
            % (self.testtoolname)

        foundRow.goto_wiki()


    def test_get_row_by_position(self):
        """
        check users can retrieve row index of a tool
        """

        self.po.search_for(self.testtoolname)
        row_position = 0

        row = self.po.form.search_results.get_row_by_position(row_position)
        row_value = row.value()

        assert row_value is not None, \
            "row at position %d returned None" % (row_position)

        assert row_value['title'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty title property"

        assert row_value['details'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty details property"

        assert row_value['alias'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty alias property"

        assert row_value['status'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty status property"

        assert row_value['time'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty time property"


    def test_get_row_by_position_wrap_negative(self):
        """
        check users can use negative wrap around to get row index
        """

        self.po.search_for(self.testtoolname)

        row_position = -1
        row = self.po.form.search_results.get_row_by_position(row_position)
        row_value = row.value()

        assert row_value is not None, \
            "row at position %d returned None" % (row_position)

        assert row_value['title'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty title property"

        assert row_value['details'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty details property"

        assert row_value['alias'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty alias property"

        assert row_value['status'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty status property"

        assert row_value['time'] != '', \
            "row at position %d returned" % (row_position) \
            + " with empty time property"


    def test_get_row_by_position_index_equals_maxrows(self):
        """
        check that users can not get row indicies equal to maxrows
        """

        self.po.search_for(self.testtoolname)

        maxrows = self.po.form.search_results.num_rows()
        row_position = maxrows

        with pytest.raises(IndexError):
            row = self.po.form.search_results.get_row_by_position(row_position)

#        assert err is True, \
#            "retrieving row by position, while row index is maxrows\
#            (%d) does not produce an IndexError" % (row_position)


    def test_get_row_by_position4(self):
        """
        check users can not get row index beyond maxrows
        """

        self.po.search_for(self.testtoolname)

        maxrows = self.po.form.search_results.num_rows()
        row_position = maxrows + 1

        with pytest.raises(IndexError):
            row = self.po.form.search_results.get_row_by_position(row_position)

#        assert err is True, \
#            "retrieving row by position, while row index" \
#            + " (%d) is beyond maxrows (%d) does" % (row_position,maxrows) \
#            + " not produce an IndexError"\


    def test_get_row_by_property(self):
        """
        check users can retrieve a row by property
        """

        self.po.search_for(self.testtoolname)

        row = self.po.form.search_results.get_row_by_property(
                'alias',self.testtoolname)
        row_value = row.value()

        assert row_value['alias'] == self.testtoolname, \
            "row returned with wrong alias: received" \
            + " '%s', expected '%s'" % (row_value['alias'],self.testtoolname)


@pytest.mark.hcunit_tools_create_page
class TestHCUnitToolsCreatePage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool resource registration form
    """

    def setup_method(self,method):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject('ToolsCreatePage')
        self.po.goto_page()


    def test_populate_form_function(self):
        """
        check that we can populate the tools create page form
        """

        self.po.populate_form(TOOLDATA)


    def test_submit_form_function_empty(self):
        """
        check that we can submit an empty tools create page form
        """

        self.po.submit_form()


    def test_submit_form_function_with_data(self):
        """
        check that we can populate and submit the tools create page form
        """

        self.po.submit_form(TOOLDATA)


    def test_goto_all_tools_function(self):
        """
        check that we can click the link to go to the list of all tools
        """

        self.po.goto_all_tools()
        assert self.po.is_on_page() is False, \
            "Clicking the 'All Tools' link"\
            + " led us back to the tool create page"


@pytest.mark.hcunit_tools_status_registered_page
@pytest.mark.usefixtures("setup_tool_state_registered")
class TestHCUnitToolsStatusRegisteredPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the registered state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusRegisteredPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


#    def test_cancel_tool_function(self):
#        """
#        check that users can press the cancel tool link
#        """
#
#        self.po.cancel_tool()
##        assert self.po.is_on_page() is True, \
##            "Clicking the tool message link" \
##            + " led us away from the tool status page"


    def test_goto_forge_function(self):
        """
        check that users can navigate to the hub forge page
        """

        self.po.goto_forge()
        assert self.po.is_on_page() is False, \
            "Clicking the tool forge link" \
            + " led us back to the tool status page"


    def test_get_forge_name_function(self):
        """
        check that users can retrieve the forge name
        """

        t = self.po.get_forge_name()
        assert t != '', \
            "Retrieving tool forge name returned an empty string"


    def test_get_time_since_request_function(self):
        """
        check that users can navigate to the hub forge page
        """

        t = self.po.get_time_since_request()
        assert t != '', \
            "Retrieving time since last status change returned an empty string"


    def test_get_todo_register_status_function(self):
        """
        check that the registered "todo" item is completed
        """

        status = self.po.get_todo_register_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Register returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_upload_status_function(self):
        """
        check that the upload "todo" item is incomplete
        """

        status = self.po.get_todo_upload_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Upload returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_toolpage_status_function(self):
        """
        check that the toolpage "todo" item is todo
        """

        status = self.po.get_todo_toolpage_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Toolpage returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.xfail(reason='test fails if tool page has been created')
    def test_goto_todo_toolpage_create_function(self):
        """
        check that users can navigate to the toolpage create link
        """

        self.po.goto_todo_toolpage_create()
        assert self.po.is_on_page() is False, \
            "Clicking the toolpage create link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_preview_function(self):
        """
        check that users can navigate to the toolpage preview link
        """

        self.po.goto_todo_toolpage_preview()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page preview link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_edit_function(self):
        """
        check that users can navigate to the toolpage edit link
        """

        self.po.goto_todo_toolpage_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page edit link" \
            + " led us back to the tool status page"


    def test_get_todo_test_approve_status_function(self):
        """
        check that the approve "todo" item is incomplete
        """

        status = self.po.get_todo_test_approve_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Test Approve returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_publish_status_function(self):
        """
        check that the publish "todo" item is incomplete
        """

        status = self.po.get_todo_publish_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Publish returned" \
            + " %s, expected one of %s" % (status,expected)


@pytest.mark.hcunit_tools_status_created_page
@pytest.mark.usefixtures("setup_tool_state_created")
class TestHCUnitToolsStatusCreatedPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the created state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusCreatedPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


    @pytest.mark.skipif(True,
        reason="haven't finished wiring cancel_tool function")
    def test_cancel_tool_function(self):
        """
        check that users can press the cancel tool link
        """

        self.po.cancel_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the tool cancel link" \
            + " led us away from the tool status page"


    def test_goto_forge_function(self):
        """
        check that users can navigate to the hub forge page
        """

        self.po.goto_forge()
        assert self.po.is_on_page() is False, \
            "Clicking the tool forge link" \
            + " led us back to the tool status page"


    def test_get_forge_name_function(self):
        """
        check that users can retrieve the forge name
        """

        t = self.po.get_forge_name()
        assert t != '', \
            "Retrieving tool forge name returned an empty string"


    def test_goto_wiki_function(self):
        """
        check that users can navigate to the tool's wiki page
        """

        self.po.goto_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool forge link" \
            + " led us back to the tool status page"


    def test_get_wiki_name_function(self):
        """
        check that users can retrieve the tool's wiki name
        """

        t = self.po.get_wiki_name()
        assert t != '', \
            "Retrieving tool forge name returned an empty string"


    def test_goto_getting_started_function(self):
        """
        check that users can navigate to the tool's getting started page
        """

        self.po.goto_getting_started()
        assert self.po.is_on_page() is False, \
            "Clicking the tool forge link" \
            + " led us back to the tool status page"


    @pytest.mark.usefixtures("finalize_set_tool_state_created")
    def test_flip_status_to_uploaded_function(self):
        """
        check that users can click the link to flip the tool status to uploaded
        """

        self.po.flip_status_to_uploaded()
        assert self.po.is_on_page() is True, \
            "Clicking the tool forge link" \
            + " led us back to the tool status page"


    def test_get_todo_register_status_function(self):
        """
        check that the registered "todo" item is completed
        """

        status = self.po.get_todo_register_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Register returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_upload_status_function(self):
        """
        check that the upload "todo" item is incomplete
        """

        status = self.po.get_todo_upload_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Upload returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.usefixtures("finalize_set_tool_state_created")
    def test_goto_todo_upload_done_function(self):
        """
        check that users can flip the tool status uing the upload done link
        """

        self.po.goto_todo_upload_done()
        assert self.po.is_on_page() is True, \
            "Clicking the remaining steps upload done link" \
            + " led us back to the tool status page"


    def test_goto_todo_upload_howto_function(self):
        """
        check that users can navigate to the upload howto page
        """

        self.po.goto_todo_upload_howto()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps upload howto link" \
            + " led us back to the tool status page"


    def test_get_todo_toolpage_status_function(self):
        """
        check that the toolpage "todo" item is todo
        """

        status = self.po.get_todo_toolpage_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Toolpage returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.xfail(reason='test fails if tool page has been created')
    def test_goto_todo_toolpage_create_function(self):
        """
        check that users can navigate to the toolpage create link
        """

        self.po.goto_todo_toolpage_create()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page create link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_preview_function(self):
        """
        check that users can navigate to the toolpage preview link
        """

        self.po.goto_todo_toolpage_preview()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page preview link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_edit_function(self):
        """
        check that users can navigate to the toolpage edit link
        """

        self.po.goto_todo_toolpage_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page edit link" \
            + " led us back to the tool status page"


    def test_get_todo_test_approve_status_function(self):
        """
        check that the approve "todo" item is incomplete
        """

        status = self.po.get_todo_test_approve_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Test Approve returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_publish_status_function(self):
        """
        check that the publish "todo" item is incomplete
        """

        status = self.po.get_todo_publish_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Publish returned" \
            + " %s, expected one of %s" % (status,expected)


@pytest.mark.hcunit_tools_status_uploaded_page
@pytest.mark.usefixtures("setup_tool_state_uploaded")
class TestHCUnitToolsStatusUploadedPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the uploaded state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusUploadedPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


    @pytest.mark.skipif(True,
        reason="haven't finished wiring cancel_tool function")
    def test_cancel_tool_function(self):
        """
        check that users can press the cancel tool link
        """

        self.po.cancel_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the tool cancel link" \
            + " led us away from the tool status page"


    def test_get_time_since_request_function(self):
        """
        check that users can retrieve the time since the request
        """

        t = self.po.get_time_since_request()
        assert t != '', \
            "Retrieving the time since request was made returned a blank string"


    def test_get_todo_register_status_function(self):
        """
        check that the registered "todo" item is completed
        """

        status = self.po.get_todo_register_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Register returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_upload_status_function(self):
        """
        check that the upload "todo" item is incomplete
        """

        status = self.po.get_todo_upload_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Upload returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_toolpage_status_function(self):
        """
        check that the toolpage "todo" item is todo
        """

        status = self.po.get_todo_toolpage_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Toolpage returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.xfail(reason='test fails if tool page has been created')
    def test_goto_todo_toolpage_create_function(self):
        """
        check that users can navigate to the toolpage create link
        """

        self.po.goto_todo_toolpage_create()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page create link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_preview_function(self):
        """
        check that users can navigate to the toolpage preview link
        """

        self.po.goto_todo_toolpage_preview()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page preview link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_edit_function(self):
        """
        check that users can navigate to the toolpage edit link
        """

        self.po.goto_todo_toolpage_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page edit link" \
            + " led us back to the tool status page"


    def test_get_todo_test_approve_status_function(self):
        """
        check that the approve "todo" item is incomplete
        """

        status = self.po.get_todo_test_approve_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Test Approve returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_publish_status_function(self):
        """
        check that the publish "todo" item is incomplete
        """

        status = self.po.get_todo_publish_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Publish returned" \
            + " %s, expected one of %s" % (status,expected)


@pytest.mark.hcunit_tools_status_installed_page
@pytest.mark.usefixtures("setup_tool_state_installed")
class TestHCUnitToolsStatusInstalledPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the installed state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusInstalledPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


    @pytest.mark.skipif(True,
        reason="haven't finished wiring cancel_tool function")
    def test_cancel_tool_function(self):
        """
        check that users can press the cancel tool link
        """

        self.po.cancel_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the tool cancel link" \
            + " led us away from the tool status page"


    def test_goto_launch_tool_function(self):
        """
        check that users can launch the dev version of the tool
        """

        self.po.goto_launch_tool()
        assert self.po.is_on_page() is False, \
            "Clicking the launch tool link" \
            + " led us back to the tool status page"


    def test_goto_tool_page_function(self):
        """
        check that users can navigate to the tool page
        (create or review) from the what's next section
        """

        self.po.goto_tool_page()
        assert self.po.is_on_page() is False, \
            "Clicking the create or review tool page link" \
            + " led us back to the tool status page"


    def test_goto_warning_create_function(self):
        """
        check that users can navigate to the create tool page
        from the what's next section's warning box
        """

        self.po.goto_tool_page()
        assert self.po.is_on_page() is False, \
            "Clicking the create or review tool page link" \
            + " led us back to the tool status page"


    @pytest.mark.skipif(True,
        reason='tool page needs to be created before\
                the approve link is enabled')
    @pytest.mark.usefixtures("finalize_set_tool_state_installed")
    def test_flip_status_to_approved_function(self):
        """
        check that users can flip the status to approved
        from the what's next section
        """

        self.po.flip_status_to_approved()
        assert self.po.is_on_page() is False, \
            "Clicking the create or review tool page link" \
            + " led us back to the tool status page"


    @pytest.mark.usefixtures("finalize_set_tool_state_installed")
    def test_flip_status_to_updated_function(self):
        """
        check that users can flip the status to updated
        from the what's next section
        """

        self.po.flip_status_to_updated()
        assert self.po.is_on_page() is True, \
            "Clicking the flip status to updated link" \
            + " led away from the tool status page"


    def test_get_todo_register_status_function(self):
        """
        check that the registered "todo" item is completed
        """

        status = self.po.get_todo_register_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Register returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_upload_status_function(self):
        """
        check that the upload "todo" item is incomplete
        """

        status = self.po.get_todo_upload_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Upload returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_toolpage_status_function(self):
        """
        check that the toolpage "todo" item is todo
        """

        status = self.po.get_todo_toolpage_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Toolpage returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.xfail(reason='test fails if tool page has been created')
    def test_goto_todo_toolpage_create_function(self):
        """
        check that users can navigate to the toolpage create link
        """

        self.po.goto_todo_toolpage_create()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page create link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_preview_function(self):
        """
        check that users can navigate to the toolpage preview link
        """

        self.po.goto_todo_toolpage_preview()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page preview link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_edit_function(self):
        """
        check that users can navigate to the toolpage edit link
        """

        self.po.goto_todo_toolpage_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page edit link" \
            + " led us back to the tool status page"


    def test_get_todo_test_approve_status_function(self):
        """
        check that the approve "todo" item is incomplete
        """

        status = self.po.get_todo_test_approve_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Test Approve returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.skipif(True,
        reason='tool page needs to be created before\
                the approve link is enabled')
    def test_goto_todo_approve_tool_function(self):
        """
        check that users can flip the tool status to approved
        from the remaining steps section
        """

        self.po.goto_todo_approve_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the remaining steps tool page edit link" \
            + " led us away from the tool status page"


    @pytest.mark.usefixtures("finalize_set_tool_state_installed")
    def test_goto_todo_update_tool_function(self):
        """
        check that users can flip the tool status to updated
        from the remaining steps section
        """

        self.po.goto_todo_update_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the remaining steps tool page edit link" \
            + " led us away from the tool status page"


    def test_get_todo_publish_status_function(self):
        """
        check that the publish "todo" item is incomplete
        """

        status = self.po.get_todo_publish_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Publish returned" \
            + " %s, expected one of %s" % (status,expected)


@pytest.mark.hcunit_tools_status_approved_page
@pytest.mark.usefixtures("setup_tool_state_approved")
class TestHCUnitToolsStatusApprovedPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the approved state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusApprovedPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


    @pytest.mark.skipif(True,
        reason="haven't finished wiring cancel_tool function")
    def test_cancel_tool_function(self):
        """
        check that users can press the cancel tool link
        """

        self.po.cancel_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the tool cancel link" \
            + " led us away from the tool status page"


    def test_goto_tool_page_function(self):
        """
        check that users can navigate to the tool information
        page from the what's new section
        """

        self.po.goto_tool_page()
        assert self.po.is_on_page() is False, \
            "Clicking the tool information page link" \
            + " led us back to the tool status page"


    def test_get_tool_page_name_function(self):
        """
        check that users can retrieve the url for the tool
        information page from the what's new section
        """

        t = self.po.get_tool_page_name()
        assert t != '', \
            "Retrieving the tool information page url from" \
            + " the what's next section returned a blank string"


    def test_get_time_since_request_function(self):
        """
        check that users can navigate to the hub forge page
        """

        t = self.po.get_time_since_request()
        assert t != '', \
            "Retrieving time since last status change returned an empty string"


    def test_get_todo_register_status_function(self):
        """
        check that the registered "todo" item is completed
        """

        status = self.po.get_todo_register_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Register returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_upload_status_function(self):
        """
        check that the upload "todo" item is incomplete
        """

        status = self.po.get_todo_upload_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Upload returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_toolpage_status_function(self):
        """
        check that the toolpage "todo" item is todo
        """

        status = self.po.get_todo_toolpage_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Toolpage returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.xfail(reason='test fails if tool page has been created')
    def test_goto_todo_toolpage_create_function(self):
        """
        check that users can navigate to the toolpage create link
        """

        self.po.goto_todo_toolpage_create()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page create link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_preview_function(self):
        """
        check that users can navigate to the toolpage preview link
        """

        self.po.goto_todo_toolpage_preview()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page preview link" \
            + " led us back to the tool status page"


    def test_goto_todo_toolpage_edit_function(self):
        """
        check that users can navigate to the toolpage edit link
        """

        self.po.goto_todo_toolpage_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the remaining steps tool page edit link" \
            + " led us back to the tool status page"


    def test_get_todo_test_approve_status_function(self):
        """
        check that the approve "todo" item is incomplete
        """

        status = self.po.get_todo_test_approve_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Test Approve returned" \
            + " %s, expected one of %s" % (status,expected)


    def test_get_todo_publish_status_function(self):
        """
        check that the publish "todo" item is incomplete
        """

        status = self.po.get_todo_publish_status()
        expected = ['incomplete','complete','todo']
        assert status in expected, \
            "Remaining Steps - Publish returned" \
            + " %s, expected one of %s" % (status,expected)


    @pytest.mark.usefixtures("finalize_set_tool_state_approved")
    def test_goto_todo_update_tool_function(self):
        """
        check that users can flip the tool status to updated
        from the remaining steps section
        """

        self.po.goto_todo_update_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the remaining steps tool page edit link" \
            + " led us away from the tool status page"


@pytest.mark.hcunit_tools_status_published_page
@pytest.mark.usefixtures("setup_tool_state_published")
class TestHCUnitToolsStatusPublishedPage(hubcheck.testcase.TestCase2):
    """
    tests related to the tool status page for a tool in the published state
    """


    def setup(self):

        # setup a web browser
        self.browser.get(self.https_authority)

        self.username,self.password = \
            self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(self.username,self.password)
        self.po = self.catalog.load_pageobject(
            'ToolsStatusPublishedPage',TOOLNAME)
        self.po.goto_page()


    def test_goto_all_tools_page_function(self):
        """
        check that users can navigate to the all tools page
        """

        self.po.goto_all_tools_page()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the all tools page" \
            + " led us back to the tool status page"


    def test_goto_new_tool_form_function(self):
        """
        check that users can navigate to the new tool form
        """

        self.po.goto_new_tool_form()
        assert self.po.is_on_page() is False, \
            "Clicking the link to go to the new tool form" \
            + " led us back to the tool status page"


    def test_get_tool_state_function(self):
        """
        check that users can retrieve the state of the tool
        """

        toolstate = self.po.get_tool_state()
        valid_states = ['Registered','Created','Uploaded',\
                        'Installed','Approved','Published']
        assert toolstate in valid_states, \
            "Retrieving the tool state produced an invalid result: %s" \
            % (toolstate)


    def test_goto_tool_info_edit_function(self):
        """
        check that users can navigate to edit the toolinfo page
        """

        self.po.goto_toolinfo_edit()
        assert self.po.is_on_page() is False, \
            "Clicking the tool info edit link" \
            + " led us back to the tool status page"


    def test_get_tool_info_title_function(self):
        """
        check that users can retrieve the title from toolinfo block
        """

        t = self.po.get_toolinfo_title()
        assert t != '', \
            "Retrieving tool info title returned an empty string"


    def test_get_tool_info_version_function(self):
        """
        check that users can retrieve the version from toolinfo block
        """

        t = self.po.get_toolinfo_version()
        assert t != '', \
            "Retrieving tool info version returned an empty string"


    def test_get_tool_info_glance_function(self):
        """
        check that users can retrieve the "at a glance" from toolinfo block
        """

        t = self.po.get_toolinfo_glance()
        assert t != '', \
            "Retrieving tool info glance returned an empty string"


    def test_get_tool_info_vnc_geometry_function(self):
        """
        check that users can retrieve the vnc geometry from toolinfo block
        """

        t = self.po.get_toolinfo_vncgeometry()
        assert t != '', \
            "Retrieving tool info vncgeometry returned an empty string"


    def test_get_tool_info_tool_access_function(self):
        """
        check that users can retrieve the tool access from toolinfo block
        """

        t = self.po.get_toolinfo_toolaccess()
        assert t != '', \
            "Retrieving tool info tool access returned an empty string"


    def test_get_tool_info_code_access_function(self):
        """
        check that users can retrieve the code access from toolinfo block
        """

        t = self.po.get_toolinfo_codeaccess()
        assert t != '', \
            "Retrieving tool info code access returned an empty string"


    def test_get_tool_info_wiki_access_function(self):
        """
        check that users can retrieve the wiki access from toolinfo block
        """

        t = self.po.get_toolinfo_wikiaccess()
        assert t != '', \
            "Retrieving tool info wiki access returned an empty string"


    def test_get_tool_info_dev_team_function(self):
        """
        check that users can retrieve the development team from toolinfo block
        """

        t = self.po.get_toolinfo_devteam()
        assert t != '', \
            "Retrieving tool info dev team returned an empty string"


    def test_goto_tooldev_history_function(self):
        """
        check that users can navigate to the tool's history ticket
        """

        self.po.goto_tooldev_history()
        assert self.po.is_on_page() is False, \
            "Clicking the tool history link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_wiki_function(self):
        """
        check that users can navigate to the tool's wiki
        """

        self.po.goto_tooldev_wiki()
        assert self.po.is_on_page() is False, \
            "Clicking the tool wiki link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_source_code_function(self):
        """
        check that users can navigate to the tool's source code
        """

        self.po.goto_tooldev_source_code()
        assert self.po.is_on_page() is False, \
            "Clicking the tool source code link" \
            + " led us back to the tool status page"


    def test_goto_tooldev_timeline_function(self):
        """
        check that users can navigate to the tool's timeline
        """

        self.po.goto_tooldev_timeline()
        assert self.po.is_on_page() is False, \
            "Clicking the tool timeline link" \
            + " led us back to the tool status page"


    def test_open_tooldev_message_function(self):
        """
        check that users can open the tools message box
        """

        self.po.open_tooldev_message()
        assert self.po.is_on_page() is True, \
            "Clicking the tool message link" \
            + " led us away from the tool status page"


    @pytest.mark.skipif(True,
        reason="haven't finished wiring cancel_tool function")
    def test_cancel_tool_function(self):
        """
        check that users can press the cancel tool link
        """

        self.po.cancel_tool()
        assert self.po.is_on_page() is True, \
            "Clicking the tool cancel link" \
            + " led us away from the tool status page"


    def test_goto_tool_page_function(self):
        """
        check that users can navigate to the tool information
        page from the what's new section
        """

        self.po.goto_tool_page()
        assert self.po.is_on_page() is False, \
            "Clicking the tool information page link" \
            + " led us back to the tool status page"


    def test_get_tool_page_name_function(self):
        """
        check that users can retrieve the url for the tool
        information page from the what's new section
        """

        t = self.po.get_tool_page_name()
        assert t != '', \
            "Retrieving the tool information page url from" \
            + " the what's next section returned a blank string"


    @pytest.mark.usefixtures("finalize_set_tool_state_published")
    def test_flip_status_to_updated_function(self):
        """
        check that users can navigate to the hub forge page
        """

        t = self.po.flip_status_to_updated()
        assert self.po.is_on_page() is True, \
            "Clicking the tool information page link" \
            + " led us away from the tool status page"


