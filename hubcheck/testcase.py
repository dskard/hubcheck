import hubcheck
import logging
import unittest
from unittest.case import *
# importing * does not import protected classes
from unittest.case import _ExpectedFailure as _ExpectedFailure
from unittest.case import _UnexpectedSuccess as _UnexpectedSuccess
from unittest.case import _AssertRaisesContext as _AssertRaisesContext
import os
import sys
import traceback

# testcase metaclass idea from http://stackoverflow.com/a/15969985

MARKER = "="*5

class TestCaseMetaClass(type):

    def __new__(cls,name,bases,dct):

        def wrappedSetUp(self):

            self.datadir = hubcheck.conf.settings.data_dir
            self.browser = None

            # setup screenshot file name
            if hubcheck.conf.settings.screenshot_dir is not None:
                ssdir = os.path.abspath(
                            os.path.expanduser(
                                os.path.expandvars(
                                    hubcheck.conf.settings.screenshot_dir)))

                self.screenshotfn = os.path.join(ssdir,"%s.png" % (self.id()))
            else:
                self.screenshotfn = None

            # start recording video if enabled
            self._start_test_case_recording()

            # setup testdata
            self.logger.debug('wrappedSetUp hubcheck.conf.settings.tdfname = %s' \
                % hubcheck.conf.settings.tdfname)

            self.testdata = hubcheck.conf.Testdata().load(
                                hubcheck.conf.settings.tdfname,
                                hubcheck.conf.settings.tdpass )
            self.locators = self.testdata.get_locators()

            self.logger.debug('wrappedSetUp locators = %s' % self.locators)
            self.logger.debug('wrappedSetUp hubcheck.conf.settings.proxy = %s' \
                % hubcheck.conf.settings.proxy)

            # setup the https authority
            https_uri = self.testdata.find_url_for('https')
            https_port = self.testdata.find_url_for('httpsport')

            if https_port == 443:
                self.https_authority = "https://%s" % (https_uri)
            else:
                self.https_authority = "https://%s:%s" % (https_uri,https_port)

            # setup the http authority
            http_uri = self.testdata.find_url_for('http')
            http_port = self.testdata.find_url_for('httpport')

            if http_port == 80:
                self.http_authority = "http://%s" % (http_uri)
            else:
                self.http_authority = "http://%s:%s" % (http_uri,http_port)
            try:
                # setup the browser
                self._start_test_case_browser()

                self.catalog = hubcheck.pageobjects.PageObjectCatalog(
                    self.locators, self.browser)
                self.utils = hubcheck.actionobjects.HubzeroActions(
                    https_uri,self.browser,self.catalog)

                # call the user's setup function
                setUp(self)

            except Exception as e:

                exc_info = sys.exc_info()

                # try to get a screenshot to help with debugging
                if self.screenshotfn is not None:
                    if hasattr(self,'browser') and self.browser is not None:
                        try:
                            self.browser.take_screenshot(self.screenshotfn)
                        except Exception:
                            self.logger.debug('Exception ignored: %s %s'
                                % (sys.exc_info()[1],sys.exc_info()[2]))

                # close the browser
                self._stop_test_case_browser()

                # stop xvfb recording
                self._stop_test_case_recording()

                raise exc_info[1], None, exc_info[2]


        def wrappedTearDown(self):

            try:
                tearDown(self)

            finally:
                # close the browser
                self._stop_test_case_browser()

                # stop xvfb recording
                self._stop_test_case_recording()

        # if the TestCase already provides setUp, wrap it
        if 'setUp' in dct:
            setUp = dct['setUp']
        else:
            setUp = lambda self: None

        dct['setUp'] = wrappedSetUp

        # if the TestCase already provides tearDown, wrap it
        if 'tearDown' in dct:
            tearDown = dct['tearDown']
        else:
            tearDown = lambda self: None

        dct['tearDown'] = wrappedTearDown

        # return the class instance with the replaced setUp/tearDown
        return type.__new__(cls, name, bases, dct)


