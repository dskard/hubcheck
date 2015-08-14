import re
import sys
import types
import socket
import logging
import time

from hubcheck.exceptions import ConnectionClosedError
from hubcheck.exceptions import ExitCodeError

class SSHShell(object):
    """
    Provide an Expect like interface to an ssh connection

    one caveat is that if the channel was started with a pty allocated,
    we can only pull data from the stdout.
    for details, see:
    http://www.lag.net/paramiko/docs/paramiko.Channel-class.html#recv_stderr
    """

    TIMEOUT = 0

    def __init__(self, client, channel, debug=False,
                 log_user=False, buffer_size=4096,timeout=10,
                 pty_width=1000,pty_height=1000,startup_cmd=None):

        self.logger = logging.getLogger(__name__)

        self.debug = debug
        self.log_user = log_user
        self.match = None
        self.timeout = timeout

        self._ssh_client = client
        self._ssh_channel = channel

        self._ssh_channel_pty_width = pty_width
        self._ssh_channel_pty_height = pty_height
        self._ssh_channel_command = startup_cmd

        self._sftp_client = None
        self._sftp_channel = None

        self._prompt = ''
        self._default_prompt = '(%|#|\$) $'
        self._use_sws = True
        self._searchwindowsize = 0
        self._buffer_stdout = ''
        self._buffer_stderr = ''
        self._buffer_size = buffer_size
        self._log_file = sys.stdout

        # start the shell count with the login shell
        self._bash_shell_count = 1

        self.set_search_prompt(self._default_prompt)

        # make sure we are in a bash shell
        self.start_bash_shell()


    def __del__(self):

        self.close()


    def close(self):

        if self._ssh_client is not None:

            self.logger.info("closing sshshell object")
            transport = self._ssh_client.get_transport()

            if transport is not None and \
               transport.is_active() and \
               transport.is_authenticated():

                # exit all of the bash shells
                try:
                    while self._bash_shell_count > 0:
                        self.stop_bash_shell()
                except socket.error as e:
                    # connection is probably closed
                    pass
                finally:
                    # reset our shell count to 0
                    self._bash_shell_count = 0

                # close the sftp connection
                # the underlying channel is closed when the client is closed
                if self._sftp_client:
                    self.logger.debug("closing sftp client")
                    self._sftp_client.close()
                    self._sftp_client = None
                    self._sftp_channel = None

                # close the ssh connection
                # this closes the transport, which closes all channels
                # associated with the session
                self.logger.debug("closing ssh client")
                self._ssh_client.close()

            # clear our handles
            self._ssh_client = None
            self._ssh_channel = None


    def searchwindowsize(self,sws=None):
        # search window size must be a non-negative integer
        if sws != None:
            if sws < 0:
                sws = 0
            self._searchwindowsize = -1 * int(sws)
        return self._searchwindowsize


    def set_search_prompt(self,prompt):
        self._prompt = prompt
        return self._prompt


    def update_search_prompt(self):
        return self.set_search_prompt(re.escape(self.get_prompt()))


    def get_buffer(self):
        return self._buffer_stdout


    def get_buffer_stderr(self):
        return self._buffer_stderr


    def update_buffer(self):
        self._buffer_stdout += self._ssh_channel.recv(self._buffer_size)


    def update_buffer_stderr(self):
        self._buffer_stderr += self._ssh_channel.recv_stderr(self._buffer_size)


    def log_file(self,fd=None):
        if hasattr(fd,'write'):
            self._log_file = fd
        else:
            self._log_file = None


    def send(self,command):
        """"""

        if not command.endswith('\r'):
            sendcmd = "%s\r" % (command)
        else:
            sendcmd = command

        self.send_raw(sendcmd)

        if sendcmd != '\r':
            searchcmd = "%s\r\n" % (re.escape(command.rstrip('\r')))
            self._use_sws = False
            self.expect([searchcmd])
            self._use_sws = True


    def send_raw(self,command):
        """"""

        self._debug_print("sending: %s" % (repr(command)))
        self._ssh_channel.sendall(command)


    def expect(self,patterns=[],flags=re.DOTALL):
        """"""
        result = None
        pattern_index = -1

        # make sure we block until there is data to read
        self._ssh_channel.settimeout(self.timeout)

        if type(patterns) in [types.StringType, types.UnicodeType]:
            patterns = [patterns]

        compiled_patterns = []
        error_on_timeout = True
        for pattern in patterns:
            if pattern == self.TIMEOUT:
                error_on_timeout = False
                continue
            compiled_patterns.append(re.compile(pattern,flags=flags))

        try:
            while True:

                self._debug_print("looking for %s in %s" \
                    % (patterns,repr(self._buffer_stdout)))

                if self._use_sws:
                    buf = self._buffer_stdout[self._searchwindowsize:]
                else:
                    buf = self._buffer_stdout

                # check buffer for patterns
                for pattern in compiled_patterns:
                    result = pattern.search(buf)
                    if result:
                        result = pattern.search(self._buffer_stdout)
                        self._debug_print("matched text: %s" \
                            % (repr(result.group())))

                        if result.groups():
                            # there are groups, display them
                            self._debug_print("groups: %s" \
                                % (repr(result.groups())))

                        # get the pattern index of the matched text
                        pattern_index = compiled_patterns.index(pattern)

                        # remove the matched text from the buffer
                        end = result.end()
                        self._buffer_stdout = self._buffer_stdout[end:]

                        # print what is left in the buffer
                        self._debug_print("buffer_stdout: %s" \
                            % (repr(self._buffer_stdout)))
                        self._debug_print("buffer_stderr: %s" \
                            % (repr(self._buffer_stderr)))

                        # break out of checking patterns
                        break

                if result:
                    # break out of checking for new text
                    break

                # grab data from stdout
                recv_stdout = self._ssh_channel.recv(self._buffer_size)
                if len(recv_stdout) == 0:
                    # channel has closed
                    msg = 'ssh connection closed unexpectedly:'
                    msg += '\npatterns:\n%s\nbuffer:\n%s\n'
                    msg = msg % (patterns,self._buffer_stdout)
                    self.logger.info(msg)
                    # sleep for 10 seconds and then
                    # try to recover by opening a new channel
                    # 10 seconds is an arbitrary number
                    recovertime = 10
                    msg = 'attempt to recover in %i seconds...' % (recovertime)
                    self.logger.info(msg)
                    time.sleep(recovertime)
                    try:
                        self.logger.info('trying to open a new ssh connection')
                        new_channel = self._ssh_client.get_transport().open_session()
                        new_channel.get_pty(width=self._ssh_channel_pty_width,
                                            height=_ssh_channel_pty_height)
                        new_channel.exec_command(self._ssh_channel_command)
                        # make sure we close the old channel
                        try:
                            self._ssh_channel.close()
                        except Exception as e:
                            self.logger.error('exception raised while trying' \
                                              + ' to close the old ssh channel')
                        self._ssh_channel = new_channel
                        # grabbing stdout will probably only help if the
                        # channel was originally closed while trying to
                        # start up the ssh shell. all other cases will probably
                        # timeout and look like the command failed.
                        recv_stdout = self._ssh_channel.recv(self._buffer_size)
                    except Exception as e:
                        msg = 'tried to create a new ssh channel,' + \
                              ' but that failed as well'
                        self.logger.error(msg)
                        raise ConnectionClosedError(msg)
                self._log_user_print(recv_stdout)

                # grab data from stderr if there is any
                recv_stderr = ''
                if self._ssh_channel.recv_stderr_ready():
                    recv_stderr = self._ssh_channel.recv_stderr(self._buffer_size)
                    self._log_user_print(":%s:" % recv_stderr)

                self._buffer_stdout += recv_stdout
                self._buffer_stderr += recv_stderr

        except socket.timeout as e:
            if error_on_timeout:
                self.logger.exception(e)
                raise


        self.match = result
        return pattern_index


    def _debug_print(self,s):
        self.logger.debug(s)
        if self.debug and self._log_file:
            print >>self._log_file, s


    def _log_user_print(self,s):
        self.logger.info(s)
        if self.log_user and self._log_file:
            self._log_file.write(s)


    ### HELPER FUNCTIONS ###

    def start_bash_shell(self):

        # if there is no pty, this will fail.
        # because there is no prompt to check against.

        self.logger.debug("entering bash shell")
        self.execute('export HISTFILE=')
        self.send('/bin/bash --login --rcfile /etc/bash.bashrc --noprofile -s')
        self.execute('export HISTFILE=')
        self._bash_shell_count += 1


    def source(self,fname):
        """
        source a file
        """

        self.send('source %s' % (fname))
        self.update_search_prompt()


    def bash_test(self,test):
        """
        perform a bash test
        """

        cmd = 'test %s && echo 1 || echo 0' % (test)
        output,es = self.execute(cmd)

        if output == '1':
            return True
        else:
            return False


    def stop_bash_shell(self):
        """exit a previously started bash shell"""

        self.logger.debug("exiting bash shell")
        self.send_raw('exit\r')
        self.expect(['exit'])
        self._bash_shell_count -= 1


    def get_prompt(self):
        p = ''
        self.send('\r')
        self.expect(['[^\r\n]*\r\n([^\r\n]+)$'])
        return self.match.groups()[0]


    def execute(self,commands,fail_on_exit_code=True):
        out = ''

        if self._prompt == self._default_prompt:
            # the instance's prompt is set to the class default,
            # in this case we want to use a more specific prompt
            # so we know when commands have finished executing.
            prompt = re.escape(self.get_prompt())
        else:
            # use the user provided prompt
            prompt = self._prompt

        if type(commands) in [types.StringType, types.UnicodeType]:
            commands = [commands]

        self.logger.debug('commands = %s' % (commands))

        reset_sws = False
        if self._searchwindowsize == 0:
            # we are only looking for the prompt which should come
            # within the last 512 characters of the end of the buffer.
            # if the _searchwindowsize has been changed by the user,
            # we don't reset it.
            reset_sws = True
            self.searchwindowsize(512)

        for command in commands:

            # send the command to the terminal
            self.send(command)

            # get the output of the command
            self.expect(["(.*)%s" % (prompt)])

            # remove the trailing \r\n
            out = self.match.groups()[0].rstrip()

            # turn off log_user to reduce noise
            # while we check the command's exit status
            old_log_user = self.log_user
            self.log_user = False

            # check the exit status of the command
            self.send('echo $?')
            self.expect(['(\d+)\r\n'])
            exit_code = int(self.match.groups()[0])

            # restore log_user
            self.log_user = old_log_user

            if fail_on_exit_code:
                # if we got a non-zero exit status, raise error
                if exit_code != 0:
                    msg = 'command exited with code %s: %s -> %s' \
                        % (exit_code,command,out)
                    self.logger.error(msg)
                    raise ExitCodeError(msg)

        if reset_sws:
            self.searchwindowsize(0)

        # return the last command's output
        return (out,exit_code)


    def execute_script(self,script,fail_on_exit_code=True):
        out = ''

        if self._prompt == self._default_prompt:
            # the instance's prompt is set to the class default,
            # in this case we want to use a more specific prompt
            # so we know when commands have finished executing.
            prompt = re.escape(self.get_prompt())
        else:
            # use the user provided prompt
            prompt = self._prompt

        reset_sws = False
        if self._searchwindowsize == 0:
            # we are only looking for the prompt which should come
            # within the last 512 characters of the end of the buffer.
            # if the _searchwindowsize has been changed by the user,
            # we don't reset it.
            reset_sws = True
            self.searchwindowsize(512)

        if not script.endswith('\r'):
            script = "%s\r" % (script)

        self.send_raw(script)

        # we don't change log user because above, we use the send_raw function
        # and don't call expect() to get the output, so the script is never
        # shared through the log_user function. below is the only call to the
        # expect function. we rely on this call to share the script through
        # log_user

