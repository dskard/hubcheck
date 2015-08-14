#!/usr/bin/env python

import hubcheck
import os
import pprint
import pytest
import re
import StringIO
import sys
import unittest


class StreamLogger(StringIO.StringIO):

    def __init__(self,old_buffer,stream_output,*args,**kwargs):
        # super(StreamLogger,self).__init__(*args,**kwargs)
        StringIO.StringIO.__init__(self,*args,**kwargs)
        self.stream_output = stream_output
        self.old_buffer = old_buffer

    def write(self,text):
        if self.stream_output is True:
            self.old_buffer.write(text)
            self.old_buffer.flush()
        # super(StreamLogger,self).write(text)
        StringIO.StringIO.write(self,text)


class HCNRBTest_LangTcl_Tool(hubcheck.Tool):

    def __init__(self,logfile='hcnrb.log',loglevel='INFO'):
        super(HCNRBTest_LangTcl_Tool,self).__init__(logfile,loglevel)

        self.command_parser.add_argument(
            '--verbosity',
            help='results detail level',
            action="store",
            dest="verbosity",
            type=int)

        self.command_parser.add_argument(
            '--email-smtp',
            help='address of the smtp server sending email reports',
            action="store",
            dest="email_smtp",
            type=str)

        self.command_parser.add_argument(
            '--email-from',
            help='email address of user sending email reports',
            action="store",
            dest="email_from",
            type=str)

        self.command_parser.add_argument(
            '--email-to',
            help='email address of user receiving email reports',
            nargs="+",
            action="store",
            dest="email_to",
            type=str)

        self.command_parser.add_argument(
            '--email-subject',
            help='email report subject',
            nargs="+",
            action="store",
            dest="email_subject",
            type=str)

        self.command_parser.add_argument(
            '--no-email',
            help='do not send email',
            action="store_true",
            dest="no_email",
            default=False)

        self.command_parser.add_argument(
            '--repo-base',
            help='url base of rappture repositories (rappture,runtime,bat)',
            action="store",
            dest="repo_base",
            type=str,
            default="https://nanohub.org/infrastructure")

        self.command_parser.add_argument(
            '--rappture-branch',
            help='branch of rappture repository to checkout tests from',
            action="store",
            dest="rappture_branch",
            type=str,
            default="branches/1.3")

        self.command_parser.add_argument(
            '--rappture-version',
            help='name of the version to be used for testing',
            action="store",
            dest="rappture_version",
            type=str,
            default="")

        self.command_parser.add_argument(
            '--testlog',
            help='name of the tcltests log file',
            action="store",
            dest="testlog",
            type=str,
            default="lang_tcl_unittests.log")

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging()


    def command(self):

        repodir = 'hcnrb_tests'
        testdir = 'lang_tcl'
        testlog = os.path.join('${HOME}',repodir,testdir,self.options.testlog)
        repourl = self.options.repo_base \
                    + '/rappture/svn/' \
                    + self.options.rappture_branch \
                    + '/lang/tcl/tests'


        # redirect stdout and stderr to variables
        # so we can log and email them later
        stream_output = self.options.verbosity > 0
        old_stdout = sys.stdout
        sys.stdout = stdout = StreamLogger(sys.stdout,stream_output)

        old_stderr = sys.stderr
        sys.stderr = stderr = StreamLogger(sys.stderr,stream_output)

        # retrieve the username and password for the rappture build user

        hostname = self.testdata.find_url_for('https')
        username,userpass = self.testdata.find_account_for('appsworkspace')

        # get into a tool session container.
        cm = hubcheck.ContainerManager()
        ws = cm.access(hostname,username,userpass)

        # print output to stdout
        ws.log_user = True

        session_number,es = ws.execute('echo $SESSION')

        # catch errors that happen in the shell
        # so we can properly exit and close the workspace
        try:
            # checkout the test repository
            script = """
                mkdir -p %(repodir)s;
                cd %(repodir)s;
                rm -rf %(testdir)s;
                svn -q checkout %(repourl)s %(testdir)s;
                cd %(testdir)s;
            """ % { 'repodir'       : repodir,
                    'repourl'       : repourl,
                    'testdir'       : testdir }

            commands = script.strip().replace('    ','').split('\n')

            ws.timeout = 300
            ws.execute(commands)


            # setup the environment with a specific rappture version
            ws.execute('. /etc/environ.sh')
            command = "use -e -r rappture"
            if self.options.rappture_version != "":
                command += '-%s' % (self.options.rappture_version)
            ws.execute(command)


            # run the tcl test suite, save the output as a log
            testlog,es = ws.execute('readlink -f %s' % (testlog))
            ws.execute('tclsh all.tcl > %s' % (testlog))


            # sftp the log file back to be processed
            local_fpath = os.path.basename(testlog)
            ws.exportfile(testlog,local_fpath)


        finally:

            # shut down the ssh connection
            ws.close()

            # close the workspace
            cm.stop_all()


        # reset the stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        # close the test results stream
        stdout.close()
        stderr.close()


if __name__=='__main__':

    tool = HCNRBTest_LangTcl_Tool()
    tool.run()


