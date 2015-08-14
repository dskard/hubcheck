import pprint
import logging
import datetime

from selenium import webdriver

import hubcheck.conf


# block websites that make linkcheck slow
# these are usually blocked by the workspace firewall
# mozillalabs comes from using a nightly version of firefox browser
# many of the others are from login authentication sites
PROXY_BLACKLIST = [
    "http(s)?://.*mozillalabs\\.com/?.*",        # testpilot.mozillalabs.com
    "http(s)?://.*google-analytics\\.com/.*",    # ssl.google-analytics.com
    'http(s)?://.*facebook\\.com/?.*',           # www.facebook.com/login.php
    'http(s)?://.*fbcdn\\.com/?.*',              # www.facebook.com/login.php
    'http(s)?://.*accounts\\.google\\.com/?.*',  # accounts.google.com
    'http(s)?://.*linkedin\\.com/?.*',           # linkedin.com
    'http(s)?://.*twitter\\.com/?.*',            # api.twitter.com
#   'http(s)?://.*purdue\\.edu/apps/account/cas/?.*', # purdue cas
]

MIMETYPES = [
    "appl/text",                        # .doc                      \
    "application/acad",                 # .dwg                      \
    "application/acrobat",              # .pdf                      \
    "application/autocad_dwg",          # .dwg                      \
    "application/doc",                  # .doc, .rtf                \
    "application/dwg",                  # .dwg                      \
    "application/eps",                  # .eps                      \
    "application/futuresplash",         # .swf                      \
    "application/gzip",                 # .gz                       \
    "application/gzipped",              # .gz                       \
    "application/gzip-compressed",      # .gz                       \
    "application/jpg",                  # .jpg                      \
    "application/ms-powerpoint",        # .ppt                      \
    "application/msexcel",              # .xls                      \
    "application/mspowerpnt",           # .ppt                      \
    "application/mspowerpoint",         # .ppt                      \
    "application/msword",               # .doc, .rtf                \
    "application/octet-stream",         # .gz, .zip                 \
    "application/pdf",                  # .pdf                      \
    "application/photoshop",            # .psd                      \
    "application/postscript",           # .ps, .avi, .eps           \
    "application/powerpoint",           # .ppt                      \
    "application/psd",                  # .psd                      \
    "application/rss+xml",              # .rss                      \
    "application/rtf",                  # .rtf                      \
    "application/tar",                  # .tar                      \
    "application/vnd.ms-excel",         # .xls, .xlt, .xla          \
    "application/vnd.ms-excel.addin.macroEnabled.12",                               # .xlam \
    "application/vnd.ms-excel.sheet.binary.macroEnabled.12",                        # .xlsb \
    "application/vnd.ms-excel.sheet.macroEnabled.12",                               # .xlsm \
    "application/vnd.ms-excel.template.macroEnabled.12",                            # .xltm \
    "application/vnd.ms-powerpoint",    # .pps, .ppt, .pot, .ppa    \
    "application/vnd.ms-powerpoint.addin.macroEnabled.12",                          # .ppam \
    "application/vnd.ms-powerpoint.presentation.macroEnabled.12",                   # .pptm \
    "application/vnd.ms-powerpoint.slideshow.macroEnabled.12",                      # .ppsm \
    "application/vnd.ms-powerpoint.template.macroEnabled.12",                       # .potm \
    "application/vnd.ms-word",          # .doc                      \
    "application/vnd.ms-word.document.macroEnabled.12",                             # .docm \
    "application/vnd.ms-word.template.macroEnabled.12",                             # .dotm \
    "application/vnd.msexcel",          # .xls                      \
    "application/vnd.mspowerpoint",     # .ppt                      \
    "application/vnd.msword",           # .doc                      \
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",    # .pptx \
    "application/vnd.openxmlformats-officedocument.presentationml.template",        # .potx \
    "application/vnd.openxmlformats-officedocument.presentationml.slideshow",       # .ppsx \
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",            # .xlsx \
    "application/vnd.openxmlformats-officedocument.spreadsheetml.template",         # .xltx \
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",      # .docx \
    "application/vnd.openxmlformats-officedocument.wordprocessingml.template",      # .dotx \
    "application/vnd.pdf",              # .pdf                      \
    "application/vnd-mspowerpoint",     # .ppt                      \
    "application/winword",              # .doc                      \
    "application/word",                 # .doc                      \
    "application/x-acad",               # .dwg                      \
    "application/x-apple-diskimage",    # .dmg                      \
    "application/x-autocad",            # .dwg                      \
    "application/x-bibtex",             # .bib                      \
    "application/x-compress",           # .gz, .tar, .zip           \
    "application/x-compressed",         # .gz, .tar, .zip           \
    "application/x-dos_ms_excel",       # .xls                      \
    "application/x-dwg",                # .dwg                      \
    "application/x-endnote-refer",      # .enw                      \
    "application/x-eps",                # .eps                      \
    "application/x-excel",              # .xls                      \
    "application/x-gtar",               # .tar                      \
    "application/x-gunzip",             # .gz                       \
    "application/x-gzip",               # .gz                       \
    "application/x-jpg",                # .jpg                      \
    "application/x-m",                  # .ppt                      \
    "application/x-ms-excel",           # .xls                      \
    "application/x-msexcel",            # .xls                      \
    "application/x-mspublisher",        # .pub                      \
    "application/x-msw6",               # .doc                      \
    "application/x-msword",             # .doc                      \
    "application/x-ole-storage",        # .msi                      \
    "application/x-pdf",                # .pdf                      \
    "application/x-powerpoint",         # .ppt                      \
    "application/x-rtf",                # .rtf                      \
    "application/x-shockwave-flash",    # .swf                      \
    "application/x-shockwave-flash2-preview",   # .swf              \
    "application/x-tar",                # .tar                      \
    "application/x-troff-msvideo",      # .avi                      \
    "application/x-soffice",            # .rtf                      \
    "application/x-xml",                # .xml, .pub                \
    "application/x-zip",                # .zip                      \
    "application/x-zip-compressed",     # .zip                      \
    "application/xls",                  # .xls                      \
    "application/xml",                  # .xml, .pub                \
    "application/zip",                  # .zip                      \
    "audio/aiff",                       # .avi, .mov                \
    "audio/avi",                        # .avi                      \
    "audio/mp3",                        # .mp3                      \
    "audio/mp4",                        # .mp4                      \
    "audio/mpg",                        # .mp3                      \
    "audio/mpeg",                       # .mp3                      \
    "audio/mpeg3",                      # .mp3                      \
    "audio/x-midi",                     # .mov                      \
    "audio/x-mp3",                      # .mp3                      \
    "audio/x-mpg",                      # .mp3                      \
    "audio/x-mpeg",                     # .mp3                      \
    "audio/x-mpeg3",                    # .mp3                      \
    "audio/x-mpegaudio",                # .mp3                      \
    "audio/x-wav",                      # .mov                      \
    "drawing/dwg",                      # .dwg                      \
    "gzip/document",                    # .gz                       \
    "image/avi",                        # .avi                      \
    "image/eps",                        # .eps                      \
    "image/gi_",                        # .gif                      \
    "image/gif",                        # .eps, .gif                \
    "image/jpeg",                       # .jpg, .jpeg               \
    "image/jpg",                        # .jpg                      \
    "image/jp_",                        # .jpg                      \
    "image/mpeg",                       # .mpeg                     \
    "image/mov",                        # .mov                      \
    "image/photoshop",                  # .psd                      \
    "image/pipeg",                      # .jpg                      \
    "image/pjpeg",                      # .jpg                      \
    "image/png",                        # .png                      \
    "image/psd",                        # .psd                      \
    "image/vnd.dwg",                    # .dwg                      \
    "image/vnd.rn-realflash",           # .swf                      \
    "image/vnd.swiftview-jpeg",         # .jpg                      \
    "image/x-eps",                      # .eps                      \
    "image/x-dwg",                      # .dwg                      \
    "image/x-photoshop",                # .psd                      \
    "image/x-xbitmap",                  # .gif, .jpg                \
    "multipart/x-tar",                  # .tar                      \
    "multipart/x-zip",                  # .zip                      \
    "octet-stream",                     # possibly some .ppt files  \
    "text/csv",                         # .csv                      \
    "text/mspg-legacyinfo",             # .msi                      \
    "text/pdf",                         # .pdf                      \
    "text/richtext",                    # .rtf                      \
    "text/rtf",                         # .rtf                      \
    "text/x-pdf",                       # .pdf                      \
    "text/xml",                         # .xml, .rss                \
    "video/avi",                        # .avi, .mov                \
    "video/mp4v-es",                    # .mp4                      \
    "video/msvideo",                    # .avi                      \
    "video/quicktime",                  # .mov                      \
    "video/x-flv",                      # .flv                      \
    "video/x-m4v",                      # .m4v                      \
    "video/x-msvideo",                  # .avi                      \
    "video/x-quicktime",                # .mov                      \
    "video/xmpg2",                      # .avi                      \
    "zz-application/zz-winassoc-psd",   # .psd                      \
]


class Browser(object):
    """hubcheck webdriver interface"""

    def __init__(self, mimetypes=[], downloaddir='/tmp'):

        self.logger = logging.getLogger(__name__)
        self.logger.info("setting up a web browser")

        self._browser = None
        self.wait_time = 2
        self.marker = 0
        self.proxy_client = None
        self.proxy_blacklist = PROXY_BLACKLIST
        self.profile = None
        self.downloaddir = downloaddir
        self.mimetypes = mimetypes


    def __del__(self):

        self.close()


    def setup_browser_preferences(self):
        """browser preferences should be setup by subclasses
        """

        pass


    def start_proxy_client(self):

        # setup proxy if needed

        if hubcheck.conf.settings.proxy is None:
            self.logger.info("proxy not started, not starting client")
            return

        # start the client
        self.proxy_client = hubcheck.conf.settings.proxy.create_client()

        # setup the proxy website blacklist
        if self.proxy_client is not None:
            self.logger.info("setting up proxy blacklist")
            for url_re in self.proxy_blacklist:
                self.logger.debug("blacklisting %s" % url_re)
                self.proxy_client.blacklist(url_re,200)


    def stop_proxy_client(self):

        if self.proxy_client is not None:
            self.logger.info("stopping proxy client")
            self.proxy_client.close()
            self.proxy_client = None


    def setup_browser_size_and_position(self):

        # set the amount of time to wait for an element to appear on the page
        self._browser.implicitly_wait(self.wait_time)

        # place the browser window in the upper left corner of the screen
        self._browser.set_window_position(0, 0)

        # resize the window to just shy of our 1024x768 screen
        self._browser.set_window_size(1070,700)


    def launch(self):
        """subclass should add code required to launch the browser
        """

        pass


    def get(self,url):

        if self._browser is None:
            self.launch()

        self.logger.debug("retrieving url: %s" % (url))
        self._browser.get(url)


    def close(self):

        if self._browser is None:
            return

        self.logger.info("closing browser")
        self._browser.quit()
        self._browser = None
        self.profile

        self.stop_proxy_client()


    def error_loading_page(self,har_entry):
        """
        check if there was an error loading the web page
        returns True or False
        """

        harurl = har_entry['request']['url']
        harstatus = har_entry['response']['status']

        self.logger.debug("%s returned status %s" % (harurl,harstatus))

        result = None

        if (harstatus >= 100) and (harstatus <= 199):
            # information codes
            result = False
        elif (harstatus >= 200) and (harstatus <= 299):
            # success codes
            result = False
        elif (harstatus >= 300) and (harstatus <= 399):
            # redirect codes
            result = False
        elif (harstatus >= 400) and (harstatus <= 499):
            # client error codes
            # client made an invalid request (bad links)
            # page does not exist
            result = True
        elif (harstatus >= 500) and (harstatus <= 599):
            # server error codes
            # client made a valid request,
            # but server failed while responsing.
            result = True
        else:
            result = True

        return result


    def page_load_details(self,url=None,follow_redirects=True):
        """
        return the har entry for the last page loaded
        follow redirects to make sure you get the har entry
        for the page that was eventually loaded.

        A return value of None means no page was ever loaded.
        """

        if not self.proxy_client:
            return None

        if url is None:
            url = self._browser.current_url

        self.logger.debug("processing har for %s" % (url))

        har = self.proxy_client.har

        self.logger.debug("har entry = %s" % (pprint.pformat(har)))

        return_entry = None

        for entry in har['log']['entries']:
            harurl = entry['request']['url']
            harstatus = entry['response']['status']

            if url == None:
                # we are following a redirect from below
                return_entry = entry
            elif url == harurl:
                # the original url matches the url for this har entry exactly
                return_entry = entry
            elif (not url.endswith('/')) and (url+'/' == harurl):
                # the original url almost matches the url for this har entry
                return_entry = entry

            if return_entry is not None:
                if follow_redirects and (harstatus >= 300) and (harstatus <= 399):
                    # follow the redirect (should be the next har entry)
                    url = None
                    continue
                else:
                    # found our match
                    break


        self.logger.debug("har for url = %s" % (pprint.pformat(return_entry)))

        return return_entry


    def take_screenshot(self,filename=None):
        """
        Take a screen shot of the browser, store it in filename.
        """

        if self._browser is None:
            return

        if filename is None:
            dts = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
            filename = 'hcss_%s.png' % dts

        self.logger.debug("screenshot filename: %s" % (filename))

        self._browser.save_screenshot(filename)


    def next_marker(self):

        self.marker += 1
        return self.marker


