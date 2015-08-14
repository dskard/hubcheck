import os
import re
import sys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait

from hubcheck.shell import ContainerManager
from hubcheck.shell import ToolSession
from hubcheck.exceptions import FormSubmissionError
from hubcheck.exceptions import NavigationError
from hubcheck.exceptions import TimeoutException
from hubcheck.exceptions import ExitCodeError

class Subversion(object):

    def __init__(self,ws,username,userpass):

        self.ws = ws
        self.username = username
        self.userpass = userpass


    def add(self,filelist):
        """add files to the source code repository
        """

        self.ws.execute('svn add %s' % (' '.join(filelist)))


    def remove(self,filelist):
        """remove files from the source code repository
        """

        self.ws.execute('svn remove %s' % (' '.join(filelist)))


    def checkout(self,svn_url,toolname):
        """checkout a source code repository

           currently only works for public repositories
           where users do not need to login.
        """

        revision = None

        prompt = re.escape(self.ws.get_prompt())
        self.ws.send('svn checkout --username %s %s %s' \
                        % (self.username,svn_url,toolname))
        while (True):
            i = self.ws.expect(['Password for \'%s\': ' % (self.username),
                                '\(t\)emporarily\?',
                                'Username: ',
                                'Checked out revision (\d+).',
                                self.ws.TIMEOUT,
                               ])
            if i == 0:
                # password
                self.ws.send_raw('%s\r' % (self.userpass))
                continue
            elif i == 1:
                # temporary store
                self.ws.send('t')
                continue
            elif i == 2:
                # username
                self.ws.send(self.username)
                continue
            elif i == 3:
                # Checked out revision ...
                revision = self.ws.match.groups()[0]
                break
            elif i == 4:
                # timeout
                raise TimeoutException(
                    'while trying to checkout %s: %s' \
                    % (svn_url,self.ws.get_buffer()))
            else:
                # unexpected state
                raise RuntimeError(
                    'unexpected result \'%s\', while trying to svn check out %s: %s' \
                    % (str(i),svn_url,self.ws.get_buffer()))

        self.ws.expect([prompt])
        return revision


    def commit(self,message):
        """commit files to the source code repository server
        """

        revision = None

        # commit the changed file back to the source code repository
        prompt = re.escape(self.ws.get_prompt())
        self.ws.send('svn commit --username %s -m "%s"\r' \
                        % (self.username,message))
        pattern_idx = self.ws.expect(['Password for \'%s\': ' % (self.username),prompt])
        if pattern_idx == 0:
            self.ws.send_raw('%s\r' % (self.userpass))
            # grab the commit revision number
            i = self.ws.expect(['Committed revision (\d+).'])
            if i == 0:
                revision = self.ws.match.groups()[0]
            # wait for the prompt to make sure the commit completed
            self.ws.expect([prompt])
        elif pattern_idx == 1:\
            # nothin was available to commit
            pass
        # self.ws.expect([prompt])

        return revision



