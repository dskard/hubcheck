import os
import logging
import copy

from selenium import webdriver

from pkg_resources import resource_listdir, resource_filename

from .browser import Browser
from .browser import MIMETYPES

from ..conf import settings


FIREFOX_PREFS = {
    # allow script for original website
    'noscript.autoAllow' : 3,

    # disable firefox updates
    'app.update.enabled' : False,

    ## update privacy setting
    # 'privacy.clearOnShutdown.cache' : True,
    # 'privacy.clearOnShutdown.cookies' : True,
    # 'privacy.clearOnShutdown.downloads' : True,
    # 'privacy.clearOnShutdown.formdata' : True,
    # 'privacy.clearOnShutdown.history' : True,
    # 'privacy.clearOnShutdown.sessions' : True,
    # 'privacy.clearOnShutdown.siteSettings' : True,

    # turn off info bars that change the position of elements on the page
    # after the page has loaded. you see this a lot on nees.org
    'plugins.hide_infobar_for_missing_plugin' : True,
    'plugins.hide_infobar_for_outdated_plugin' : True,

    # other stuff from cuddlefish project and mozilla automation

    # no startup or homepage
    'browser.startup.page' : 0,
    'extensions.checkCompatibility.nightly' : False,
    'browser.startup.homepage' : 'about:blank',
    'startup.homepage_welcome_url' : 'about:blank',
    'devtools.errorconsole.enabled' : True,

    # Disable extension updates and notifications.
    'extensions.update.enabled' : False,
    'extensions.update.notifyUser' : False,

    # From:
    # http://hg.mozilla.org/mozilla-central/file/1dd81c324ac7/build/automation.py.in#l372
    # Only load extensions from the application and user profile.
    # AddonManager.SCOPE_PROFILE + AddonManager.SCOPE_APPLICATION
    'extensions.enabledScopes' : 5,
    # Disable metadata caching for installed add-ons by default
    'extensions.getAddons.cache.enabled' : False,
    # Disable intalling any distribution add-ons
    'extensions.installDistroAddons' : False,
    'extensions.testpilot.runStudies' : False,

    # From:
    # http://hg.mozilla.org/mozilla-central/file/1dd81c324ac7/build/automation.py.in#l388
    # Make url-classifier updates so rare that they won't affect tests.
    'urlclassifier.updateinterval' : 172800,
    # Point the url-classifier to a nonexistent local URL for fast failures.
    'browser.safebrowsing.provider.0.gethashURL' : 'http://localhost/safebrowsing-dummy/gethash',
    'browser.safebrowsing.provider.0.keyURL' : 'http://localhost/safebrowsing-dummy/newkey',
    'browser.safebrowsing.provider.0.updateURL' : 'http://localhost/safebrowsing-dummy/update',
    # Point update checks to a nonexistent local URL for fast failures.
    'extensions.update.url' : 'http://localhost/extensions-dummy/updateURL',
    'extensions.blocklist.url' : 'http://localhost/extensions-dummy/blocklistURL',
    # Make sure opening about:addons won't hit the network.
    'extensions.webservice.discoverURL' : 'http://localhost/extensions-dummy/discoveryURL',

    'webdriver.firefox.useExisting' : False,
    'webdriver.development' : False,
    'webdriver.reap_profile' : True,
    'webdriver.firefox.logfile' : '/tmp/firefox.log',

    # don't warn me about old insecure java plugins
    'plugin.scan.plid.all' : False,
    'plugin.update.notifyUser' : False,

    # don't flash the download manager when downloading
    'browser.download.manager.closeWhenDone' : True,
    'browser.download.manager.flashCount' : 0,
    'browser.download.manager.focusWhenStarting' : False,
    'browser.download.manager.openDelay' : 99999,
    'browser.download.manager.showAlertOnComplete' : False,
    'browser.download.manager.showWhenStarting' : False,
    'browser.download.manager.showAlertInterval' : 0,
    'browser.download.panel.firstSessionCompleted' : True,
    'browser.download.panel.shown' : True,
}


class Firefox(Browser):
    """hubcheck webdriver interface"""

    def setup_browser_preferences(self):

        preferences = copy.deepcopy(FIREFOX_PREFS)

        # setup a firefox profile
        # if noscript is installed, we want to automatically
        # allow the scripts from the host of the page we are
        # visiting.

        self.logger.debug("using default firefox profile")
        self.profile = webdriver.FirefoxProfile()

        self.logger.debug("loading browser extensions")
        xpidir = os.path.join(settings.profiles_dir, 'firefox','xpi')
        if os.path.isdir(xpidir):
            extensions = ['firebug-1.11.4.xpi',
                          'firefinder_for_firebug-1.2.5-fx.xpi']

            # install extensions
            for extension in extensions:
                self.profile.add_extension(os.path.join(xpidir, extension))

            # fix extension config settings
            preferences['extensions.firebug.currentVersion'] = '1.11.4'


        # setup firefox to automatically download files
        # instead of showing the download dialog box
        self.logger.debug(
            "updating browser mimetypes for automatic file download")

        self.downloaddir = os.path.abspath(self.downloaddir)
        if self.downloaddir:
            if not os.path.isdir(self.downloaddir):
                os.mkdir(self.downloaddir,0700)


        all_mimetypes = copy.deepcopy(MIMETYPES)
        all_mimetypes.extend(self.mimetypes)

        preferences['browser.download.folderList'] = 2
        preferences['browser.download.manager.showWhenStarting'] = False
        preferences['browser.download.dir'] = self.downloaddir
        preferences['browser.helperApps.neverAsk.saveToDisk'] = \
            ','.join(all_mimetypes)

        self.logger.info("updating browser preferences")
        for key,value in preferences.items():
            self.logger.debug("setting preference: %s -> %s" % (key,value))
            self.profile.set_preference(key,value)

        self.profile.update_preferences()


    def launch(self):

        self.setup_browser_preferences()

        self.start_proxy_client()

        self.logger.debug("launching local firefox browser")
        self._browser = webdriver.Firefox(
                            firefox_profile=self.profile,
                            proxy=self.proxy_client)

        self.setup_browser_size_and_position()
