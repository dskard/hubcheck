import argparse
import copy
import easyprocess
import getpass
import glob
import hubcheck.browser
import hubcheck.conf
import hubcheck.utils
import logging
import logging.config
import os
import pprint
import pyvirtualdisplay
import signal
import subprocess
import sys
import datetime

class Tool(object):

    def __init__(self,logfile='hcutils.log',loglevel='INFO'):

        self.options = None
        self.logger = None
        self.testdata = None
        self.__recording = None
        self.__display = None
        self.__windowmanager = None
        self.__vncviewer = None
        self.__proxy = None


        usage = "usage: %prog [options]"
        usage = None
        self.command_parser = argparse.ArgumentParser(usage=usage)

        self.command_parser.add_argument(
            '--testdata',
            help='testdata file with account information',
            action="store",
            dest="tdfname",
            default=None,
            type=str)

        self.command_parser.add_argument(
            '--config',
            help='configuration file with option overrides',
            action="store",
            dest="config",
            default='',
            type=str)

        self.command_parser.add_argument(
            '--logfile',
            help='log filename',
            action="store",
            dest="logfile",
            default=None,
            type=str)

        self.command_parser.add_argument(
            '--loglevel',
            help='log level',
            action="store",
            dest="loglevel",
            default=None,
            type=str)

        self.command_parser.add_argument(
            '--log-locator-updates',
            help='show page object locator updates in DEBUG level log messages',
            action="store_true",
            dest="log_locator_updates",
            default=None)

        self.command_parser.add_argument(
            '--log-widget-attachments',
            help='show page object widgets attaching and detaching from their owners in DEBUG level log messages',
            action="store_true",
            dest="log_widget_attachments",
            default=None)

        self.command_parser.add_argument(
            '--browsermobproxy-port',
            help='port to run browsermobproxy on',
            action="store",
            dest="bmp_port",
            default=None,
            type=int)

        self.command_parser.add_argument(
            '--no-xvfb',
            help='run tests outside of xvfb display',
            action="store_true",
            dest="no_xvfb",
            default=False)

        self.command_parser.add_argument(
            '--show-xvfb',
            help='show tests running in xvfb display',
            action="store_true",
            dest="show_xvfb",
            default=False)

        self.command_parser.add_argument(
            '--record-xvfb',
            help='record the xvfb display',
            action="store_true",
            dest="record_xvfb",
            default=False)

        self.command_parser.add_argument(
            '--highlight-web-elements',
            help='highlight web elements as they are interacted with (slow)',
            action="store_true",
            dest="highlight_web_elements",
            default=False)

        self.command_parser.add_argument(
            '--scroll-to-web-elements',
            help='scroll browser to web elements that are searched for (slow)',
            action="store_true",
            dest="scroll_to_web_elements",
            default=False)

        self.command_parser.add_argument(
            '--screenshotdir',
            help='directory to store screenshots',
            action="store",
            dest="screenshotdir",
            default=None,
            type=str)

        self.command_parser.add_argument(
            '--videodir',
            help='directory to store videos',
            action="store",
            dest="videodir",
            default=None,
            type=str)

        # self.command_parser.add_argument('remainder', nargs=argparse.REMAINDER)


        self.config_parser = hubcheck.conf.ConfigurationParser()


        self.config_parser.add_option(
            'tdfname',
            help='testdata file with account information',
            action="get",
            path=['testdata','file'],
            default="hub.info",
            type=str)

        self.config_parser.add_option(
            'tdfkey',
            help='testdata file key',
            action="get",
            path=['testdata','key'],
            default=None,
            type=str)

        self.config_parser.add_option(
            'logfile',
            help='log filename',
            action="get",
            path=['logging','logfile'],
            default=logfile,
            type=str)

        self.config_parser.add_option(
            'loglevel',
            help='log level',
            action="get",
            path=['logging','loglevel'],
            default=loglevel,
            type=str)

        self.config_parser.add_option(
            'log_locator_updates',
            help='show page object locator updates in DEBUG level log messages',
            action="get",
            path=['logging','log_locator_updates'],
            default=False,
            type=str)

        self.config_parser.add_option(
            'log_widget_attachments',
            help='show page object widgets attaching and detaching from their owners in DEBUG level log messages',
            action="get",
            path=['logging','log_widget_attachments'],
            default=False,
            type=str)

        self.config_parser.add_option(
            'bmp_port',
            help='port to run browsermobproxy on',
            action="get",
            path=['proxy','port'],
            default=9095,
            type=int)

        self.config_parser.add_option(
            'resultsfile',
            help='results filename',
            action="get",
            path=['logging','resultsfile'],
            default=None,
            type=str)

        self.config_parser.add_option(
            'verbosity',
            help='results detail level',
            action="get",
            path=['logging','verbosity'],
            default=2,
            type=int)

        self.config_parser.add_option(
            'email_smtp',
            help='address of the smtp server sending email reports',
            action="get",
            path=['email','smtp'],
            default='localhost',
            type=str)

        self.config_parser.add_option(
            'email_from',
            help='email address of user sending email reports',
            action="get",
            path=['email','from'],
            default=None,
            type=str)

        self.config_parser.add_option(
            'email_to',
            help='email address of user receiving email reports',
            action="options",
            path=['email_addresses'],
            default=[],
            type=list)

        self.config_parser.add_option(
            'email_subject',
            help='email report subject',
            action="get",
            path=['email','subject'],
            default='hubcheck error report',
            type=str)

        self.config_parser.add_option(
            'screenshotdir',
            help='directory to hold screenshots of errors',
            action="get",
            path=['logging','screenshotdir'],
            default=None,
            type=str)

        self.config_parser.add_option(
            'videodir',
            help='directory to hold video of running tests',
            action="get",
            path=['logging','videodir'],
            default=None,
            type=str)


    def parse_options(self):

        # parse command line options
        # cl_options = self.command_parser.parse_args()
        cl_options, cl_unknown = self.command_parser.parse_known_args()

        # parse config options
        configpath = os.path.expanduser(os.path.expandvars(cl_options.config))
        hubcheck.conf.settings.configpath = configpath
        self.config_parser.set_path(configpath)
        cf_options = self.config_parser.parse_config()

        # use the config file options as a base
        # use command line options as overrides
        self.options = self.resolve_options(cf_options,cl_options)
        self.options.__dict__['remainder'] = cl_unknown


    def resolve_options(self,base,overrides):

        if base is None and overrides is None:
            return None

        if (base is None) and (overrides is not None):
            return overrides

        if (base is not None) and (overrides is None):
            return base

        for key,value in overrides.__dict__.items():
            # if the override doesn't exist in base,
            # set it to the default value
            if key not in base.__dict__:
                base.__dict__[key] = value

            # check if we need to override the value from base
            if value is not None:
                # overrides[key] is not None, set the override
                base.__dict__[key] = value
                #self.logger.debug('option override: %s = %s',key,value)

        return base


    def start_logging(self,create_logger=True):

        if create_logger is True:
            # setup a log file
            self.options.logfile = os.path.abspath(
                                    os.path.expanduser(
                                        os.path.expandvars(
                                            self.options.logfile)))

            dc = hubcheck.utils.create_dictConfig(
                    self.options.logfile,self.options.loglevel)

            logging.config.dictConfig(dc)


        self.logger = logging.getLogger(__name__)

        self.logger.info("starting %s" % sys.argv[0])
        self.logger.info("command line options: %s" % sys.argv[1:])

        # print out the parsed options
        tmp_options = copy.deepcopy(self.options)
        tmp_options.tdfkey = "HIDDEN"
        self.logger.debug("parsed options = %s" %
            pprint.pformat(tmp_options.__dict__))


    def cleanup_temporary_files(self):

        hubcheck.utils.cleanup_temporary_files()


    def start_recording_xvfb(self,filename):

        self.__recording = None
        if hubcheck.conf.settings.video_dir is not None:
            videodir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.video_dir)))
            videofn = os.path.join(videodir,filename)
            self.__recording = hubcheck.utils.WebRecordXvfb(videofn)
            self.__recording.start()


    def stop_recording_xvfb(self):

        if self.__recording is not None:
            self.__recording.stop()


    def screenshot_filepath(self,fnamebase="hcss"):

        if hubcheck.conf.settings.screenshot_dir is not None:
            basepath = hubcheck.conf.settings.screenshot_dir
        else:
            basepath = ""

        dts = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        filepath = os.path.join(basepath, fnamebase + '_%s.png' % (dts))

        return filepath


    def __setup_run(self):

        # FIXME:
        # check if logger has been started, and options have been parsed

        # set flag for highlighting web elements
        hubcheck.conf.settings.highlight_web_elements = \
            self.options.highlight_web_elements

        # set flag for highlighting web elements
        hubcheck.conf.settings.scroll_to_web_elements = \
            self.options.scroll_to_web_elements

        # set flags for logging
        hubcheck.conf.settings.log_locator_updates = \
            self.options.log_locator_updates
        hubcheck.conf.settings.log_widget_attachments = \
            self.options.log_widget_attachments

        # get account and hub data
        hubcheck.conf.settings.tdfname = os.path.abspath(
                                    os.path.expanduser(
                                        os.path.expandvars(
                                            self.options.tdfname)))

        self.logger.debug("hubcheck.conf.settings.tdfname = %s"
                            % hubcheck.conf.settings.tdfname)

        # check if the testdata file exists
        if os.path.exists(hubcheck.conf.settings.tdfname) is False:
            raise ValueError('Testdata file does not exist: %s' \
                                % (hubcheck.conf.settings.tdfname))

        if getattr(self.options,'tdfkey',None) is None:
            # testdata key was not provided, prompt user for it
            self.logger.info("requesting testdata key from user")
            if sys.stdin.isatty():
                hubcheck.conf.settings.tdpass = getpass.getpass('testdata password: ')
            else:
                sys.stdout.write('testdata password: ')
                hubcheck.conf.settings.tdpass = sys.stdin.readline().rstrip()
        else:
            hubcheck.conf.settings.tdpass = self.options.tdfkey


        # set up screenshot directory
        self.logger.info("setting up hubcheck.conf.settings.screenshot_dir")
        if self.options.screenshotdir is not None:
            self.options.screenshotdir = os.path.abspath(
                                            os.path.expanduser(
                                                os.path.expandvars(
                                                    self.options.screenshotdir)))
            if not os.path.isdir(self.options.screenshotdir):
                if os.path.isfile(self.options.screenshotdir):
                    # remove files in the way
                    os.remove(self.options.screenshotdir)
                os.makedirs(self.options.screenshotdir,0700)
        hubcheck.conf.settings.screenshot_dir = self.options.screenshotdir


        # set up video recording directory
        self.logger.info("setting up hubcheck.conf.settings.video_dir")
        if self.options.videodir is not None:
            self.options.videodir = os.path.abspath(
                                            os.path.expanduser(
                                                os.path.expandvars(
                                                    self.options.videodir)))
            if not os.path.isdir(self.options.videodir):
                if os.path.isfile(self.options.videodir):
                    # remove files in the way
                    os.remove(self.options.videodir)
                os.makedirs(self.options.videodir,0700)
        hubcheck.conf.settings.video_dir = self.options.videodir


        # load the testdata file
        self.logger.info("loading the testdata file")
        self.testdata = hubcheck.conf.Testdata().load(
                            hubcheck.conf.settings.tdfname,
                            self.options.tdfkey)


        # setup hub config variables from testdata file

        # setup the hub hostname info
        hubcheck.conf.settings.hub_hostname = self.testdata.find_url_for('https')

        # setup the hub version info
        hubcheck.conf.settings.hub_version = self.testdata.get_hub_version()

        # setup the hub tool container version info
        hubcheck.conf.settings.tool_container_version = \
            self.testdata.get_tool_container_version()

        # setup the hub's default workspace toolname
        hubcheck.conf.settings.default_workspace_toolname = \
            self.testdata.get_default_workspace()

        # setup the hub's apps workspace toolname
        hubcheck.conf.settings.apps_workspace_toolname = \
            self.testdata.get_apps_workspace()


        # start a virtual display
        self.__display = None
        self.__windowmanager = None
        self.__vncviewer = None

        disp_env = os.environ.get('DISPLAY',None)
        disp_width = 1080
        disp_height = 768

        if self.options.no_xvfb is False:
            self.logger.info("starting the virtual display")
            self.logger.debug("old DISPLAY: %s" %  disp_env)
            self.__display = pyvirtualdisplay.Display(visible=0,
                        size=(disp_width,disp_height))
            self.__display.start()
            self.logger.debug("new DISPLAY: %s" %  os.environ['DISPLAY'])

            # try to start a window manager so things look pretty
            # in the videos and screenshots
            icewm_path = hubcheck.utils.which('icewm')
            if icewm_path is not None:
                self.logger.info("starting a window manager")
                self.__windowmanager = easyprocess.EasyProcess(icewm_path).start()
            else:
                self.logger.info("no window manager found")

            # check if we should show the xvfb display to the user
            # we can only show the display if the user has a DISPLAY
            if self.options.show_xvfb is True and disp_env is not None:
                self.logger.info("starting a vncserver to show our xvfb session")

                self.__vncviewer = hubcheck.utils.XvfbView(
                                os.environ['DISPLAY'],disp_env)
                self.__vncviewer.start()

        else:
            # we are not starting an xvfb display
            #
            # disable recording the display because
            # when we record in the workspace, ffmpeg segfaults
            # it probably can't connect to the display or something
            # not sure of another way to signal we are in a workspace.
            self.options.record_xvfb = False


        # check if we should record the xvfb sessions
        if self.options.record_xvfb is False:
            hubcheck.conf.settings.video_dir = None


        # configure the web proxy
        self.__proxy = hubcheck.browser.Proxy(port=self.options.bmp_port)
        self.__proxy.start()


    def __teardown_run(self):

        # stop the web proxy
        if self.__proxy is not None:
            self.__proxy.stop()

        # shutdown the xvfb view
        if self.__vncviewer is not None:
            try:
                self.__vncviewer.stop()
            except Exception as e:
                self.logger.exception(e)
            self.__vncviewer = None

        # shutdown the window manager
        if self.__windowmanager is not None:
            self.logger.info("stopping the virtual display window manager")
            try:
                self.__windowmanager.stop()
            except Exception as e:
                self.logger.exception(e)
            self.__windowmanager = None

        # shutdown the virtual display
        if self.__display is not None:
            self.logger.info("stopping the virtual display")
            try:
                self.__display.stop()
            except Exception as e:
                self.logger.exception(e)
            self.__display = None

        # remove temp files
        self.cleanup_temporary_files()


    def run(self):

        try:
            self.__setup_run()
            self.command()
        except Exception as e:
            self.logger.exception(e)
            raise
        finally:
            self.__teardown_run()


