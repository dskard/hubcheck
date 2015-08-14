from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Text
from hubcheck.pageobjects.basepageelement import TextAC
from hubcheck.pageobjects.basepageelement import TextArea

from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class GroupsNewForm1(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsNewForm1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsNewForm_Locators = self.load_class('GroupsNewForm_Locators')
        WikiTextArea = self.load_class('WikiTextArea')

        # update this object's locator with defaults
        self.locators.update(GroupsNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.groupid        = Text(self,{'base':'groupid'})
        self.title          = Text(self,{'base':'title'})
        self.tags           = TextAC(self,{'base':'tags',
                                           'aclocatorid':'tagsac',
                                           'choicelocatorid':'tagsacchoices',
                                           'tokenlocatorid':'tagsactoken',
                                           'deletelocatorid':'tagsacdelete'})
        self.public_desc    = WikiTextArea(self,
                                {'base'     : 'public_desc',
                                 'textarea' : 'public_desc_ta',
                                 'toolbar'  : 'public_desc_tb'})
        self.private_desc   = WikiTextArea(self,
                                {'base'     : 'private_desc',
                                 'textarea' : 'private_desc_ta',
                                 'toolbar'  : 'private_desc_tb'})
        self.join_policy    = Radio(self,{'Anyone'      : 'join_anyone',
                                          'Restricted'  : 'join_restricted',
                                          'Invite Only' : 'join_invite',
                                          'Closed'      : 'join_closed'})
        self.restrict_msg   = TextArea(self,{'base':'restrict_msg'})
        self.privacy        = Radio(self,{'Visible' : 'privacy_visible',
                                          'Hidden'  : 'privacy_hidden'})

        self.fields += ['groupid','title','tags','public_desc','private_desc',
                        'join_policy','restrict_msg','privacy']

        # update the component's locators with this objects overrides
        self._updateLocators()

    def create_group(self, data):
        """create a new group, filling in the data as provided"""

        self.submit_form(data)

class GroupsNewForm1_Locators_Base(object):
    """locators for GroupsNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#group_cn_field",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'public_desc'       : "css=#hubForm label[for='public_desc']",
        'public_desc_ta'    : "css=#hubForm label[for='public_desc'] .wiki-toolbar-content",
        'public_desc_tb'    : "css=#hubForm label[for='public_desc'] .wiki-toolbar",
        'private_desc'      : "css=#hubForm label[for='private_desc']",
        'private_desc_ta'   : "css=#hubForm label[for='private_desc'] .wiki-toolbar-content",
        'private_desc_tb'   : "css=#hubForm label[for='private_desc'] .wiki-toolbar",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='privacy'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='privacy'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }

class GroupsNewForm1_Locators_Base_2(object):
    """locators for GroupsNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#hubForm [name='cn']",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'public_desc'       : "css=#hubForm label[for='public_desc']",
        'public_desc_ta'    : "css=#hubForm label[for='public_desc'] .wiki-toolbar-content",
        'public_desc_tb'    : "css=#hubForm label[for='public_desc'] .wiki-toolbar",
        'private_desc'      : "css=#hubForm label[for='private_desc']",
        'private_desc_ta'   : "css=#hubForm label[for='private_desc'] .wiki-toolbar-content",
        'private_desc_tb'   : "css=#hubForm label[for='private_desc'] .wiki-toolbar",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='privacy'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='privacy'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }

class GroupsNewForm1_Locators_Base_3(object):
    """locators for GroupsNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#group_cn_field",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'public_desc'       : "css=#hubForm label[for='public_desc']",
        'public_desc_ta'    : "css=#public_desc",
        'public_desc_tb'    : "css=#wiki-toolbar-public_desc",
        'private_desc'      : "css=#hubForm label[for='private_desc']",
        'private_desc_ta'   : "css=#private_desc",
        'private_desc_tb'   : "css=#wiki-toolbar-private_desc",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='discoverability'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='discoverability'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }


class GroupsNewForm1_Locators_Base_4(object):
    """locators for GroupsNewForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#group_cn_field",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'public_desc'       : "css=#hubForm label[for='public_desc']",
        'public_desc_ta'    : "css=#wykiwyg-editor",
        'public_desc_tb'    : "css=#hubForm label[for='public_desc'] .wykiwyg-header",
        'private_desc'      : "css=#hubForm label[for='private_desc']",
        'private_desc_ta'   : "css=#wykiwyg-editor",
        'private_desc_tb'   : "css=#hubForm label[for='private_desc'] .wykiwyg-header",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='privacy'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='privacy'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }


