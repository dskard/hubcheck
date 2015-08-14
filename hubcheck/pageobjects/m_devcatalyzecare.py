# load default page objects, widgets, and locators
from m_osr_1_1_4 import *


# load page object overrides


# load widget overrides
from widgets.header import Header2 as Header


# load page object locator overrides
from po_login import LoginPage1_Locators_Base_1 as LoginPage_Locators
from po_tags_browse_page import TagsBrowsePage_Locators_Base_1 as TagsBrowsePage_Locators


# load widget locator overrides
from widgets.header import Header2_Locators_Base_4 as Header_Locators
from widgets.login_base import Login_Locators_Base_4 as Login_Locators
