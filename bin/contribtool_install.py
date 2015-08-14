#!/usr/bin/env python

# usage:
#     ./contribtool_install [options]
#
# options:
#    --config <hub-config>
#
# examples:
#
#     ./contribtool_install \
#       --config hub.conf \
#       toolname
#

import hubcheck
import json

class ContribtoolInstallTool(hubcheck.Tool):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):
        super(ContribtoolInstallTool,self).__init__(logfile,loglevel)

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging()


    def command(self):

        if (len(self.options.remainder) != 1):
            raise RuntimeError("Wrong # arguments, use --help for help: %s"
                % (self.options.remainder))

        toolname = self.options.remainder[0]

        locators = self.testdata.get_locators()
        hostname = self.testdata.find_url_for('https')
        url = "https://%s" % (hostname)

        hc = hubcheck.Hubcheck(hostname=hostname,locators=locators)

        self.start_recording_xvfb('contribtool_install.mp4')

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        cm = hubcheck.ContainerManager()

        try:
            # launch the browser
            hc.browser.get(url)

            # login to the website as the tool manager
            hc.utils.account.login_as(adminuser,adminpass)

            # install the tool through contribtool
            hc.utils.contribtool.install(toolname,adminuser,adminpass)

            # try launching the tool
            hc.utils.contribtool.launch(toolname,adminuser,adminpass)

            # logout of the website as the tool developer
            hc.utils.account.logout()

        except Exception as e:
            hc.browser.take_screenshot(
                self.screenshot_filepath('contribtool_install'))
            raise

        finally:
            # close the browser and cleanup
            hc.browser.close()
            self.stop_recording_xvfb()

            # shut down all of the tool session containres
            cm.stop_all()


if __name__=='__main__':

    tool = ContribtoolInstallTool()
    tool.run()
