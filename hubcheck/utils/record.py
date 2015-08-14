import logging
import os
import pty
import signal
import shlex
import subprocess

class WebRecordXvfb(object):


    def __init__(self, filename, size=None, display=None):
        """
        record an xvfb session running a test

        filename: the name of the file to save the recording to.
        size: 2-tuple of (W,H) (ex. (1024,768)).
        display: the DISPLAY to record (ex. ':0.0').

        """

        self.logger = logging.getLogger(__name__)


        self.filename = filename

        if display is None:
            display = os.environ['DISPLAY']

        self.display = display

        if size is None:
            # assuming there is only one screen for the display,
            # use the following command to grab the size of the display:
            # xdpyinfo -display :0 2> /dev/null | grep dimensions
            #
            # the output looks something like this:
            # dimensions:    1680x1050 pixels (444x277 millimeters)
            #
            # you could also use this command to get just the WxH
            # xdpyinfo -display :0.0 2> /dev/null \
            #     | grep dimensions | tr -s ' ' | cut -d' ' -f3
            #
            # which gives:
            # 1680x1050

            #cmd = 'xdpyinfo -display %s 2> /dev/null' % (self.display) \
            #      + ' | grep dimensions | tr -s ' ' | cut -d' ' -f3'
            #p = subprocess.Popen(cmd,shell=True)
            #os.waitpid(p.pid,0)
            size = (1024,768)

        self.size = size

        self.p = None


    def start(self):
        """
        start recording a display
        """

        # use ffmpeg to record the display
        # -y automatically overwrites existing output file.
        # use the x11grab extension with the display as the input.
        # -crf 0 increases the quality of the videos
        # order of arguments matters,
        # -vcodec must come after -i to ensure it is
        # interpreted as an encoding codec
        cmd = "ffmpeg -y" \
              + " -video_size %sx%s" % (self.size) \
              + " -framerate 25" \
              + " -preset ultrafast" \
              + " -crf 0 " \
              + " -threads 0" \
              + " -f x11grab " \
              + " -i %s " % (self.display) \
              + " -vcodec libx264 " \
              + " %s" % (self.filename)

        self.logger.info('recording X session with command: %s' % (cmd))

        # needs a shell to record the display
        # FIXME: communicate with the shell through a pty to quit recording

        self.p = subprocess.Popen(cmd,shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    preexec_fn=os.setsid)


    def stop(self):
        """
        stop recording a display
        """

        if self.p is not None:
            self.logger.info('saving recorded X session to %s' % (self.filename))

            # Send the signal to all the process groups
            os.killpg(self.p.pid, signal.SIGTERM)

            self.p = None