class TestCaseMetaClass2(type):

    def __new__(cls,name,bases,dct):

        def wrapped_setup_method(self,method,*args,**kwargs):

            self.fnbase = "%s.%s" % (type(self).__name__, method.__name__)
            self.datadir = hubcheck.conf.settings.data_dir
            self.browser = None

            # add start marker to the log
            self.logger.info("%s TestCase Start: %s" % (MARKER,self.fnbase))

            # setup screenshot file name
            self._setup_test_case_screenshot()

            # start recording video if enabled
            self._start_test_case_recording()

            # setup testdata, locators, and urls
            self._setup_test_case_testdata()

            # setup the browser
            self._start_test_case_browser()

            try:

                # call the user's setup function
                user_setup_method(self,method,*args,**kwargs)

            except Exception as e:

                exc_info = sys.exc_info()

                # try to get a screenshot to help with debugging
                if self.screenshotfn is not None:
                    if hasattr(self,'browser') and self.browser is not None:
                        try:
                            self.browser.take_screenshot(self.screenshotfn)
                        except Exception:
                            self.logger.debug('Exception ignored: %s %s'
                                % (sys.exc_info()[1],sys.exc_info()[2]))

                # close the browser
                self._stop_test_case_browser()

                # stop xvfb recording
                self._stop_test_case_recording()

                # add end test marker to the log file
                self.logger.info("%s TestCase End: %s" % (MARKER,self.fnbase))

                raise exc_info[1], None, exc_info[2]


        def wrapped_teardown_method(self,method,*args,**kwargs):

            try:
                user_teardown_method(self,method,*args,**kwargs)

            finally:
                # close the browser
                self._stop_test_case_browser()

                # stop xvfb recording
                self._stop_test_case_recording()

                # add end test marker to the log file
                self.logger.info("%s TestCase End: %s" % (MARKER,self.fnbase))


        # if the TestCase already provides setUp, wrap it
        if 'setup_method' in dct:
            user_setup_method = dct['setup_method']
        else:
            user_setup_method = lambda self,method: None

        dct['setup_method'] = wrapped_setup_method

        # if the TestCase already provides tearDown, wrap it
        if 'teardown_method' in dct:
            user_teardown_method = dct['teardown_method']
        else:
            user_teardown_method = lambda self,method: None

        dct['teardown_method'] = wrapped_teardown_method

        # return the class instance with the replaced setUp/tearDown
        return type.__new__(cls, name, bases, dct)


class TestCase(unittest.TestCase):
    __metaclass__ = TestCaseMetaClass
    logger = logging.getLogger()

    def _start_test_case_browser(self):
        self.browser = hubcheck.browser.Firefox()


    def _stop_test_case_browser(self):
        if self.browser is not None:
            try:
                self.browser.close()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))


    def _start_test_case_recording(self):
        self.recording = None
        if hubcheck.conf.settings.video_dir is not None:
            videodir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.video_dir)))
            # self.videofn = os.path.join(videodir,"%s.avi" % (self.id()))
            self.videofn = os.path.join(videodir,"%s.mp4" % (self.id()))
            self.recording = hubcheck.utils.WebRecordXvfb(self.videofn)
            self.recording.start()


    def _stop_test_case_recording(self):
        if self.recording is not None:
            try:
                self.recording.stop()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))


    # copy of unittest.case.py's run function
    # with some local modifications for screenshots
    # as self.browser.take_screenshot()

    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        self._resultForDoCleanups = result
        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, skip_why)
            finally:
                result.stopTest(self)
            return

        self.logger.info("%s TestCase Start: %s" % (MARKER,self.id()))

        try:
            success = False
            try:
                self.setUp()
            except SkipTest as e:
                self._addSkip(result, str(e))
            except KeyboardInterrupt:
                raise
            except:
                self.logger.debug('run() caught exception in setUp():\n%s' % traceback.format_exc())
                result.addError(self, sys.exc_info())
            else:
                try:
                    testMethod()
                except KeyboardInterrupt:
                    raise
                except self.failureException:
                    self.logger.debug('run() caught failure in testMethod():\n%s' % traceback.format_exc())
                    result.addFailure(self, sys.exc_info())
                    if self.screenshotfn is not None:
                        try:
                            self.browser.take_screenshot(self.screenshotfn)
                        except Exception:
                            pass
                except _ExpectedFailure as e:
                    addExpectedFailure = getattr(result, 'addExpectedFailure', None)
                    if addExpectedFailure is not None:
                        addExpectedFailure(self, e.exc_info)
                    else:
                        warnings.warn("TestResult has no addExpectedFailure method, reporting as passes",
                                      RuntimeWarning)
                        result.addSuccess(self)
                except _UnexpectedSuccess:
                    addUnexpectedSuccess = getattr(result, 'addUnexpectedSuccess', None)
                    if addUnexpectedSuccess is not None:
                        addUnexpectedSuccess(self)
                    else:
                        warnings.warn("TestResult has no addUnexpectedSuccess method, reporting as failures",
                                      RuntimeWarning)
                        self.logger.debug('run() caught failure in testMethod():\n%s' % traceback.format_exc())
                        result.addFailure(self, sys.exc_info())
                except SkipTest as e:
                    self._addSkip(result, str(e))
                except:
                    self.logger.debug('run() caught exception in testMethod():\n%s' % traceback.format_exc())
                    result.addError(self, sys.exc_info())
                    if self.screenshotfn is not None:
                        try:
                            self.browser.take_screenshot(self.screenshotfn)
                        except Exception:
                            pass
                else:
                    success = True

                try:
                    self.tearDown()
                except KeyboardInterrupt:
                    raise
                except:
                    self.logger.debug('run() caught exception in tearDown():\n%s' % traceback.format_exc())
                    result.addError(self, sys.exc_info())
                    success = False

            cleanUpSuccess = self.doCleanups()
            success = success and cleanUpSuccess
            if success:
                result.addSuccess(self)
        finally:
            self.logger.info("%s TestCase End: %s" % (MARKER,self.id()))
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()


