# load default page objects, widgets, and locators
from m_osr_1_1_0 import *


# load page objects overrides


# load widgets overrides
from widgets.header import Header


# load page object locator overrides
from po_login import LoginPage1_Locators_Base_1 as LoginPage_Locators


# load widget locator overrides
from widgets.header import Header_Locators_Base as Header_Locators
from widgets.login_base import Login_Locators_Base_4 as Login_Locators
from widgets.ticket_save import TicketSave_Locators_Base as TicketSave_Locators
