# load the fancy editors for groups new form and wiki pages.
# the fancy editors use iframes instead of the default textarea.
# this works with hub version 1.1.5


# load page object overrides


# load widget overrides
from widgets.groups_new_form import GroupsNewForm2 as GroupsNewForm
from widgets.groups_wiki_edit_form import GroupsWikiEditForm2 as GroupsWikiEditForm
from widgets.groups_wiki_new_form import GroupsWikiNewForm2 as GroupsWikiNewForm


# load page object locator overrides


# load widget locator overrides
from widgets.groups_new_form import GroupsNewForm2_Locators_Base_1 as GroupsNewForm_Locators
from widgets.groups_wiki_edit_form import GroupsWikiEditForm2_Locators_Base as GroupsWikiEditForm_Locators
from widgets.groups_wiki_new_form import GroupsWikiNewForm2_Locators_Base as GroupsWikiNewForm_Locators
