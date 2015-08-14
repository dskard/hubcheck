#! /usr/bin/env python

# usage:
#     ./contribtool_create [options] <tool-config>
#
# options:
#    --config <hub-config>
#
# examples:
#
#     ./contribtool_create \
#       --config hub.conf \
#       workspace.json
#


import hubcheck
import json

class ContribtoolCreateTool(hubcheck.Tool):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):
        super(ContribtoolCreateTool,self).__init__(logfile,loglevel)

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging()


    def command(self):

        if (len(self.options.remainder) != 1):
            raise RuntimeError("Wrong # arguments, use --help for help: %s"
                % (self.options.remainder))

        # parse the tool configuration
        with open(self.options.remainder[0],"r") as f:
            toolconfig = json.load(f)

        locators = self.testdata.get_locators()
        hostname = self.testdata.find_url_for('https')
        url = "https://%s" % (hostname)

        hc = hubcheck.Hubcheck(hostname=hostname,locators=locators)

        self.start_recording_xvfb('contribtool_create.mp4')

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        toolname = toolconfig['toolinfo']['name']
        toolinfo = toolconfig['toolinfo']

        cm = hubcheck.ContainerManager()

        try:
            # launch the browser
            hc.browser.get(url)

            # login to the website as the tool manager
            hc.utils.account.login_as(adminuser,adminpass)

            # create the repository (if necessary)
            hc.utils.contribtool.create(toolname)

            # check out the repository to make sure it was created
            hc.utils.contribtool.checkout_repository(
                toolname,adminuser,adminpass)

            # logout of the website as the tool manager
            hc.utils.account.logout()

        except Exception as e:
            hc.browser.take_screenshot(
                self.screenshot_filepath('contribtool_create'))
            raise

        finally:
            # close the browser and cleanup
            hc.browser.close()
            self.stop_recording_xvfb()

            # shut down all of the tool session containres
            cm.stop_all()


if __name__=='__main__':

    tool = ContribtoolCreateTool()
    tool.run()