class GroupsNewForm1_Locators_Base_5(object):
    """locators for GroupsNewForm1 object
       uses updates to GroupsNewForm1_Locators_Base_3's
       privacy_visibility and privacy_hidden locators
       these locators were used sometime before hubzero
       version 1.1.5
    """

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#group_cn_field",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'public_desc'       : "css=#hubForm label[for='public_desc']",
        'public_desc_ta'    : "css=#public_desc",
        'public_desc_tb'    : "css=#wiki-toolbar-public_desc",
        'private_desc'      : "css=#hubForm label[for='private_desc']",
        'private_desc_ta'   : "css=#private_desc",
        'private_desc_tb'   : "css=#wiki-toolbar-private_desc",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='privacy'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='privacy'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }


class GroupsNewForm2(FormBase):
    """
    Updating public_desc and private_desc to use IframeWrap
    This version is used on hubs with the fancy wiki editor plugin.
    """

    # GroupsNewForm1 probably used to do this but I've been cleaning up
    # the WikiTextArea and WikiIframe... objects. I think it is better
    # to keep the two instances of the object different.

    def __init__(self, owner, locatordict={}):
        super(GroupsNewForm2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsNewForm_Locators = self.load_class('GroupsNewForm_Locators')
        # WikiTextArea = self.load_class('WikiTextArea')

        # update this object's locator with defaults
        self.locators.update(GroupsNewForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.groupid        = Text(self,{'base':'groupid'})
        self.title          = Text(self,{'base':'title'})
        self.tags           = TextAC(self,{'base':'tags',
                                           'aclocatorid':'tagsac',
                                           'choicelocatorid':'tagsacchoices',
                                           'tokenlocatorid':'tagsactoken',
                                           'deletelocatorid':'tagsacdelete'})
        self.public_desc    = IframeWrap(TextArea(self,{'base':'publicdesctext'}),
                                         ['publicdescframe'])
        self.private_desc   = IframeWrap(TextArea(self,{'base':'privatedesctext'}),
                                         ['privatedescframe'])
        self.join_policy    = Radio(self,{'Anyone'      : 'join_anyone',
                                          'Restricted'  : 'join_restricted',
                                          'Invite Only' : 'join_invite',
                                          'Closed'      : 'join_closed'})
        self.restrict_msg   = TextArea(self,{'base':'restrict_msg'})
        self.privacy        = Radio(self,{'Visible' : 'privacy_visible',
                                          'Hidden'  : 'privacy_hidden'})

        self.fields += ['groupid','title','tags','public_desc','private_desc',
                        'join_policy','restrict_msg','privacy']

        # update the component's locators with this objects overrides
        self._updateLocators()

    def create_group(self, data):
        """create a new group, filling in the data as provided"""

        self.submit_form(data)


class GroupsNewForm2_Locators_Base_1(object):
    """
    locators for GroupsNewForm2 object
    """

    locators = {
        'base'              : "css=#hubForm",
        'groupid'           : "css=#group_cn_field",
        'title'             : "css=#hubForm [name='description']",
        'tags'              : "css=#actags",
        'tagsac'            : "css=#token-input-actags",
        'tagsacchoices'     : "css=.token-input-dropdown-act",
        'tagsactoken'       : "css=.token-input-token-act",
        'tagsacdelete'      : "css=.token-input-delete-token-act",
        'publicdescframe'   : "css=#hubForm label[for='public_desc'] iframe",
        'publicdesctext'    : "css=body",
        'privatedescframe'  : "css=#hubForm label[for='private_desc'] iframe",
        'privatedesctext'   : "css=body",
        'join_anyone'       : "css=#hubForm [name='join_policy'][value='0']",
        'join_restricted'   : "css=#hubForm [name='join_policy'][value='1']",
        'join_invite'       : "css=#hubForm [name='join_policy'][value='2']",
        'join_closed'       : "css=#hubForm [name='join_policy'][value='3']",
        'privacy_visible'   : "css=#hubForm [name='discoverability'][value='0']",
        'privacy_hidden'    : "css=#hubForm [name='discoverability'][value='1']",
        'restrict_msg'      : "css=#hubForm [name='restrict_msg']",
        'submit'            : "css=#hubForm [type='submit']",
    }


