import logging
import sys
import traceback

from ..browser import Firefox
from ..pageobjects import PageObjectCatalog
from ..actionobjects import HubzeroActions


class Hubcheck(object):

    def __init__(self,
            hostname='hubzero.org',
            http_port=80,
            https_port=443,
            locators='hubzero',
            browser_type='Firefox',
            screenshot_dir=None,
            video_dir=None):

        self.logger = logging.getLogger()

        self.hostname = hostname
        self.http_port = http_port
        self.https_port = https_port
        self.locators = locators
        self.screenshot_dir = screenshot_dir
        self.video_dir = video_dir
        self.browser = None
        self.catalog = None
        self.utils = None

        # setup the browser
        supported_browsers = ['Firefox']
        if browser_type not in supported_browsers:
            raise ValueError('unsupported browser: %s, choose one of %s' \
                             % (browser_type,supported_browsers))

        if browser_type == 'Firefox':
            self.browser = Firefox()

        self.catalog = PageObjectCatalog(self.locators,self.browser)
        self.utils = HubzeroActions(hostname,self.browser,self.catalog)


    def __del__(self):

        # close the browser
        if self.browser is not None:
            try:
                self.browser.close()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))
            self.browser = None