class TestCase2(object):
    __metaclass__ = TestCaseMetaClass2
    logger = logging.getLogger()

    def _start_test_case_browser(self):
        self.browser = hubcheck.browser.Firefox()

        self.catalog = hubcheck.pageobjects.PageObjectCatalog(
            self.locators,self.browser)
        self.utils = hubcheck.actionobjects.HubzeroActions(
            self.https_uri,self.browser,self.catalog)


    def _stop_test_case_browser(self):
        if self.browser is not None:
            try:
                self.browser.close()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))


    def _setup_test_case_screenshot(self):
        if hubcheck.conf.settings.screenshot_dir is not None:
            ssdir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.screenshot_dir)))

            self.screenshotfn = os.path.join(ssdir,"%s.png" % (self.fnbase))
        else:
            self.screenshotfn = None


    def _setup_test_case_testdata(self):
        self.logger.debug('wrappedSetUp hubcheck.conf.settings.tdfname = %s' \
            % hubcheck.conf.settings.tdfname)

        self.testdata = hubcheck.conf.Testdata().load(
                            hubcheck.conf.settings.tdfname,
                            hubcheck.conf.settings.tdpass )
        self.locators = self.testdata.get_locators()

        self.logger.debug('wrappedSetUp locators = %s' % self.locators)
        self.logger.debug('wrappedSetUp hubcheck.conf.settings.proxy = %s' \
            % hubcheck.conf.settings.proxy)

        # setup the https authority
        self.https_uri = self.testdata.find_url_for('https')
        https_port = self.testdata.find_url_for('httpsport')

        if https_port == 443:
            self.https_authority = "https://%s" % (self.https_uri)
        else:
            self.https_authority = "https://%s:%s" % (self.https_uri,https_port)

        # setup the http authority
        self.http_uri = self.testdata.find_url_for('http')
        http_port = self.testdata.find_url_for('httpport')

        if http_port == 80:
            self.http_authority = "http://%s" % (self.http_uri)
        else:
            self.http_authority = "http://%s:%s" % (self.http_uri,http_port)


    def _start_test_case_recording(self):
        self.recording = None
        if hubcheck.conf.settings.video_dir is not None:
            videodir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.video_dir)))
            self.videofn = os.path.join(videodir,"%s.mp4" % (self.fnbase))
            self.recording = hubcheck.utils.WebRecordXvfb(self.videofn)
            self.recording.start()


    def _stop_test_case_recording(self):
        if self.recording is not None:
            try:
                self.recording.stop()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))


