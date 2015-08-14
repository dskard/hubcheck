import json
import hashlib
import StringIO
import pyppp
import logging
import string

from .crypto import encrypt_file, decrypt_file

class AdminProperties(object):
    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.groups = {}
        self.supportacl = {
            'tickets_read' : False,
            'tickets_update' : False,
            'tickets_delete' : False,
            'comments_create' : False,
            'comments_read' : False,
            'private_comments_create' : False,
            'private_comments_read' : False,
        }

    def update_groups(self,name,role):
        self.groups.update({name:role})

    def delete_groups(self,name):
        if name in self.groups:
            del self.groups[name]

    def load(self,data):
        self.groups.update(data['groups'])
        # some accounts don't have this info,
        # don't fail if it doesn't exist
        if 'supportacl' in data:
            self.supportacl.update(data['supportacl'])

    def as_dict(self):
        return {'groups' : self.groups, 'supportacl' : self.supportacl}


class UserData(object):

    def __init__(self,data=None):

        self.logger = logging.getLogger(__name__)

        self.firstname = ''
        self.middlename = ''
        self.lastname = ''
        self.username = ''
        self.password = ''
        self.old_password = ''
        self.email = ''
        self.admin_properties = None

        if data is not None:
            self.load(data)


    def load(self,data):
        self.firstname = data['firstname']
        self.middlename = data['middlename']
        self.lastname = data['lastname']
        self.username = data['username']
        self.password = data['password']
        if 'old_password' in data:
            self.old_password = data['old_password']
        self.email = data['email']
        self.admin_properties = AdminProperties()
        if 'admin-properties' in data.keys():
            self.admin_properties.load(data['admin-properties'])


    def as_dict(self):
        return {
            'firstname' : self.firstname,
            'middlename' : self.middlename,
            'lastname' : self.lastname,
            'username' : self.username,
            'password' : self.password,
            'old_password' : self.old_password,
            'email' : self.email,
            'admin-properties' : self.admin_properties.as_dict(),
        }


    def update_password(self,new_password=None):
        self.logger.info('updating testdata password for %s' % (self.username))
        if new_password is None:
            while True:
                p = pyppp.PyPPP()
                p.generate_random_sequence_key()
                new_password = ''.join(p.retrieve_passcodes(0,3))

                # check that new_password has at least one digit
                if any((c in string.digits) for c in new_password):
                    # has digits
                    # check that new_password has at least one symbol
                    if any((c in string.punctuation) for c in new_password):
                        # has symbol
                        break
                    else:
                        # missing symbol
                        pass
                else:
                    # missing digits
                    pass

        self.old_password = self.password
        self.password = new_password

    def undo_update_password(self):
        self.logger.info('undo\'ing testdata password update for %s'
            % (self.username))
        self.password = self.old_password
        self.old_password = ''

class UserTypes(object):

    def __init__(self,data=None):

        self.logger = logging.getLogger(__name__)

        self.usertypes = {
            "registeredworkspace"   : "",
            "networkworkspace"      : "",
            "purdueworkspace"       : "",
            "appsworkspace"         : "",
            "rappturecompile"       : "",
            "wishsubmitter"         : "",
            "submituser"            : "",
            "citationsubmitter"     : "",
            "hubumanager"           : "",
            "hubumember"            : "",
            "webdavuser"            : "",
            "ticketsubmitter"       : "",
            "ticketmanager"         : "",
            "timesubmitter"         : "",
            "groupmanager"          : "",
            "groupmember"           : "",
            "toolsubmitter"         : "",
        }

        if data is not None:
            self.load(data)

    def load(self,data):
        self.usertypes.update(data)

    def as_dict(self):
        return self.usertypes

