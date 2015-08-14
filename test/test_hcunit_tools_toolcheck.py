import pytest
import sys
import hubcheck
import time
import os
import json


toolcheck_path = hubcheck.utils.which('toolcheck')
toolcheck_dir = os.path.dirname(toolcheck_path)
sys.path.append(toolcheck_dir)

import toolcheck


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.hcunit_tools_toolcheck,
             ]


# configure the test tool

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


# configure the toolcheck module

ToolCheck = toolcheck.ToolCheck
toolcheck.CREATE_LOGGER = False


class TestHCUnitToolsToolcheck(hubcheck.testcase.TestCase2):

    def setup_method(self,method):
        pass


    @pytest.mark.usefixtures("setup_tool_state_registered")
    def test_create(self):
        """
        check if toolcheck moves a tool in the
        registered state to the created state
        """

        sys.argv = ['toolcheck',
                    '--config', hubcheck.conf.settings.configpath,
                    '--tool', TOOLNAME,
                    '--screenshotdir', os.getcwd(),
                    '--videodir', os.getcwd(),
                    '--no-xvfb',
                   ]

        t = ToolCheck()
        t.run()


    @pytest.mark.usefixtures("setup_tool_state_uploaded")
    @pytest.mark.usefixtures("setup_populate_tool_repository")
    def test_install(self):
        """
        check if toolcheck moves a tool in the
        uploaded state to the installed state
        """


        sys.argv = ['toolcheck',
                    '--config', hubcheck.conf.settings.configpath,
                    '--tool', TOOLNAME,
                    '--screenshotdir', os.getcwd(),
                    '--videodir', os.getcwd(),
                    '--no-xvfb',
                   ]

        t = ToolCheck()
        t.run()


    @pytest.mark.usefixtures("setup_tool_state_approved")
    def test_publish(self):
        """
        check if toolcheck moves a tool in the
        approved state to the published state
        """


        sys.argv = ['toolcheck',
                    '--config', hubcheck.conf.settings.configpath,
                    '--tool', TOOLNAME,
                    '--screenshotdir', os.getcwd(),
                    '--videodir', os.getcwd(),
                    '--no-xvfb',
                   ]

        t = ToolCheck()
        t.run()
