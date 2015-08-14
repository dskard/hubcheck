#!/usr/bin/env python

# usage:
#     ./contribtool_update [options]
#
# options:
#    --config <hub-config>
#
# examples:
#     ./contribtool_update \
#       --config hub.conf \
#       toolname
#


import hubcheck


class ContribtoolUpdateTool(hubcheck.Tool):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):
        super(ContribtoolUpdateTool,self).__init__(logfile,loglevel)

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

        self.start_recording_xvfb('contribtool_update.mp4')

        username,userpass = self.testdata.find_account_for('toolsubmitter')

        cm = hubcheck.ContainerManager()

        try:
            # launch the browser
            hc.browser.get(url)

            # login to the website as the tool developer
            hc.utils.account.login_as(username,userpass)

            # update the tool through contribtool
            hc.utils.contribtool.update(toolname,username,userpass)

            # logout of the website as the tool developer
            hc.utils.account.logout()

        except Exception as e:
            hc.browser.take_screenshot(
                self.screenshot_filepath('contribtool_update'))
            raise

        finally:
            # close the browser and cleanup
            hc.browser.close()
            self.stop_recording_xvfb()

            # shut down all of the tool session containres
            cm.stop_all()


if __name__=='__main__':

    tool = ContribtoolUpdateTool()
    tool.run()
