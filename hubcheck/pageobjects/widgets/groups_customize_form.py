from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import Radio
from hubcheck.pageobjects.basepageelement import Select

class GroupsCustomizeForm1(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsCustomizeForm1,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsCustomizeForm_Locators = self.load_class('GroupsCustomizeForm_Locators')

        # update this object's locator
        self.locators.update(GroupsCustomizeForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.logo           = Select(self,{'base':'logo'})
        self.content_type   = Radio(self,{'Default Content' : 'default_content',
                                          'Custom Content'  : 'custom_content'})
        self.overview       = Select(self,{'base':'overview'})
        self.members        = Select(self,{'base':'members'})
        self.wiki           = Select(self,{'base':'wiki'})
        self.resources      = Select(self,{'base':'resources'})
        self.discussion     = Select(self,{'base':'discussion'})
        self.messages       = Select(self,{'base':'messages'})
        self.wishlist       = Select(self,{'base':'wishlist'})
        self.blog           = Select(self,{'base':'blog'})
        self.calendar       = Select(self,{'base':'calendar'})

        self.fields += ['logo','content_type','overview','members',
                        'wiki','resources','discussion','messages',
                        'wishlist','blog','calendar']

        self._updateLocators()

class GroupsCustomizeForm1_Locators_Base(object):
    """locators for GroupsCustomizeForm1 object"""

    locators = {
        'base'              : "css=#hubForm",
        'logo'              : "css=#group_logo",
        'default_content'   : "css=#group_overview_type_default",
        'custom_content'    : "css=#group_overview_type_custom",
        'overview'          : "xpath=//span[text()='Overview']/../select",
        'members'           : "xpath=//span[text()='Members']/../select",
        'wiki'              : "xpath=//span[text()='Wiki']/../select",
        'resources'         : "xpath=//span[text()='Resources']/../select",
        'discussion'        : "xpath=//span[text()='Discussion']/../select",
        'messages'          : "xpath=//span[text()='Messages']/../select",
        'wishlist'          : "xpath=//span[text()='Wish List']/../select",
        'blog'              : "xpath=//span[text()='Blog']/../select",
        'calendar'          : "xpath=//span[text()='Calendar']/../select",
        'submit'            : "css=#hubForm [type='submit']",
    }


class GroupsCustomizeForm2(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsCustomizeForm2,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsCustomizeForm_Locators = self.load_class('GroupsCustomizeForm_Locators')

        # update this object's locator
        self.locators = GroupsCustomizeForm_Locators.locators

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.logo           = Select(self,{'base':'logo'})
        self.content_type   = Radio(self,{'Default Content' : 'default_content',
                                          'Custom Content'  : 'custom_content'})
        self.overview       = Select(self,{'base':'overview'})
        self.members        = Select(self,{'base':'members'})
        self.wiki           = Select(self,{'base':'wiki'})
        self.resources      = Select(self,{'base':'resources'})
        self.discussion     = Select(self,{'base':'discussion'})
        self.messages       = Select(self,{'base':'messages'})
        self.wishlist       = Select(self,{'base':'wishlist'})
        self.blog           = Select(self,{'base':'blog'})
        self.calendar       = Select(self,{'base':'calendar'})
        self.usage          = Select(self,{'base':'usage'})
        self.projects       = Select(self,{'base':'projects'})

        self.fields += ['logo','content_type','overview','members',
                        'wiki','resources','discussion','messages',
                        'wishlist','blog','calendar','usage','projects']

        self._updateLocators()

class GroupsCustomizeForm2_Locators_Base(object):
    """locators for GroupsCustomizeForm2 object"""

    locators = {
        'base'              : "css=#hubForm",
        'logo'              : "css=#group_logo",
        'default_content'   : "css=#group_overview_type_default",
        'custom_content'    : "css=#group_overview_type_custom",
        'overview'          : "xpath=//span[text()='Overview']/../select",
        'members'           : "xpath=//span[text()='Members']/../select",
        'wiki'              : "xpath=//span[text()='Wiki']/../select",
        'resources'         : "xpath=//span[text()='Resources']/../select",
        'discussion'        : "xpath=//span[text()='Discussion']/../select",
        'messages'          : "xpath=//span[text()='Messages']/../select",
        'wishlist'          : "xpath=//span[text()='Wish List']/../select",
        'blog'              : "xpath=//span[text()='Blog']/../select",
        'calendar'          : "xpath=//span[text()='Calendar']/../select",
        'usage'             : "xpath=//span[text()='Usage']/../select",
        'projects'          : "xpath=//span[text()='Projects']/../select",
        'submit'            : "css=#hubForm [type='submit']",
    }


class GroupsCustomizeForm3(FormBase):
    def __init__(self, owner, locatordict={}):
        super(GroupsCustomizeForm3,self).__init__(owner,locatordict)

        # load hub's classes
        GroupsCustomizeForm_Locators = self.load_class('GroupsCustomizeForm_Locators')

        # update this object's locator
        self.locators = GroupsCustomizeForm_Locators.locators

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.logo           = Select(self,{'base':'logo'})
        self.content_type   = Radio(self,{'Default Content' : 'default_content',
                                          'Custom Content'  : 'custom_content'})
        self.overview       = Select(self,{'base':'overview'})
        self.members        = Select(self,{'base':'members'})
        self.wiki           = Select(self,{'base':'wiki'})
        self.resources      = Select(self,{'base':'resources'})
        self.discussion     = Select(self,{'base':'discussion'})
        self.messages       = Select(self,{'base':'messages'})
        self.wishlist       = Select(self,{'base':'wishlist'})
        self.blog           = Select(self,{'base':'blog'})
        self.calendar       = Select(self,{'base':'calendar'})
        self.datasharing    = Select(self,{'base':'datasharing'})

        self.fields += ['logo','content_type','overview','members',
                        'wiki','resources','discussion','messages',
                        'wishlist','blog','calendar','datasharing']

        self._updateLocators()

class GroupsCustomizeForm3_Locators_Base(object):
    """locators for GroupsCustomizeForm3 object"""

    locators = {
        'base'              : "css=#hubForm",
        'logo'              : "css=#group_logo",
        'default_content'   : "css=#group_overview_type_default",
        'custom_content'    : "css=#group_overview_type_custom",
        'overview'          : "xpath=//span[text()='Overview']/../select",
        'members'           : "xpath=//span[text()='Members']/../select",
        'wiki'              : "xpath=//span[text()='Wiki']/../select",
        'resources'         : "xpath=//span[text()='Resources']/../select",
        'discussion'        : "xpath=//span[text()='Discussion']/../select",
        'messages'          : "xpath=//span[text()='Messages']/../select",
        'wishlist'          : "xpath=//span[text()='Wish List']/../select",
        'blog'              : "xpath=//span[text()='Blog']/../select",
        'calendar'          : "xpath=//span[text()='Calendar']/../select",
        'datasharing'       : "xpath=//span[text()='Data Sharing']/../select",
        'submit'            : "css=#hubForm [type='submit']",
    }
