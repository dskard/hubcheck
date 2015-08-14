from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Link
from selenium.webdriver.common.action_chains import ActionChains

class AdminMenu1(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(AdminMenu1,self).__init__(owner,locatordict)

        # load hub's classes
        AdminMenu_Locators = self.load_class('AdminMenu_Locators')

        # update this object's locator defaults
        self.locators.update(AdminMenu_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components

        self.linkpath = {
            'site'                  : ['Site'],
            'control_panel'         : ['Site','Control Panel'],
            'my_profile'            : ['Site','My Profile'],
            'global_configuration'  : ['Site','Global Configuration'],
            'maintenance'           : ['Site','Maintenance'],
            'global_check_in'       : ['Site','Maintenance','Global Check-in'],
            'clear_cache'           : ['Site','Maintenance','Clear Cache'],
            'purge_expired_cache'   : ['Site','Maintenance','Purge Expired Cache'],
            'ldap'                  : ['Site','Maintenance','LDAP'],
            'geo_db'                : ['Site','Maintenance','Geo DB'],
            'apc'                   : ['Site','Maintenance','APC'],
            'scripts'               : ['Site','Maintenance','Scripts'],
            'routes'                : ['Site','Maintenance','Routes'],
            'system_info'           : ['Site','System Information'],
            'logout'                : ['Site','Logout'],
            'users'                 : ['Users'],
            'user_manager'          : ['Users','User Manager'],
            'add_new_user'          : ['Users','User Manager','Add New User'],
            'members'               : ['Users','Members'],
            'groups'                : ['Users','Groups'],
            'access_groups'         : ['Users','Access Groups'],
            'add_new_group'         : ['Users','Access Groups','Add New Group'],
            'access_levels'         : ['Users','Access Levels'],
            'add_new_access_level'  : ['Users','Access Levels','Add New Access Level'],
            'user_notes'            : ['Users','User Notes'],
            'add_user_note'         : ['Users','User Notes','Add User Note'],
            'user_note_catagories'  : ['Users','User Note Catagories'],
            'unc_add_new_catagory'  : ['Users','User Note Catagories','Add New Catagory'],
            'mass_mail_users'       : ['Users','Mass Mail Users'],
            'menus'                 : ['Menus'],
            'menu_manager'          : ['Menus','Menu Manager'],
            'add_new_menu'          : ['Menus','Menu Manager','Add New Menu'],
            'main_menu'             : ['Menus','Main Menu'],
            'add_new_main_menu_item': ['Menus','Main Menu','Add New Menu Item'],
            'legal'                 : ['Menus','Legal'],
            'legal_add_new_menu_item': ['Menus','Legal','Add New Menu Item'],
            'about'                 : ['Menus','About'],
            'about_add_new_menu_item': ['Menus','About','Add New Menu Item'],
            'default'               : ['Menus','Default'],
            'default_add_new_menu_item': ['Menus','Default','Add New Menu Item'],
            'content'               : ['Content'],
            'article_manager'       : ['Content','Article Manager'],
            'am_add_new_article'    : ['Content','Article Manager','Add New Article'],
            'catagory_manager'      : ['Content','Catagory Manager'],
            'cm_add_new_catagory'   : ['Content','Catagory Manager','Add New Article'],
            'featured_articles'     : ['Content','Featured Articles'],
            'media_manager'         : ['Content','Media Manager'],
            'components'            : ['Components'],
            'answers'               : ['Components','Answers'],
            'billboards'            : ['Components','Billboards'],
            'blog'                  : ['Components','Blog'],
            'cart'                  : ['Components','Cart'],
            'collections'           : ['Components','Collections'],
            'courses'               : ['Components','Courses'],
            'cron'                  : ['Components','Cron'],
            'dataviewer'            : ['Components','DataViewer'],
            'databases'             : ['Components','Databases'],
            'events'                : ['Components','Events'],
            'feedback'              : ['Components','Feedback'],
            'forum'                 : ['Components','Forum'],
            'jobs'                  : ['Components','Jobs'],
            'knowledge_base'        : ['Components','Knowledge Base'],
            'newsletter'            : ['Components','Newsletter'],
            'poll'                  : ['Components','Poll'],
            'projects'              : ['Components','Projects'],
            'publications'          : ['Components','Publications'],
            'registration'          : ['Components','Registration'],
            'resources'             : ['Components','Resources'],
            'services'              : ['Components','Services'],
            'store'                 : ['Components','Store'],
            'support'               : ['Components','Support'],
            'tags'                  : ['Components','Tags'],
            'tools'                 : ['Components','Tools'],
            'usage'                 : ['Components','Usage'],
            'wiki'                  : ['Components','Wiki'],
            'ysearch'               : ['Components','YSearch'],
            'oilspillvideo'         : ['Components','oilspillvideo'],
            'reporting'             : ['Components','reporting'],
            'sef'                   : ['Components','sef'],
            'storefront'            : ['Components','storefront'],
            'survey'                : ['Components','survey'],
            'extensions'            : ['Extensions'],
            'extension_manager'     : ['Extensions','Extension Manager'],
            'module_manager'        : ['Extensions','Module Manager'],
            'plugin_manager'        : ['Extensions','Plug-in Manager'],
            'template_manager'      : ['Extensions','Template Manager'],
            'language_manager'      : ['Extensions','Language Manager'],
            'help'                  : ['Help'],
            'joomla_help'           : ['Help','Joomla Help'],
            'official_support_forum': ['Help','Official Support Forum'],
            'documentation_wiki'    : ['Help','Documenation Wiki'],
        }

        # update the component's locators with this objects overrides
        self._updateLocators()

    def _checkLocators(self,widgets=None,cltype=''):
        base = self.owner.find_element(self.locators['base'])

        # hover mouse over the group manager toolbar to expand it
        actionProvider = ActionChains(self.owner._browser)\
                         .move_to_element(base)
        actionProvider.perform()

        # check for locators
        super(AdminMenu,self)._checkLocators(widgets,cltype)


    def goto(self,link):
        """this function does selenium specific stuff"""

        if not link in self.linkpath:
            raise ValueError("invalid link name: '%s'",link)

        # add the base
        e = self.owner.find_element(self.locators['base'])

        actionProvider = ActionChains(self.owner._browser)\
                            .move_to_element(e)

        # traverse the menu
        for link_text in self.linkpath[link]:
            link_locator = self.locators['template'].format(link_text=link_text)
            e = self.find_element(link_locator,e)
            actionProvider.move_to_element(e)

        # click the element
        actionProvider.click()

        # perform the actions
        actionProvider.perform()


class AdminMenu1_Locators_Base_1(object):
    """locators for AdminMenu1 object"""

    locators = {
        'base'      : "css=#menu",
        'template'  : "xpath=//a[text()='{link_text}']",
    }

