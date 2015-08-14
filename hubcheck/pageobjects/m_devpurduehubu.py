# load default page objects, widgets, and locators
from m_osr_1_1_5 import *


# load page objects overrides


# load widgets overrides
from widgets.header import Header2 as Header
from widgets.members_profile_form import MembersProfileForm3 as MembersProfileForm


# load page object locator overrides
from po_supportticketsave import SupportTicketSavePage_Locators_Base_2012b as SupportTicketSavePage_Locators
from po_wishlistsearch import WishlistSearchPage_Locators_Base_2 as WishlistSearchPage_Locators


# load widget locator overrides
from widgets.header import Header2_Locators_Base as Header_Locators
from widgets.wishlist_search_form import WishlistSearchForm_Locators_Base_2013 as WishlistSearchForm_Locators
