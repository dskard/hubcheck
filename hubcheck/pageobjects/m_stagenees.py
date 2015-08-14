# load default page objects, widgets, and locators
from m_osr_1_3_0 import *
from m_overrides_group_wiki_editors import *


# load page objects overrides


# load widget overrides
from widgets.groups_customize_form import GroupsCustomizeForm3 as GroupsCustomizeForm
from widgets.groups_menu import GroupsMenu2 as GroupsMenu
from widgets.header import Header3 as Header
from widgets.register_form import RegisterForm3 as RegisterForm
from widgets.resources_new_compose_form import ResourcesNewComposeForm2 as ResourcesNewComposeForm
from widgets.ticket_new_form import TicketNewForm2 as TicketNewForm


# load page object locator overrides
from po_supportticketsave import SupportTicketSavePage_Locators_Base_2012 as SupportTicketSavePage_Locators
from po_wishlistsearch import WishlistSearchPage_Locators_Base_2 as WishlistSearchPage_Locators


# load widget locator overrides
from widgets.groups_customize_form import GroupsCustomizeForm3_Locators_Base as GroupsCustomizeForm
from widgets.groups_menu import GroupsMenu2_Locators_Base as GroupsMenu_Locators
from widgets.header import Header3_Locators_Base_1 as Header_Locators
from widgets.resources_new_compose_form import ResourcesNewComposeForm2_Locators_Base as ResourcesNewComposeForm_Locators
from widgets.ticket_new_form import TicketNewForm2_Locators_Base as TicketNewForm_Locators