#        # turn off log_user to reduce noise
#        # while we check the command's exit status
#        old_log_user = self.log_user
#        self.log_user = False

        # check the exit status of the command
        cmd = 'echo $?'
        self.send_raw(cmd+'\r')
        cmd = re.escape(cmd)
        self.expect('(.*)'+prompt+cmd+'\r\n(\d+)\r\n')

#        # restore log_user
#        self.log_user = old_log_user

        # get the output of the all commands
        # remove the trailing \r\n
        out = self.match.groups()[0].rstrip()
        exit_code = int(self.match.groups()[1])

        # get the output of the last commands
        out = re.split(prompt+'[^\r\n]*(\r\n)*',out)[-1]

        if fail_on_exit_code:
            # check the exit status of the command
            # if we got a non-zero exit status, raise error
            if exit_code != 0:
                msg = 'script exited with code %s: %s -> %s' \
                    % (exit_code,command,out)
                self.logger.error(msg)
                raise ExitCodeError(msg)

        if reset_sws:
            self.searchwindowsize(0)

        # return the last command's output
        return (out,exit_code)


    def write_file(self,filename,data,setinal="_END_"):
        """
        write a file to disk. this is helpful for times when sftp doesn't
        like when sudo'd to another user.
        """

        p = self.get_prompt()
        data = data.replace('\\','\\\\')
        data = data.replace('$','\$')
        self.send_raw(
            "cat <<- %(setinal)s > %(filename)s\r%(data)s\r%(setinal)s\r" \
            % {'setinal' : setinal, 'filename' : filename, 'data' : data})
        self.expect(re.escape(p))
        write_len,es = self.execute('wc -c %s | cut -d" " -f1' % (filename))
        return int(write_len)


    def read_file(self,filename,convert_crlf=True):
        """
        read a file from disk.
        """

        data,es = self.execute("cat %s" % (filename))

        # FIXME:
        # figure out how to read the file without needing CRLF translations
        if convert_crlf:
            # translate \r\n (inserted by the shell) to \n
            data = data.replace("\r\n","\n")

        return data