class TestCase3(object):

    # see
    # http://pytest.org/dev/example/simple.html#making-test-result-information-available-in-fixtures
    # to help figure out how to identify when a test failed
    # so we can add screenshots of the browser.

    def __init__(self,method):

        self.logger = logging.getLogger()
        self.id = lambda : "%s.%s" % (type(self).__name__, method.__name__)
        self.datadir = hubcheck.conf.settings.data_dir
        self.browser = None

        # add start marker to the log
        self.logger.info("%s TestCase Start: %s" % (MARKER,self.id()))

        # setup screenshot file name
        if hubcheck.conf.settings.screenshot_dir is not None:
            ssdir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.screenshot_dir)))

            self.screenshotfn = os.path.join(ssdir,"%s.png" % (self.id()))
        else:
            self.screenshotfn = None

        # start recording video if enabled
        self._start_test_case_recording()

        # setup testdata
        self.logger.debug('wrappedSetUp hubcheck.conf.settings.tdfname = %s' \
            % hubcheck.conf.settings.tdfname)

        self.testdata = hubcheck.conf.Testdata().load(
                            hubcheck.conf.settings.tdfname,
                            hubcheck.conf.settings.tdpass )
        self.locators = self.testdata.get_locators()

        self.logger.debug('wrappedSetUp locators = %s' % self.locators)
        self.logger.debug('wrappedSetUp hubcheck.conf.settings = %s' \
            % hubcheck.conf.settings)

        # setup the https authority
        https_uri = self.testdata.find_url_for('https')
        https_port = self.testdata.find_url_for('httpsport')

        if https_port == 443:
            self.https_authority = "https://%s" % (https_uri)
        else:
            self.https_authority = "https://%s:%s" % (https_uri,https_port)

        # setup the http authority
        http_uri = self.testdata.find_url_for('http')
        http_port = self.testdata.find_url_for('httpport')

        if http_port == 80:
            self.http_authority = "http://%s" % (http_uri)
        else:
            self.http_authority = "http://%s:%s" % (http_uri,http_port)
        try:
            # setup the browser
            self._start_test_case_browser()

            self.catalog = hubcheck.pageobjects.PageObjectCatalog(
                self.locators, self.browser)
            self.utils = hubcheck.actionobjects.HubzeroActions(
                https_uri,self.browser,self.catalog)

        except Exception as e:

            exc_info = sys.exc_info()

            # try to get a screenshot to help with debugging
            if self.screenshotfn is not None:
                if hasattr(self,'browser') and self.browser is not None:
                    try:
                        self.browser.take_screenshot(self.screenshotfn)
                    except Exception:
                        self.logger.debug('Exception ignored: %s %s'
                            % (sys.exc_info()[1],sys.exc_info()[2]))

            self.teardown()

            raise exc_info[1], None, exc_info[2]


    def teardown(self):

        # close the browser
        self._stop_test_case_browser()

        # stop xvfb recording
        self._stop_test_case_recording()

        # add end test marker to the log file
        self.logger.info("%s TestCase End: %s" % (MARKER,self.id()))


    def _start_test_case_browser(self):
        self.browser = hubcheck.browser.Firefox()


    def _stop_test_case_browser(self):
        if self.browser is not None:
            try:
                self.browser.close()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))


    def _start_test_case_recording(self):
        self.recording = None
        if hubcheck.conf.settings.video_dir is not None:
            videodir = os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                hubcheck.conf.settings.video_dir)))
            # self.videofn = os.path.join(videodir,"%s.avi" % (self.id()))
            self.videofn = os.path.join(videodir,"%s.mp4" % (self.id()))
            self.recording = hubcheck.utils.WebRecordXvfb(self.videofn)
            self.recording.start()


    def _stop_test_case_recording(self):
        if self.recording is not None:
            try:
                self.recording.stop()
            except Exception:
                self.logger.debug('Exception ignored: %s\n%s'
                    % (sys.exc_info()[1],traceback.format_exc()))

