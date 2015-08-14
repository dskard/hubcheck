import logging
import os
import re
import select
import signal
import subprocess


BUFSIZ = 4096


class XvfbView(object):


    def __init__(self, xvfb_display, viewer_display):
        """
        show an xvfb display using x11vnc


        xvfb_display: display where xvfb is running
        viewer_display: display to show vnc window on
        """

        self.logger = logging.getLogger(__name__)

        self.xvfb_display = xvfb_display
        self.viewer_display = viewer_display

        self.vnc_server_proc = None
        self.vnc_client_proc = None


    def start(self):
        """
        start a vnc session to the xvfb display
        """

        # start up the vnc server
        # we only allow one connection,
        # and the server will exit after that connection ends
        cmd = 'DISPLAY=%s x11vnc -display %s ' \
              % (self.viewer_display,self.xvfb_display) \
              + '-norc -nopw -listen localhost'
        self.vnc_server_proc = subprocess.Popen(cmd,shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                preexec_fn=os.setsid,
                                bufsize=BUFSIZ)

        # read the output looking for the port number
        buf = ''
        port = None
        errmsg = None
        break_while = False
        re_port = re.compile(r'PORT=([^\s]+)')
        re_fail = re.compile(r'x11vnc was unable to open .*$',
                    flags=re.M)
        while self.vnc_server_proc.poll() is None:
            r,w,x = select.select([self.vnc_server_proc.stdout,
                                   self.vnc_server_proc.stderr],[],[])
            for f in r:
                data = os.read(f.fileno(),BUFSIZ)
                self.logger.debug(data)
                buf += data

                matches = re_port.search(buf)
                if matches:
                    port = matches.group(1)
                    break_while = True
                    break

                matches = re_fail.search(buf)
                if matches:
                    errmsg = matches.group()
                    self.logger.error(errmsg)
                    break_while = True

                    # we don't raise an exception here because its not the
                    # end of the world if the x11vnc doesnt start

            if break_while:
                break

        self.logger.debug('port = %s' % (port))

        if port is not None:

            self.logger.info('x11vnc session: localhost:%s' % (port))

            # start up the client that the user sees
            cmd = 'DISPLAY=%s vncviewer localhost:%s' \
                    % (self.viewer_display,port)
            self.vnc_client_proc = subprocess.Popen(cmd,shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    preexec_fn=os.setsid)
        else:
            self.logger.info('skipped opening vncviewer because' \
                             + ' x11vnc did not return a port')


    def stop(self):
        """
        stop the vnc server and client viewing the xvfb display
        """

        # shutdown the vnc server and client
        if self.vnc_client_proc is not None:
            self.logger.info("stopping the vnc client")
            # self.vnc_client_proc.kill()
            os.killpg(self.vnc_client_proc.pid, signal.SIGKILL)
            self.vnc_client_proc = None

        if self.vnc_server_proc is not None:
            self.logger.info("stopping the vnc server")
            # the server is probably already dead
            # because we setup x11vnc to accept only
            # one connection and die upon disconnect
            # but we wrap it in a try and attempt
            # to kill it just in case it is still alive.
            try:
                os.killpg(self.vnc_server_proc.pid, signal.SIGKILL)
            except Exception as e:
                self.logger.exception(e)
            self.vnc_server_proc = None

