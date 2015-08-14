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


class HCNightlyRapptureBuildTool(hubcheck.Tool):

    def __init__(self,logfile='hcnrb.log',loglevel='INFO'):
        super(HCNightlyRapptureBuildTool,self).__init__(logfile,loglevel)

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
            '--repo-dir',
            help='name of the directory to download repositories to',
            action="store",
            dest="repo_dir",
            type=str,
            default="repos")

        self.command_parser.add_argument(
            '--rappture-branch',
            help='branch of rappture repository to checkout',
            action="store",
            dest="rappture_branch",
            type=str,
            default="branches/1.3")

        self.command_parser.add_argument(
            '--runtime-branch',
            help='branch of rappture-runtime repository to checkout',
            action="store",
            dest="runtime_branch",
            type=str,
            default="branches/1.3")

        self.command_parser.add_argument(
            '--bat-branch',
            help='branch of rappture-bat repository to checkout',
            action="store",
            dest="bat_branch",
            type=str,
            default="branches/1.3")

        self.command_parser.add_argument(
            '--rappture-build-dir',
            help='directory where this build of rappture will be installed, the strings @@RAPPTURE_REV@@ and @@RUNTIME_REV@@ will be substituted with values representing the rappture and runtime repository revisions respectively',
            action="store",
            dest="build_dir",
            type=str,
            default="/apps/share64/debian7/rappture/nightly/branch_1.3-@@RAPPTURE_REV@@-@@RUNTIME_REV@@")

        self.command_parser.add_argument(
            '--build-packages',
            help='build gzipped tar packages for rappture and rappture-runtime',
            action="store_true",
            dest="build_packages",
            default=False)

        self.command_parser.add_argument(
            '--copy-tars-dir',
            help='if there are tar files, copy them to the specified directory',
            action="store",
            dest="copy_tars_dir",
            type=str,
            default='')

        self.command_parser.add_argument(
            '--copy-tars-base',
            help='if there are tar files, change the "rappture" protion of the file name',
            action="store",
            dest="copy_tars_base",
            type=str,
            default='rappture')

        self.command_parser.add_argument(
            '--transfer-tars',
            help='if there are tar files, transfer them back, files most be in a publicly accessible place',
            action="store_true",
            dest="transfer_tars",
            default=False)

        self.command_parser.add_argument(
            '--buildscript',
            help='name of the buildscript to use',
            action="store",
            dest="buildscript",
            default="hchub.sh")

        self.command_parser.add_argument(
            '--use',
            help='name of use environments to be sourced',
            action="append",
            dest="use_libs",
            default=[])

        self.command_parser.add_argument(
            '--no-checkout',
            help='don\'t checkout sources, uses already existing sources.',
            action="store_true",
            dest="no_checkout",
            default=False)

        self.command_parser.add_argument(
            '--container',
            help='use the specified container instead of the default container for building (ex. workspace32_dev).',
            action="store",
            dest="container",
            default=None)

        # parse command line and config file options
        self.parse_options()

        # start logging
        self.start_logging()


    def command(self):

        repodir = os.path.join('hcnrb',self.options.repo_dir)
        rappture_url = self.options.repo_base \
                        + '/rappture/svn/' \
                        + self.options.rappture_branch
        runtime_url = self.options.repo_base \
                        + '/rappture-runtime/svn/' \
                        + self.options.runtime_branch
        bat_url = self.options.repo_base \
                        + '/rappture-bat/svn/' \
                        + self.options.bat_branch


        # redirect stdout and stderr to variables
        # so we can log and email them later
        stream_output = self.options.verbosity > 0
        old_stdout = sys.stdout
        sys.stdout = stdout = StreamLogger(sys.stdout,stream_output)

        old_stderr = sys.stderr
        sys.stderr = stderr = StreamLogger(sys.stderr,stream_output)

        # retrieve the username and password for the rappture build user
        username,userpass = self.testdata.find_account_for('appsworkspace')

        # if the user didn't specify a container, lookup the correct one from testdata
        if self.options.container is None:
            apps_container = hubcheck.conf.settings.apps_workspace_toolname
        else:
            apps_container = self.options.container

        # get into a tool session container.
        cm = hubcheck.ContainerManager()
        ws = cm.create(hubcheck.conf.settings.hub_hostname,username,userpass,
                toolname=apps_container)

        # print output to stdout
        ws.log_user = True

        session_number,es = ws.execute('echo $SESSION')

        # catch errors that happen in the shell
        # so we can properly exit and close the workspace
        try:
            exit_bash = False
            exit_apps = False

            # become the apps user
            ws.send('sudo su - apps')
            ws.start_bash_shell()
            exit_bash = True
            output,es = ws.execute('whoami')
            exit_apps = True
            if output != 'apps':
                exit_apps = False
                msg = "unable to su apps"
                self.logger.error(msg)
                raise Exception(msg)


            # setup the external library paths rappture uses for extensions.
            # self.options.use_libs = ['R-3.0.1','matlab-7.12']
            out,es = ws.execute('. /etc/environ.sh')
            for use_lib in self.options.use_libs:
                cmd = 'use -h 2>&1 | grep ^%s:' % (use_lib)
                out,es = ws.execute(cmd,fail_on_exit_code=False)
                if out == '':
                    msg = 'cannot find use script for %s, ignoring' % (use_lib)
                    self.logger.warn(msg)
                else:
                    cmd = 'use -e -r %s' % (use_lib)
                    out,es = ws.execute(cmd)


            if self.options.no_checkout is False:
                # checkout the repositories
                script = """
                    mkdir -p %(repodir)s;
                    cd %(repodir)s;
                    rm -rf stage* builds;
                    if [[ ! -d rappture ]] ; then
                        svn -q checkout %(rappture_url)s rappture;
                    fi
                    cd rappture;
                    { # try to svn update
                        svn cleanup &&
                        svn revert -R . &&
                        svn update &&
                        cd ../
                    } || {  # if the update fails, do an svn checkout
                        cd ../ &&
                        rm -rf rappture &&
                        svn -q checkout %(rappture_url)s rappture
                    }
                    if [[ ! -d runtime ]] ; then
                        svn -q checkout %(runtime_url)s runtime;
                    fi
                    cd runtime;
                    { # try to svn update
                        svn cleanup &&
                        svn revert -R . &&
                        svn update &&
                        cd ../
                    } || {  # if the update fails, do an svn checkout
                        cd ../ &&
                        rm -rf runtime &&
                        svn -q checkout %(runtime_url)s runtime
                    }
                    if [[ ! -d bat ]] ; then
                        svn -q checkout %(bat_url)s bat --depth immediates;
                        cd bat/buildscripts;
                        svn -q update --set-depth infinity;
                        cd -;
                    fi
                    cd bat/buildscripts;
                    { # try to svn update
                        svn cleanup &&
                        svn revert -R . &&
                        svn update
                    } || {  # if the update fails, do an svn checkout
                        cd - &&
                        rm -rf bat &&
                        svn -q checkout %(bat_url)s bat --depth immediates &&
                        cd bat/buildscripts &&
                        svn -q update --set-depth infinity
                    }
                    cd -;
                """ % { 'repodir'       : repodir,
                        'rappture_url'  : rappture_url,
                        'runtime_url'   : runtime_url,
                        'bat_url'       : bat_url }

            else:
                script = """
                    cd %(repodir)s;
                    rm -rf stage* builds;
                """ % { 'repodir' : repodir }

            script = re.sub(r'\n( {4})+','\n',script.strip())

            # checking out the runtime is epic on hubs with slow nfs
            ws.timeout = 60*60
            ws.execute_script(script)

            # get the rappture revision
            ws.execute('cd rappture')
            # rappture_svn_revision,err = ws.execute('svnversion')
            cmd = 'svn info | grep "Last Changed Rev" | cut -d" " -f 4'
            rappture_svn_revision,err = ws.execute(cmd)
            ws.execute('cd -')
            ws.execute('cd runtime')
            # runtime_svn_revision,err = ws.execute('svnversion')
            cmd = 'svn info | grep "Last Changed Rev" | cut -d" " -f 4'
            runtime_svn_revision,err = ws.execute(cmd)
            ws.execute('cd -')

            # craft our buildscript
            buildscript = './bat/buildscripts/%s' % (self.options.buildscript)

            # check if the file exists, die if it doesn't
            ws.execute('[[ -x %s ]]' % (buildscript))

            # update the base_dir and build_dir
            # add expat and zlib libraries if we are building packages
            build_dir = self.options.build_dir
            base_dir = os.path.dirname(build_dir)
            if self.options.build_packages is True:
                tar_dir = os.path.join(build_dir,"tars")
                dist_flags = '--with-expat --with-zlib'
            else:
                tar_dir = ''
                dist_flags = ''

            # populate the build_dir's template variables:
            # @@RAPPTURE_REV@@
            # @@RUNTIME_REV@@

            assert int(rappture_svn_revision) > 0, \
                'invalid rappture revision number: %s' \
                % (rappture_svn_revision)
            build_dir = re.sub('@@RAPPTURE_REV@@',rappture_svn_revision,build_dir)

            assert int(runtime_svn_revision) > 0, \
                'invalid runtime revision number: %s' \
                % (runtime_svn_revision)
            build_dir = re.sub('@@RUNTIME_REV@@',runtime_svn_revision,build_dir)


            # update the build script with options from command line
            command = ('sed'
                      + ' -e "s:base_dir=.*:base_dir=\\"%(base_dir)s\\":"'
                      + ' -e "s:build_dir=.*:build_dir=\\"%(build_dir)s\\":"'
                      + ' -e "s:tar_dir=.*:tar_dir=\\"%(tar_dir)s\\":"'
                      + ' -e "s:distribution_flags=.*:distribution_flags=\\"%(dist_flags)s\\":"'
                      + ' -i %(buildscript)s') % {
                        'base_dir'    : base_dir,
                        'build_dir'   : build_dir,
                        'tar_dir'     : tar_dir,
                        'dist_flags'  : dist_flags,
                        'buildscript' : buildscript,
                      }

            ws.execute(command)

            # remove previous build by the same name
            ws.execute('rm -rf %s' % (build_dir))

            # takes about 20 minutes to compile,
            # give it extra time for hubs with slow nfs
            ws.timeout = 60*60

            # compile
            output,es = ws.execute(buildscript)

            # reset the timeout after compiling
            ws.timeout = 10*60

            # check if we should copy tar files to another directory
            if self.options.build_packages is True \
               and self.options.copy_tars_dir != '':
                command = 'mkdir -p %s' % (self.options.copy_tars_dir)
                output,es = ws.execute(command)

                command = 'rm -f %s/%s-*.tar.gz' \
                            % (self.options.copy_tars_dir,
                               self.options.copy_tars_base)
                output,es = ws.execute(command)

                command = 'ls %s/rappture-*.tar.gz' % (tar_dir)
                output,es = ws.execute(command,fail_on_exit_code=False)
                if es == 0:
                    for remote_fpath in output.split():
                        new_fpath_base = os.path.basename(remote_fpath)

                        # update the tar file name
                        if self.options.copy_tars_base != 'rappture':
                            remote_fpath_base = os.path.basename(remote_fpath)
                            new_fpath_base = re.sub('rappture',
                                self.options.copy_tars_base,remote_fpath_base)

                        # copy the file to copy_tars_dir directory
                        ws.execute('cp {0} {1}/{2}'.format(remote_fpath,
                            self.options.copy_tars_dir,new_fpath_base))

            # exit sudo
            ws.stop_bash_shell()
            exit_bash = False
            ws.send('exit')
            exit_apps = False

            # check if we should transfer tar files back to host
            if self.options.build_packages is True \
               and self.options.transfer_tars is True:
                # file names look something like this
                # rappture-runtime-src-20140204.tar.gz
                # rappture-Linux-x86_64-20140204.tar.gz
                # rappture-src-20140204.tar.gz
                command = 'ls %s/rappture-*.tar.gz' % (tar_dir)
                output,es = ws.execute(command,fail_on_exit_code=False)
                if es == 0:
                    # create a temporary directory in the home
                    # directory to store the tar file for transfer
                    command = 'mktemp -d --tmpdir=${HOME} hcnrb_XXXX'
                    tempdir,es = ws.execute(command)

                    for remote_fpath in output.split():

                        # copy the file to user's home directory
                        # so we can sftp it
                        ws.execute('cp {0} {1}'.format(remote_fpath,tempdir))

                        # sftp the file
                        local_fpath = os.path.basename(remote_fpath)
                        remote_fpath = os.path.join(tempdir,
                                        os.path.basename(remote_fpath))
                        ws.exportfile(remote_fpath,local_fpath)

                        # remove the file from the user's home directory
                        output,es = ws.execute('rm %s' % (remote_fpath))

                    # remove the temp directory
                    output,es = ws.execute('rm -rf %s' % (tempdir))


        finally:

            # exit sudo if necessary
            if exit_bash:
                ws.stop_bash_shell()
            if exit_apps:
                ws.send('exit')

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

    tool = HCNightlyRapptureBuildTool()
    tool.run()


