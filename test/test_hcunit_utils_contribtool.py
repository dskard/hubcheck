import pytest
import sys
import hubcheck
import time
import os
import json

from hubcheck.actionobjects.contribtool import Contribtool

pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.hcunit_utils_contribtool,
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

if toolconfig['license']['sourceaccess'] == "closed source":
    TOOLLICENSEDATA = [
        ('sourceaccess' , toolconfig['license']['sourceaccess']),
        ('reason'       , toolconfig['license']['reason'])
    ]
elif toolconfig['license']['sourceaccess'] == "open source":
    TOOLLICENSEDATA = [
        ('sourceaccess' , toolconfig['license']['sourceaccess']),
        ('licensetext'  , toolconfig['license']['licensetext'])
        ('authorize'    , toolconfig['license']['authorize'])
    ]


class TestHCUnitUtilsContribtool(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        self.testtoolname = TOOLNAME

        # setup a web browser
        self.browser.get(self.https_authority)

        self.contribtool = Contribtool(self.https_uri,self.browser,self.catalog)


    def test_register(self):
        """
        try registering a tool
        """

        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        message = self.contribtool.register(TOOLNAME,TOOLDATA)

        success_msg = 'Tool information successfully registered'
        fail_msg = 'Tool with this name already exists! Please provide' \
                   + ' a unique name\nTool with this title already exists!' \
                   + ' Please provide a unique title'

        assert message == success_msg or message[0] == fail_msg , \
            'Problem registering tool: %s' % (message)


    @pytest.mark.usefixtures("setup_tool_state_registered")
    def test_create(self):
        """
        try creating a tool
        """

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        self.utils.account.login_as(adminuser,adminpass)

        self.contribtool.create(TOOLNAME)


    def test_checkout_repository(self):
        """
        try checking out a tool repository
        """


        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.contribtool.checkout_repository(TOOLNAME,username,userpass)


    @pytest.mark.usefixtures("setup_tool_state_created")
    @pytest.mark.usefixtures("setup_clear_tool_repository")
    def test_upload(self):
        """
        try uploading files to a tool repository

        this test could fail because the files were already
        uploaded to the repository.
        """


        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        self.contribtool.upload(TOOLNAME,TOOLFILEDATA,username,userpass)


    @pytest.mark.hcunit_utils_contribtool_update
    @pytest.mark.usefixtures("setup_tool_state_installed")
    def test_update(self):
        """
        try uploading files to a tool repository
        """


        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        self.contribtool.update(TOOLNAME,username,userpass)


    @pytest.mark.usefixtures("setup_tool_state_uploaded")
    def test_install(self):
        """
        try installing files to a tool repository
        """


        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        self.utils.account.login_as(adminuser,adminpass)

        self.contribtool.install(TOOLNAME,adminuser,adminpass)


    @pytest.mark.usefixtures("setup_tool_state_installed")
    def test_launch(self):
        """
        try launching the installed tool
        """


        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        self.contribtool.launch(TOOLNAME,username,userpass)


    @pytest.mark.usefixtures("setup_tool_state_installed")
    def test_edit_tool_page(self):
        """
        try editing the tool page with reasonable inputs
        """


        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        self.contribtool.edit_tool_page(TOOLNAME,TOOLPAGEDATA)


    @pytest.mark.usefixtures("setup_tool_state_installed")
    def test_approve(self):
        """
        try approving a tool
        """

        username,userpass = self.testdata.find_account_for('toolsubmitter')

        self.utils.account.login_as(username,userpass)

        self.contribtool.approve(TOOLNAME,TOOLLICENSEDATA)


    @pytest.mark.usefixtures("setup_tool_state_approved")
    def test_publish(self):
        """
        try publishing a tool
        """

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        self.utils.account.login_as(adminuser,adminpass)

        self.contribtool.publish(TOOLNAME)