class Contribtool(object):

    def __init__(self, hubname, browser, catalog,
            repo_url_template="https://%(hubname)s/tools/%(toolname)s/svn/trunk"):

        self.hubname = hubname
        self.browser = browser
        self.catalog = catalog
        self.logger = self.browser.logger

        self.update_marker = '# hc contribtool update: '
        self.repo_url_template = repo_url_template


    def __wait_for_tool_state(self,po,state):

        def condition(browser):
            self.logger.debug('waiting until tool state is %s' % (state))
            current_state = po.get_tool_state()
            self.logger.debug('current state = %s' % (current_state))
            return current_state.lower() == state.lower()

        message = "while waiting for tool state to change to %s" % (state)
        w = WebDriverWait(self.browser,10)
        w.until(condition,message=message)


    def goto_tool_status_page(self,toolname):
        """
        navigate to the tool's contribtool status page
        """

        po = self.catalog.load_pageobject('ToolsPipelinePage')
        po.goto_page()
        po.search_for(toolname)

        row = None
        for row in po.search_result_rows():
            if row.value()['alias'] == toolname:
                row.goto_title()
                break
        else:
            raise NavigationError('while navigating to tool status page,'\
                                  + ' tool is not registered: %s' % (toolname))


    def plan(self,end_state,toolname,tooldata,codedata,adminuser,adminpass,username,userpass):
        """
        take a tool from its current state to the provided state
        using the provided tooldata, source code, admin and user
        account information
        """

        states = { 'none'       : { 'fxn' : None,
                                    'args' : None,
                                    'next' : 'created',
                                  },
                   'created'    : { 'fxn' : self.register,
                                    'args' : (toolname,tooldata),
                                    'next' : 'uploaded',
                                  },
                   'uploaded'   : { 'fxn' : self.upload,
                                    'args' : (toolname,codedata,username,userpass),
                                    'next' : 'installed',
                                  },
                   'installed'  : { 'fxn' : self.install,
                                    'args' : (toolname,adminuser,adminpass),
                                    'next' : 'approved',
                                  },
                   'approved'   : { 'fxn' : self.approve,
                                    'args' : (toolname,username,userpass),
                                    'next' : 'published',
                                  },
                   'published'  : { 'fxn' : self.publish,
                                    'args' : (toolname,adminuser,adminpass),
                                    'next' : 'updated',
                                  },
                   'updated'    : { 'fxn' : self.updated,
                                    'args' : (toolname,username,userpass),
                                    'next' : 'installed',
                                  },
                 }

        if end_state not in states:
            raise ValueError('invalid end state: %s' % (end_state))

        try:
            self.goto_tool_status_page(toolname)
            po = self.catalog.load_pageobject('ToolsStatusRegisteredPage')
            cur_state = po.get_tool_state().lower()
        except NavigationError:
            cur_state = 'none'

        while cur_state != end_state:
            next_state = state['next']
            state = states[next_state]

            state['fxn'](*state['args'])

            last_state = cur_state
            cur_state = po.get_tool_state().lower()
            assert cur_state == next_state, \
                "unexpected state change from %s to %s" % (last_state,next_state)


