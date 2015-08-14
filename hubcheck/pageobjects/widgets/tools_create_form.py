from hubcheck.pageobjects.widgets.form_base import FormBase
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import Text

class ToolsCreateForm(FormBase):
    def __init__(self, owner, locatordict={}):
        super(ToolsCreateForm,self).__init__(owner,locatordict)

        # load hub's classes
        ToolsCreateForm_Locators = self.load_class('ToolsCreateForm_Locators')

        # update this object's locator
        self.locators.update(ToolsCreateForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.name               = Text(self,{'base':'name'})
        self.title              = Text(self,{'base':'title'})
        self.version            = Text(self,{'base':'version'})
        self.description        = Text(self,{'base':'description'})
        self.vncwidth           = Text(self,{'base':'vncwidth'})
        self.vncheight          = Text(self,{'base':'vncheight'})
        self.toolaccess         = Select(self,{'base':'toolaccess'})
        self.toolaccessgroups   = Text(self,{'base':'groups'})
        self.codeaccess         = Select(self,{'base':'codeaccess'})
        self.projectaccess      = Select(self,{'base':'projectaccess'})
        self.devteam            = Text(self,{'base':'devteam'})


        self.fields += ['name','title','version','description',
                        'vncwidth','vncheight','toolaccess',
                        'toolaccessgroups','codeaccess',
                        'projectaccess','devteam']

        # update the component's locators with this objects overrides
        self._updateLocators()


class ToolsCreateForm_Locators_Base(object):
    """locators for ToolsCreateForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'name'              : "css=#t_toolname",
        'title'             : "css=#t_title",
        'version'           : "css=#t_version",
        'description'       : "css=#t_description",
        'vncwidth'          : "css=#vncGeometryX",
        'vncheight'         : "css=#vncGeometryY",
        'toolaccess'        : "css=#t_exec",
        'groups'            : "css=#t_groups",
        'codeaccess'        : "css=#t_code",
        'projectaccess'     : "css=#t_wiki",
        'devteam'           : "css=#t_team",
        'submit'            : "css=#hubForm input[type='submit']",
    }
