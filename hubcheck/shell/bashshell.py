import pexpect
import re
import sys
import types
import logging
import time

class BashShell(object):

    def __init__(self,buffer_size=1024):

        # FIXME: figure out how to deal with WINCH

        self.logger = logging.getLogger(__name__)
        self.logger.write = self._write
        self.logger.flush = self._flush

        self.debug = False
        self.log_user = False
        self.match = None

        self._client = None

        self._timeout = 10
        self._buffer = ''
        self._buffer_size = buffer_size
        self._bash_shell_count = 0

        self.set_prompt()


    # this will be the method called by the pexpect object to log
    # http://python.6.x6.nabble.com/pexpect-and-logging-integration-td980456.html
    def _write(*args, **kwargs):

        content = args[0]

        # let's ignore other params, pexpect only use one arg AFAIK
        if content in [' ', '', '\n', '\r', '\r\n']:
            # don't log empty lines
            return

        for eol in ['\r\n', '\r', '\n']:
            # remove ending EOL, the logger will add it anyway
            content = re.sub('\%s$' % eol, '', content)

        # call the logger info method with the reworked content
        return self.logger.info(content)


    def _flush(self):

        # leave it to logging to flush properly
        pass


    def set_prompt(self,new_prompt='(%|#|\$) $'):

        self._prompt = new_prompt
        return self._prompt


    def get_buffer(self):

        return self._buffer


    def get_client(self):

        return self._client


    def update_buffer(self):

        # self._buffer += self._channel.recv(self._buffer_size)
        pass


    def close(self):
        """Close the channel"""

        while self._bash_shell_count > 0:
            self.stop_bash_shell()

        # close the pexpect object
        self._client.close()

        # reset the prompt to the default prompt regular expression
        self.set_prompt()




    def connect(self):
        """Spawn a new bash shell"""

        # start up a bash shell
        cmd = '/bin/bash --login --rcfile /etc/bash.bashrc --noprofile'
        self._client = pexpect.spawn(command=cmd,logfile=self.logger)

        self._client.setecho(False)
        self._client.delaybeforesend = 0.2

        # clear the buffer of header text
        # from the newly invoked shell
        self.expect([self._prompt])

        # make sure we are in a bash shell
        self.start_bash_shell()

        # retrieve the prompt from the shell
        self.send('')
        # self.expect(['[^\r\n]*\r\n([^\r\n]+)$'])
        # self.expect(['[^\r\n]*[\r\n]+([^\r\n]+)$'])
        self.expect(["(.*)"])
        if self.match:
            new_prompt = self.match.group(1)
            new_prompt = re.escape(new_prompt)
            self.logger.debug("updating prompt from %s to %s" \
                % (repr(self._prompt),repr(new_prompt)))
            self._prompt = new_prompt


    def send(self,command):
        """"""

        if not command.endswith('\r'):
            sendcmd = "%s\r" % (command)
        else:
            sendcmd = command

        self.send_raw(sendcmd)

        #if sendcmd != '\r':
        #    searchcmd = "%s\r\n" % (re.escape(command))
        #    self.expect([searchcmd])


    def send_raw(self,command):
        """"""

        self.logger.debug("sending: %s" % (repr(command)))
        self._client.send(command)


    def expect(self,patterns=[],timeout=10,flags=0):
        """"""

        if type(patterns) in [types.StringType,types.UnicodeType]:
            patterns = [patterns]

        lpatterns = len(patterns)
        patterns.append(pexpect.EOF)
        # patterns.append(pexpect.TIMEOUT)

        pattern_index = self._client.expect(patterns,timeout)

        if (pattern_index >= 0) and (pattern_index < lpatterns):
            self.match = self._client.match
        else:
            patterns_index = -1

        return pattern_index


    ### HELPER FUNCTIONS ###

    def start_bash_shell(self):

        commands = ['export HISTFILE=',
                    '/bin/bash --login --rcfile /etc/bash.bashrc --noprofile',
                    'export HISTFILE=']
        output = self.execute(commands)
        self._bash_shell_count += 1

    def stop_bash_shell(self):
        """exit a previously started bash shell"""

        self.send_raw('exit')
        # self.expect(['exit'])
        self._bash_shell_count -= 1


    def prompt(self):
        p = ''
        self.send('\r')
        self.expect(['[^\r\n]*\r\n([^\r\n]+)$'])
        return self.match.groups()[0]


    def execute(self,commands):
        # prompt = self.prompt()
        out = ''

        if type(commands) == types.StringType:
            commands = [commands]

        for command in commands:

            # send the command to the terminal
            self.send(command)

            # get the output of the command
            self.expect(["(.*)%s" % (self._prompt)])

            # remove the trailing \r\n
            out = self.match.groups()[0].rstrip()

            # check the exit status of the command
            exit_code = -1
            self.send('echo $?')
            self.expect(['(\d+)\r\n'])
            exit_code = self.match.groups()[0]

            # if we got a non-zero exit status, raise error
            if int(exit_code) != 0:
                raise RuntimeError(out)

        # return the last command's output
        return out



import unittest
class bash_shell_tests(unittest.TestCase):

    def setUp(self):
        self.c = BashShell()
        self.c.debug = False
        self.c.log_user = False

    def test_connect(self):
        self.c.connect()

    def tearDown(self):
        self.c.close()

if __name__ == '__main__':
    tr = unittest.TextTestRunner(stream=sys.stdout,verbosity=0)
    unittest.main(testRunner=tr,exit=False)

# TODO:
# i don't think close() works properly, probably need another exit call
# need to write test cases
