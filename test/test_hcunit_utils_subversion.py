import pytest
import hubcheck
import json
import time
import os
from hubcheck.actionobjects.contribtool import Subversion


pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_nightly,
               pytest.mark.hcunit_utils_subversion,
             ]

TMP_FNAME = 't_%s' % (str(int(time.time())))

TOOLNAME = 'hutt'
toolconfigfile = os.path.join(hubcheck.conf.settings.data_dir,
                              TOOLNAME,TOOLNAME+'.json')
with open(toolconfigfile,"r") as f:
    toolconfig = json.load(f)


class TestHCUnitUtilsSubversion(hubcheck.testcase.TestCase2):

    def setup_method(self,method):

        # get user account info
        self.hubname = self.testdata.find_url_for('https')
        self.username,self.userpass = \
            self.testdata.find_account_for('registeredworkspace')

        cm = hubcheck.shell.ContainerManager()
        self.ws = cm.access(host=self.hubname,
                            username=self.username,
                            password=self.userpass)

        self.repo_url_template = 'https://%(hubname)s/tools/%(toolname)s/svn/trunk'
        self.repo_url = self.repo_url_template % {
                            'hubname'  : self.hubname,
                            'toolname' : TOOLNAME,
                        }


    def teardown_method(self,method):

        self.ws.execute('cd')
        self.ws.execute('rm -rf ./%s' % (TOOLNAME))

        self.ws.close()


    def test_checkout(self):
        """
        try checking out a tool
        """

        repo = Subversion(self.ws,self.username,self.userpass)

        revision = repo.checkout(self.repo_url,TOOLNAME)

        assert revision is not None,\
            "checkout failed, returned revision == None"



#    def test_checkout_bad_password(self):
#        """
#        try checking out a tool with a bad password
#        """
#
#        repo = Subversion(self.ws,self.username,'bad_password')
#
#        with pytest.raises(RuntimeError):
#            revision = repo.checkout(self.repo_url,TOOLNAME)
#            self.ws.execute('rm -rf ./%s' % (TOOLNAME))
#
#
#    def test_checkout_not_authorized(self):
#        """
#        try checking out a tool the user is not authorized to checkout
#        """
#
#        toolname = 'workspace'
#
#        repo_url = self.repo_url_template % {
#                        'hubname'  : self.hubname,
#                        'toolname' : toolname,
#                   }
#
#        repo = Subversion(self.ws,self.username,self.userpass)
#
#        with pytest.raises(RuntimeError):
#            revision = repo.checkout(repo_url,toolname)
#            self.ws.execute('rm -rf ./%s' % (toolname))


    def test_add(self):
        """
        try adding files to a repository
        """

        repo = Subversion(self.ws,self.username,self.userpass)
        repo.checkout(self.repo_url,TOOLNAME)
        self.ws.execute('cd %s' % (TOOLNAME))
        self.ws.execute('echo hi > doc/%s' % (TMP_FNAME))
        repo.add(['doc/%s' % (TMP_FNAME)])


    def test_remove(self):
        """
        try remove files to a repository
        """

        repo = Subversion(self.ws,self.username,self.userpass)
        repo.checkout(self.repo_url,TOOLNAME)
        self.ws.execute('cd %s' % (TOOLNAME))
        repo.remove(['middleware/invoke'])


    def test_commit_success(self):
        """
        try committing files to a repository
        """

        repo = Subversion(self.ws,self.username,self.userpass)
        repo.checkout(self.repo_url,TOOLNAME)
        self.ws.execute('cd %s' % (TOOLNAME))
        self.ws.execute('echo hi > doc/%s' % (TMP_FNAME))
        repo.add(['doc/%s' % (TMP_FNAME)])
        revision = repo.commit("testing hubcheck's svn commit: adding file")
        assert revision is not None
        repo.remove(['doc/%s' % (TMP_FNAME)])
        repo.commit("testing hubcheck's svn commit: removing file")
        assert revision is not None


    def test_commit_failure(self):
        """
        try committing files to a repository when no new files were added
        """

        repo = Subversion(self.ws,self.username,self.userpass)
        repo.checkout(self.repo_url,TOOLNAME)
        self.ws.execute('cd %s' % (TOOLNAME))
        revision = repo.commit("testing hubcheck's svn commit: no files added")
        assert revision is None