class Testdata(object):

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.data = {}

    def encrypt(self,password,indata):
        """indata should be a StringIO object"""
        key = hashlib.sha256(password).digest()
        return encrypt_file(key,indata)

    def encrypt_file(self,password,fname):
        indata = open(fname,'rb')
        return self.encrypt(password,indata)

    def decrypt(self,password,indata):
        """indata should be a StringIO object"""
        key = hashlib.sha256(password).digest()
        return decrypt_file(key,indata)

    def decrypt_file(self,password,fname):
        indata = open(fname,'rb')
        return self.decrypt(password,indata)

    def load (self,fname,password=None):
        indata = open(fname,'rb')
        return self.loads(indata.read(),password)

    def loads(self,s,password=None):
        if password:
            s = StringIO.StringIO(s)
            self.data = json.load(self.decrypt(password,s))
        else:
            self.data = json.loads(s)
        return self

    def save(self,fname,password):
        io = StringIO.StringIO()
        json.dump(self.data,io,indent=4)
        s = self.encrypt(password,io)
        with open(fname,'wb') as outdata:
            outdata.write(s.getvalue())


    # object functions

    def get_userdata_for(self,username):
        self.logger.debug("getting userdata for %s" % (username))
        ud = UserData(self.data['accounts'][username])
        return ud

    def set_userdata_for(self,username,userdata):
        self.logger.debug("setting userdata for %s" % (username))
        self.data['accounts'][username] = userdata.as_dict()

    def get_usertypes(self):
        ut = UserTypes(self.data('users'))
        return ut

    def set_usertypes(self,usertypes):
        self.data['users'] = usertypes.as_dict()


    # user account related functions

    def get_account_info(self,username):
        self.logger.debug("getting account info for %s" % (username))
        if not self.data['accounts'].has_key(username):
            raise ValueError("testdata does not contain account info for %s" \
                                % (username))

        return self.data['accounts'][username]

    def get_usernames(self):
        return self.data['accounts'].keys()

    def update_password(self,username):
        userdata = self.get_account_info()

    def find_account_by_property(self,property):
        self.logger.debug("finding account for property %s" % (property))
        if not self.data.has_key('accounts'):
            raise ValueError('testdata contains no accounts')

        result = None
        for v in self.data['accounts'].values():
            if v.has_key('admin-properties'):
                if v['admin-properties'].has_key(property):
                    result = {
                               'username' : v['username'],
                               'password' : v['password'],
                               property   : v['admin-properties'][property]
                             }
                    break

        return result

    def find_group_manager(self,group):
        if not self.data.has_key('groups'):
            raise ValueError('testdata contains no groups')

        if not self.data['groups'].has_key(group):
            raise ValueError("testdata contains no group named: %s" % group)

        username = self.data['groups'][group]['managers'][0]
        password = self.find_account_password(username)

        return username,password

    def find_course_manager(self,course):
        if not self.data.has_key('courses'):
            raise ValueError('testdata contains no courses')

        if not self.data['courses'].has_key(course):
            raise ValueError("testdata contains no course named: %s" % course)

        username = self.data['courses'][course]['manager']
        password = self.find_account_password(username)

        return username,password

    def find_account_password(self,username):
        if not self.data.has_key('accounts'):
            raise ValueError('testdata contains no accounts')

        if not self.data['accounts'].has_key(username):
            raise ValueError("testdata contains no account: %s" % username)

        result = self.data['accounts'][username]['password']
        return result

    def find_account_email(self,username):
        if not self.data.has_key('accounts'):
            raise ValueError('testdata contains no accounts')

        if not self.data['accounts'].has_key(username):
            raise ValueError("testdata contains no account: %s" % username)

        result = self.data['accounts'][username]['email']
        return result

    def find_account_for(self,usertype):
        self.logger.debug("finding account for %s" % (usertype))

        if not self.data['users'].has_key(usertype):
            raise ValueError("testdata contains no usertype %s" % usertype)

        accountname = self.data['users'][usertype]
        password = self.find_account_password(accountname)

        self.logger.debug("returning account %s" % (accountname))
        return accountname,password

    def find_url_for(self,urltype):
        self.logger.debug("finding url for %s" % (urltype))
        if not self.data.has_key('urls'):
            raise ValueError('testdata contains no url')

        if not self.data['urls'].has_key(urltype):
            raise ValueError("testdata contains no urltype %s" % urltype)

        return self.data['urls'][urltype]

    def find_group_for(self,alias):
        if not self.data.has_key('groups_alias'):
            raise ValueError('testdata contains no groups_alias')

        if not self.data['groups_alias'].has_key(alias):
            raise ValueError("testdata contains no groups alias %s" % alias)

        return self.data['groups_alias'][alias]

    def get_locators(self):
        return self.data['locators']

    def get_hub_version(self):
        return self.data['hub_version']

    def get_tool_container_version(self):
        return self.data['tools']['tool_container_version']

    def get_default_workspace(self):
        return self.data['tools']['default_workspace']

    def get_apps_workspace(self):
        return self.data['tools']['apps_workspace']

    #def acccount_with_properties(self,properties):
    #    for k,v in self.data['accounts']:
    #        if v.has_key('properties'):
    #            for property in properties
    #                if v['properties'].has_key(property):
    #                return k

