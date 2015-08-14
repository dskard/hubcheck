#!/usr/bin/env python

# usage:
#     ./contribtool_publish [options]
#
# options:
#    --toolname hppt
#    --toolversion r13
#
# examples:
#     ./contribtool_publish --toolname hppt --config hub.conf
#     ./contribtool_publish --toolname hppt --config hub.conf


import hubcheck


class ContribtoolPublishTool(hubcheck.Tool):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):
        super(ContribtoolPublishTool,self).__init__(logfile,loglevel)

        self.command_parser.add_argument(
            '--toolname',
            help='name of the tool to compile',
            action="store",
            dest="toolname",
            default=None,
            type=str)

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging()


    def command(self):

        if self.options.toolname is None:
            msg = 'no toolname provided, use the --toolname flag'
            raise RuntimeError(msg)

        # toolname = self.options.remainder[0]

        locators    = self.testdata.get_locators()
        httpsurl    = self.testdata.find_url_for('https')
        url = "https://%s" % (httpsurl)

        # start up a selenium webdriver based browser
        self.browser = hubcheck.browser.Firefox()

        if self.browser is None:
            msg = 'Failed to initialize web browser.'
            self.logger.error(msg)
            raise RuntimeError(msg)

        self.start_recording_xvfb('contribtool_publish.mp4')

        adminuser,adminpass = self.testdata.find_account_for('toolmanager')

        try:
            self.browser.get(url)

            self.catalog = hubcheck.PageObjectCatalog(locators)
            self.utils = hubcheck.Utils(httpsurl,self.browser,self.catalog)

            # login to the website as a tool manager
            self.utils.account.login_as(adminuser,adminpass)

            # publish the tool through contribtool
            self.utils.contribtool.publish(self.options.toolname)

            # try launching the tool to make sure it was published

            # logout of the website
            self.utils.account.logout()

        except Exception as e:
            self.browser.take_screenshot(
                self.screenshot_filepath('contribtool_publish'))
            raise

        finally:
            # close the browser and cleanup
            self.browser.close()
            self.stop_recording_xvfb()


if __name__=='__main__':

    tool = ContribtoolPublishTool()
    tool.run()
