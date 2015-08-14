#!/usr/bin/env python

# Verify that all the pieces needed to install a tool exist, compile the source
# code, and publish the tool.
#
# usage:
#     ./toolcheck [options]
#
# options:
#    --config <hub-config>
#    --tool <toolname>
#    --compile-only
#
# examples:
#
#     ./toolcheck --config hub.conf --tool toolname
#

import hubcheck

CREATE_LOGGER = True

class ToolCheck(hubcheck.Tool):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):
        super(ToolCheck,self).__init__(logfile,loglevel)

        self.command_parser.add_argument(
            '--tool',
            help='name of the tool to create, install, or publish',
            action="store",
            dest="toolname",
            default='',
            type=str)

        self.command_parser.add_argument(
            '--compile-only',
            help='login to workspace, compile, and install code only (dont flip status on website)',
            action="store_true",
            dest="compile_only",
            default=False)

        self.command_parser.add_argument(
            '--revision',
            help='specify revision of tool that should be compiled and installed, revision must be checked out',
            action="store",
            dest="revision",
            default='dev',      # could also be rXXX or current
            type=str)

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging(CREATE_LOGGER)


    def command(self):

        if (len(self.options.remainder) != 0):
            raise RuntimeError("Wrong # arguments, use --help for help: %s"
                % (self.options.remainder))

        toolname = self.options.toolname

        locators = self.testdata.get_locators()
        url = "https://%s" % (hubcheck.conf.settings.hub_hostname)

        self.hc = hubcheck.Hubcheck(hostname=hubcheck.conf.settings.hub_hostname,
                               locators=locators)

        self.start_recording_xvfb('toolcheck.mp4')

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        cm = hubcheck.ContainerManager()

        try:
            # launch the browser
            self.hc.browser.get(url)

            # login to the website as the tool manager
            self.hc.utils.account.login_as(adminuser,adminpass)

            # go to the tools pipeline page
            po = self.hc.catalog.load_pageobject('ToolsPipelinePage')
            po.goto_page()
            po.form.footer.display_limit('1000')

            # if the current state is.............then do...
            states = { 'registered' : { 'fxn'  : self.create_tool,
                                        'args' : (),
                                      },
                       'updated'    : { 'fxn'  : self.install_tool,
                                        'args' : (adminuser,adminpass),
                                      },
                       'uploaded'   : { 'fxn'  : self.install_tool,
                                        'args' : (adminuser,adminpass),
                                      },
                       'approved'   : { 'fxn'  : self.publish_tool,
                                        'args' : (),
                                      },
                     }

            if toolname == '':
                # get all tool aliases matching statuses
                statuses = states.keys()
                alias_list = po.form.get_aliases_by_status(statuses)

                for (status,toolnames) in alias_list.items():
                    for toolname in toolnames:
                        # perform the action
                        states[status]['fxn'](toolname,*states[status]['args'])
            else:
                # process a single tool
                self.hc.utils.contribtool.goto_tool_status_page(toolname)
                po = self.hc.catalog.load_pageobject('ToolsStatusRegisteredPage')
                status = po.get_tool_state().lower()
                if status in states.keys():
                    states[status]['fxn'](toolname,*states[status]['args'])
                else:
                    # nothing for tool admin to do in this state
                    pass


            # logout of the website as the tool developer
            self.hc.utils.account.logout()


        except Exception as e:
            self.hc.browser.take_screenshot(
                self.screenshot_filepath('contribtool_install'))
            raise

        finally:
            # close the browser and cleanup
            self.hc.browser.close()
            self.stop_recording_xvfb()

            # shut down all of the tool session containres
            cm.stop_all()


    def create_tool(self,toolname):

        return self.hc.utils.contribtool.create(toolname)


    def install_tool(self,toolname,adminuser,adminpass):

        if self.options.compile_only is False:
            self.hc.utils.contribtool.push_admin_install_button(toolname)

        # perform pre-compile tests here
        # check for:
        # * makefile in src directory
        # * invoke script executable
        # * invoke script calls /usr/bin/invoke_app, not old version
        # * nanowhim 

        self.hc.utils.contribtool.compile_code(toolname,adminuser,adminpass)

        # perform post-compile tests here
        # check for:
        # * matlab code is compiled

        if self.options.compile_only is False:
            self.hc.utils.contribtool.flip_tool_status(
                'ToolsStatusUploadedAdminPage',toolname,'Installed')

            # try launching the tool
            self.hc.utils.contribtool.launch(toolname,adminuser,adminpass)


    def publish_tool(self,toolname):

        return self.hc.utils.contribtool.publish(toolname)


if __name__=='__main__':

    tool = ToolCheck()
    tool.run()