#    def process_tools(self,statuses,adminuser,adminpass,username,userpass):
#        """
#        create, install, or publish tools with a status that matching one of those
#        in the statuses parameter
#
#        ex:
#        statuses = ['registered','updated','uploaded','approved']
#        """
#
#        # go to the tools pipeline page
#        po = self.catalog.load_pageobject('ToolsPipelinePage')
#        po.goto_page()
#        po.form.search_results.display_limit('1000')
#
#        # get all tool aliases matching statuses
#        alias_lists = po.form.get_aliases_by_status(statuses)
#
#
#        #         current state.........then do...
#        states = { 'registered' : { 'fxn'  : self.create,
#                                    'args' : (toolname),
#                                  },
#                   'uploaded'   : { 'fxn'  : self.install,
#                                    'args' : (toolname,adminuser,adminpass),
#                                  },
#                   'approved'   : { 'fxn'  : self.publish,
#                                    'args' : (toolname),
#                                  },
#                   'updated'    : { 'fxn'  : self.install,
#                                    'args' : (toolname,adminuser,adminpass),
#                                  },
#                 }
#
#        for (status,toolnames) in alias_list.items():
#            for toolname in toolnames:
#                states[status]['fxn'](*states[status]['args'])


    def register(self,toolname,data):
        """
        register a tool as the tool submitter
        """

        self.logger.info("registering the tool '%s'" % (toolname))

        po = self.catalog.load_pageobject('ToolsCreatePage')
        po.goto_page()

        # fill in and submit the tool create page
        po.populate_form(data)
        po.submit_form()

        # upon successful tool registration,
        # users are taken to the registered or created page
        po = self.catalog.load_pageobject(
                'ToolsStatusRegisteredPage', toolname)

        # the page should have a system message explaining
        # the tool was successfully registered
        try:
            message = po.get_system_message()
        except Exception as e:
            try:
                message = po.get_error_info()
            except:
                raise e
            else:
                raise FormSubmissionError(' '.join(message))


        # if message is None, there was probably an error
        # message should say 'Tool information successfully registered'
        return message


    def create(self,toolname):

        self.logger.info("adding tool repository for '%s'" % (toolname))

        po = self.catalog.load_pageobject(
                'ToolsStatusRegisteredAdminPage',toolname)
        po.goto_page()

        # click the addrepo link
        addrepo_status,output = po.do_addrepo()

        # wait for the output success / failure block to appear
        if addrepo_status is False:
            raise RuntimeError("addrepo failed: %s" % (output))

        # mark project as created
        self.flip_tool_status('ToolsStatusRegisteredAdminPage',toolname,'Created')

        # check that the tool is in the created state
        tool_state = po.get_tool_state()
        if tool_state.lower() != 'Created'.lower():
            raise Exception('Incorrect tool state: %s, expected "Created"'\
                % tool_state)


    def checkout_repository(self,toolname,username,userpass):
        """
        checkout the repository to see if it exists and is accessible.
        """

        self.logger.info("checking out repository for the tool '%s'" \
            % (toolname))

        repo_url = self.repo_url_template % { 'hubname'  : self.hubname,
                                              'toolname' : toolname }

        # ssh into a tool session container
        cm = ContainerManager()
        ws = cm.access(host=self.hubname,username=username,password=userpass)

        svn = Subversion(ws,username,userpass)

        session_number = -1
        repo_home = None
        try:
            session_number,es = ws.execute('echo $SESSION')
            if session_number <= 0:
                raise RuntimeError('invalid session number: %s' \
                    % (session_number))

            # create a temp directory to hold the repo
            repo_home,es = ws.execute('mktemp -d --tmpdir=`pwd` -t tmp.XXXXXXXX')
            ws.execute('cd %s' % (repo_home))

            # do the checkout
            svn.checkout(repo_url,toolname)

            # cd into the repo
            ws.execute('cd %s' % (toolname))
            tool_repo,es = ws.execute('pwd')

        finally:
            # FIXME: remove the temp directory
            ws.send_raw('')
            ws.send_raw('')
            time.sleep(5)
            if repo_home is not None:
                ws.execute('rm -rf %s' % (repo_home))

            # shut down the ssh connection
            ws.close()


    def upload(self,toolname,data,username,userpass):
        """
        upload source code into the source code repository

        data is a dictionary that links files on the local file system
        to a path relative to the checked out svn repository.

        example:
        data = {
            '/home/hubzero/testuser/main.c'      : 'src/main.c',
            '/home/hubzero/testuser/Makefile'    : 'src/Makefile',
            '/home/hubzero/testuser/tool.xml'    : 'rappture/tool.xml',
        }
        """

        msg = 'initial upload of source code'
        self.upload_code(toolname,data,username,userpass,msg)

        # navigate to the tool status page
        po = self.catalog.load_pageobject('ToolsStatusCreatedPage',toolname)
        po.goto_page()

        # on web page, mark project as uploaded
        po.flip_status_to_uploaded()

        self.__wait_for_tool_state(po,'Uploaded')


    def upload_code(self,toolname,data,username,userpass,msg):
        """
        upload source code into the source code repository

        data is a dictionary that links files on the local file system
        to a path relative to the checked out svn repository.

        example:
        data = {
            '/home/hubzero/testuser/main.c'      : 'src/main.c',
            '/home/hubzero/testuser/Makefile'    : 'src/Makefile',
            '/home/hubzero/testuser/tool.xml'    : 'rappture/tool.xml',
        }
        """

        self.logger.info("uploading source code for the tool '%s'" \
            % (toolname))

        repo_url = self.repo_url_template % { 'hubname'  : self.hubname,
                                              'toolname' : toolname }

        # ssh into a tool session container
        cm = ContainerManager()
        ws = cm.access(host=self.hubname,username=username,password=userpass)

        svn = Subversion(ws,username,userpass)

        session_number = -1
        repo_home = None
        try:
            session_number,es = ws.execute('echo $SESSION')
            if session_number <= 0:
                raise RuntimeError('invalid session number: %s' \
                    % (session_number))

            # create a temp directory to hold the repo
            repo_home,es = ws.execute('mktemp -d --tmpdir=`pwd` -t tmp.XXXXXXXX')
            ws.execute('cd %s' % (repo_home))

            # do the checkout
            svn.checkout(repo_url,toolname)

            # cd into the repo
            ws.execute('cd %s' % (toolname))
            tool_repo,es = ws.execute('pwd')

            # add some code
            commit_files = []
            for localpath,remotepath in data.items():
                commit_files.append(remotepath)
                remotepath = os.path.join(tool_repo,remotepath)
                ws.importfile(localpath,remotepath)

            # commit the source code repository
            svn.add(commit_files)
            revision = svn.commit("initial upload of source code")
            if revision is None:
                raise RuntimeError('commit failure, revision is None')

        finally:
            # FIXME: remove the temp directory
            ws.send_raw('')
            ws.send_raw('')
            time.sleep(5)
            if repo_home is not None:
                ws.execute('rm -rf %s' % (repo_home))

            # shut down the ssh connection
            ws.close()


    def update(self,toolname,username,userpass):
        """
        update the svn repository with a change so the tool can be installed

        in this case we update the invoke script because all
        tools should have one. we change a predetermined line
        starting with '# hc contribtool update: DATE'
        Where the term DATE is replaced with a date time stamp
        """

        self.logger.info("updating svn repository for the tool '%s'" \
            % (toolname))

        repo_url = self.repo_url_template % { 'hubname'  : self.hubname,
                                              'toolname' : toolname }

        # ssh into a tool session container
        cm = ContainerManager()
        ws = cm.access(host=self.hubname,username=username,password=userpass)

        svn = Subversion(ws,username,userpass)

        session_number = -1
        repo_home = None
        try:
            session_number,es = ws.execute('echo $SESSION')
            if session_number <= 0:
                raise RuntimeError('invalid session number: %s' \
                    % (session_number))

            # create a temp directory to hold the repo
            repo_home,es = ws.execute('mktemp -d --tmpdir=`pwd` -t tmp.XXXXXXXX')
            ws.execute('cd %s' % (repo_home))

            # do the checkout
            svn.checkout(repo_url,toolname)

            # cd into the repo
            ws.execute('cd %s' % (toolname))
            tool_repo,es = ws.execute('pwd')

            # add the marker to the invoke script if it does not exist
            script_path = 'middleware/invoke'
            script_data = ws.read_file(script_path)
            if re.search(self.update_marker,script_data) is None:
                # file doesn't have the marker, add it
                script_data += '\n%sDATE' % (self.update_marker)

            # update the marker with the current date time stamp
            dts = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
            pattern = self.update_marker + '.*'
            replace = self.update_marker + dts
            script_data = re.sub(pattern,replace,script_data)

            # write the change back to the disk
            ws.write_file(script_path,script_data)

            # commit the changed file back to the source code repository
            revision = svn.commit("updating the invoke script")
            if revision is None:
                raise RuntimeError('commit failure, revision is None')

        finally:
            # FIXME: remove the temp directory
            ws.send_raw('')
            ws.send_raw('')
            time.sleep(5)
            if repo_home is not None:
                ws.execute('rm -rf %s' % (repo_home))

            # shut down the ssh connection
            ws.close()

        # navigate to the tool status page
        po = self.catalog.load_pageobject('ToolsStatusInstalledPage',toolname)
        po.goto_page()

        # on web page, mark project as updated
        po.flip_status_to_updated()

        self.__wait_for_tool_state(po,'Updated')


    def install(self,toolname,adminuser,adminpass):
        """
        install the tool as a tool manager
        """

        self.logger.info("installing the tool '%s'" % (toolname))

        self.push_admin_install_button(toolname)

        self.compile_code(toolname,adminuser,adminpass)

        self.flip_tool_status('ToolsStatusUploadedAdminPage',toolname,'Installed')


    def flip_tool_status(self,po_type,toolname,status):
        """
        flip the status of a tool
        """

        # navigate to the tool status page as a tool manager
        po = self.catalog.load_pageobject(po_type,toolname)
        po.goto_page()

        # flip the status from uploaded to installed
        po.submit_form({'status' : status})

        self.__wait_for_tool_state(po,status)


    def push_admin_install_button(self,toolname):
        """
        push the install button under admin controls on a tool's status page
        """

        self.logger.info("clicking install link for tool '%s'" % (toolname))

        # navigate to the tool status page as a tool manager
        # press the install link
        po = self.catalog.load_pageobject('ToolsStatusUploadedAdminPage',toolname)
        po.goto_page()
        checkout_status,output = po.do_install()

        # wait for the output success / failure block to appear
        if checkout_status is False:
            raise RuntimeError("checkout failed: %s" % (output))

        # FIXME: add function to get the passed/failed message


    def compile_code(self,toolname,adminuser,adminpass):
        """
        ssh into a tool session container as a tool manager,
        compile a tool's source code, and install the binaries
        """

        # ssh into a tool session container as the tools manager
        # compile and install the code

        # get into a tool session container.
        cm = ContainerManager()
        ws = cm.access(host=self.hubname,username=adminuser,password=adminpass)

        session_number,es = ws.execute('echo $SESSION')

        # catch errors that happen in the shell
        # so we can properly exit and close the workspace
        try:
            # become the apps user
            ws.send('sudo su - apps')
            ws.start_bash_shell()
            output,es = ws.execute('whoami')
            exit_apps = True
            if output != 'apps':
                exit_apps = False
                msg = "doesn't look like we were able to become the apps user"
                self.logger.error(msg)
                raise Exception(msg)

            # catch compile and install errors
            # so we can report them back to the developer

            # navigate to the tool directory
            cmd = 'cd /apps/%(toolname)s/dev/src' \
                    % { 'toolname' : toolname, }
            ws.execute(cmd)

            # if there is a makefile available
            # run:
            # make clean
            # make all
            # make install
            # don't fail if there is no clean or all targets
            if ws.bash_test('-e Makefile'):
                # allow 30 minutes for the code to compile
                ws.timeout = 1800
                output,es = ws.execute('make clean',False)
                output,es = ws.execute('make all',False)
                no_make_all_text = "make: *** No rule to make target `all'.  Stop."
                if es > 0:
                    if es == 2 and output == no_make_all_text:
                        output,es = ws.execute('make')
                    else:
                        self.logger.exception(output)
                        raise ExitCodeError(output)
                output,es = ws.execute('make install')
                ws.timeout = 10
            else:
                msg = "No Makefile found"
                print msg
                self.logger.info(msg)

        finally:
            # exit sudo
            ws.stop_bash_shell()
            if exit_apps:
                ws.send('exit')

            # shut down the ssh connection
            ws.close()


    def launch(self,toolname,username,userpass):
        """
        test launching the tool as the tool submitter
        """

        self.logger.info("test launching the tool '%s'" % (toolname))

        # try launching the tool
        po = self.catalog.load_pageobject('ToolsStatusInstalledPage',toolname)
        po.goto_page()
        po.goto_launch_tool()

        # check if a new tool session was started
        self.logger.info("checking if new tool session was started")

        po = self.catalog.load_pageobject('ToolSessionPage')
        session_number = po.get_session_number()

        session = ToolSession(host=self.hubname,
                              username=username,
                              password=userpass)
        session_data = session.get_open_session_detail()

        has_session = False
        for session_info in session_data.values():
            if int(session_info['session_number']) == int(session_number):
                has_session = True
                self.logger.info("Found session %s in user's session list" \
                    % session_number)
                break

        if not has_session:
            raise Exception('session #%s does not appear to be open' \
                % (session_number))

        ws = session.access(session_number)
        snum,es = ws.execute('echo $SESSION')
        if session_number != int(snum):
            # we are not in the correct session
            raise Exception("ssh'ing into session #%s failed: %s" \
                % (session_number,snum))

        # look for the tool to be running
        output = ''
        cmd = 'ps aux | grep /apps/%s/.*/middleware/invoke | grep -v grep'\
            % (toolname)

        output,es = ws.execute(cmd,fail_on_exit_code=False)
        ws.close()

        # close the tool
        session.stop(session_number)


        if es != 0:
            self.logger.error(output)
            raise Exception(output)


    def edit_tool_page(self,toolname,data):
        """
        update the tool info page
        """

        self.logger.info("editing the tool information page for '%s'" \
                            % (toolname))

        # navigate to the resource page edit forms
        po = self.catalog.load_pageobject('ToolsStatusInstalledPage',toolname)
        po.goto_page()
        po.goto_toolinfo_toolpage_edit()


        # generate a data dictionary for the tool description
        form_data = {}
        # fields = ['title','description','abstract','bio','credits', \
        #           'citations', 'sponsoredby','references','publications']
        fields = ['title','description','abstract']
        for field in fields:
            try:
                form_data.update({field:data[field]})
            except KeyError:
                pass

        # fill out the description form
        po = self.catalog.load_pageobject('ResourcesToolDescriptionPage',toolname)

        po.form.populate_form(form_data)

        po.form.submit.click()


        # check for error after submitting the form
        # FIXME: add error checking


        # add contributors to the resource page
        po = self.catalog.load_pageobject('ResourcesToolContributorsPage',toolname)

        if data['contributors'] is not None:
            # remove all authors so we can repopulate it
            # with provided contributors
            for author in po.form.authorlist.get_authors():
                po.form.authorlist.delete_author(author)

            # generate our new author list
            authors = [c['username'] for c in data['contributors']]

            if len(authors) > 0:

                # fill in the authors
                po.form.authorform.submit_form({'author' : authors})

                # check for error after submitting the form
                # FIXME: add error checking


                # update the author's organization and role
                for c in data['contributors']:

                    if (c.has_key('firstname') and c['firstname'] and
                        c.has_key('lastname') and c['lastname']):
                        name = "{0} {1}".format(c['firstname'],c['lastname'])
                        self.logger.info('adding contributor: {0}'.format(name))
                    else:
                        self.logger.info(
                            "skipping author '%s': missing firstname or lastname" \
                            % (c['username']))
                        next

                    if c.has_key('role') and c['role']:
                        po.form.authorlist.author_role(name,c['role'])

                    if c.has_key('organization') and c['organization']:
                        po.form.authorlist.author_organization(
                            name,c['organization'])

                    # check for error after submitting the form
                    # FIXME: add error checking

        po.form.submit.click()

        # add documents and screenshots to the resource page
        po = self.catalog.load_pageobject('ResourcesToolAttachmentsPage',toolname)

        if data['supportingdocs'] is not None:
            # remove all supporting docs so we can repopulate it
            for filename in po.form.documents.get_uploaded_files():
                po.form.documents.delete_file(filename)

            # upload the supporting documents
            po.form.documents.value(data['supportingdocs'])

            # check for error after uploading the documents
            # FIXME: add error checking


        if data['screenshots'] is not None:
            # remove all supporting docs so we can repopulate it
            for filename in po.form.screenshots.get_uploaded_files():
                po.form.screenshots.delete_file(filename)

            # upload the screenshots
            # we don't handle the screenshot title
            po.form.screenshots.value(data['screenshots'])

            # check for error after uploading the documents
            # FIXME: add error checking


        po.form.submit.click()


        # populate the tags for the tool resource page
        po = self.catalog.load_pageobject('ResourcesToolTagsPage',toolname)

        if data['tags'] is not None:
            po.form.populate_form({'tags':data['tags']})

        po.form.submit.click()


        # check for error after submitting the form
        # FIXME: add error checking


        # finalize tool resource page
        po = self.catalog.load_pageobject('ResourcesToolFinalizePage',toolname)

        po.form.submit.click()


        # check for error after submitting the form
        # FIXME: add error checking


    def approve(self,toolname,data):
        """
        update the version info and flip the status of an installed tool
        """

        self.logger.info("approving the tool '%s'" % (toolname))

        po = self.catalog.load_pageobject('ToolsStatusInstalledPage',toolname)
        po.goto_page()

        # click the approve link
        po.flip_status_to_approved()


        po = self.catalog.load_pageobject('ToolsStatusApproveConfirmVersionPage',toolname)

        # check for error on page
        err = po.get_error_info()
        if err:
            # update the version information
            old_version = po.version_form.version.value
            new_version = str(float(old_version) + 0.01)
            po.version_form.submit_form({'version':new_version})

            # check for error on page
            err = po.get_error_info()
            if err:
                raise RuntimeError('error found on page: %s' % (err))

            # check for the success message
            ok = po.get_success_info()
            if not ok:
                raise RuntimeError('missing success message after updating version')

            # click the approve link again ?!?
            po = self.catalog.load_pageobject('ToolsStatusInstalledPage',toolname)
            po.flip_status_to_approved()

        # confirm the version
        po = self.catalog.load_pageobject('ToolsStatusApproveConfirmVersionPage',toolname)
        po.version_form.submit_form()

        # confirm the license
        po = self.catalog.load_pageobject('ToolsStatusApproveConfirmLicensePage',toolname)
        po.submit_form(data)

        # check for error on page
        err = po.get_error_info()
        if err:
            raise RuntimeError('error found on page: %s' % (err))

        # confirm the tool info
        po = self.catalog.load_pageobject('ToolsStatusApproveConfirmToolInfoPage',toolname)
        po.approve_tool()

        # check for the success message
        po = self.catalog.load_pageobject('ToolsStatusApprovedPage',toolname)
        ok = po.get_success_info()
        if not ok:
            raise RuntimeError('missing success message after approving tool info')


    def publish(self,toolname):
        """
        press the publish button in the admin controls of the tool's status page
        """

        self.logger.info("publishing '%s'" % (toolname))

        po = self.catalog.load_pageobject('ToolsStatusApprovedAdminPage',toolname)
        po.goto_page()

        # click the publish link
        publish_status,output = po.do_publish()

        # wait for the output success / failure block to appear
        if publish_status is False:
            raise RuntimeError("finalizetool failed: %s" % (output))

        # mark project as created
        self.flip_tool_status('ToolsStatusApprovedAdminPage',toolname,'Published')

        # check that the tool is in the published state
        tool_state = po.get_tool_state()
        if tool_state.lower() != 'Published'.lower():
            raise Exception('Incorrect tool state: %s, expected "Published"'\
                % tool_state)

