from hubcheck.pageobjects.widgets.ticket_new_form import TicketNewForm
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.basepageelement import TextAC

class TicketNewFormUpdater(TicketNewForm):
    def __init__(self, owner, locatordict={}):
        super(TicketNewFormUpdater,self).__init__(owner,locatordict)

        # load hub's classes
        TicketNewFormUpdater_Locators = self.load_class('TicketNewFormUpdater_Locators')

        # update this object's locator
        self.locators.update(TicketNewFormUpdater_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.tags            = TextAC(self,{'base':'tags',
                                            'aclocatorid':'tagsac',
                                            'choicelocatorid':'tagsacchoices',
                                            'tokenlocatorid':'tagsactoken',
                                            'deletelocatorid':'tagsacdelete'})
        self.group           = TextAC(self,{'base':'group',
                                            'aclocatorid':'groupac',
                                            'choicelocatorid':'groupacchoices',
                                            'tokenlocatorid':'groupactoken',
                                            'deletelocatorid':'groupacdelete'})
        self.assignee        = Select(self,{'base':'assignee'})
        self.severity        = Select(self,{'base':'severity'})
        self.status          = Select(self,{'base':'statusdd'})

        self.fields += ['tags', 'groups', 'assignee', 'severity', 'status']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def _checkLocatorsTicketUpdater(self,widgets=None,cltype='TicketUpdater'):

        widgets = [self.name,self.organization,self.email,self.os,
                   self.webbrowser,self.problem,self.upload,self.tags,
                   self.group,self.assignee,self.severity,self.status,
                   self.submit]
        self._checkLocators(widgets,cltype)


class TicketNewFormUpdater_Locators_Base(object):
    """locators for TicketNewFormUpdater object"""

    locators = {
        'tags'           : "css=#actags",
        'tagsac'         : "css=#token-input-actags",
        'tagsacchoices'  : "css=.token-input-dropdown-act",
        'tagsactoken'    : "css=.token-input-token-act",
        'tagsacdelete'   : "css=.token-input-delete-token-act",
        'group'          : "css=#acgroup",
        'groupac'        : "css=#token-input-acgroup",
        'groupacchoices' : "css=.token-input-dropdown-acg",
        'groupactoken'   : "css=.token-input-token-acg",
        'groupacdelete'  : "css=.token-input-delete-token-acg",
        'assignee'       : "css=#problemowner",
        'severity'       : "css=[id='ticket[severity]']",
        'statusdd'       : "css=#ticket-field-status",
    }
