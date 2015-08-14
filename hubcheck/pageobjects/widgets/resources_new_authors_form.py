from hubcheck.pageobjects.basepagewidget import BasePageWidget
from hubcheck.pageobjects.basepageelement import Button
from hubcheck.pageobjects.basepageelement import Select
from hubcheck.pageobjects.widgets.iframewrap import IframeWrap

class ResourcesNewAuthorsForm(BasePageWidget):
    def __init__(self, owner, locatordict={}):
        super(ResourcesNewAuthorsForm,self).__init__(owner,locatordict)

        # load hub's classes
        ResourcesNewAuthorsForm_Locators = self.load_class('ResourcesNewAuthorsForm_Locators')
        ResourcesNewAuthorsAuthorsForm = self.load_class('ResourcesNewAuthorsAuthorsForm')
        ResourcesNewAuthorsAuthorsList = self.load_class('ResourcesNewAuthorsAuthorsList')

        # update this object's locator
        self.locators.update(ResourcesNewAuthorsForm_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.group      = Select(self,{'base':'group'})
        self.access     = Select(self,{'base':'access'})

        self.authorform = IframeWrap(
                            ResourcesNewAuthorsAuthorsForm(
                                self,{'base':'authorsform'}),
                            ['authorsframe'])

        self.authorlist = IframeWrap(
                            ResourcesNewAuthorsAuthorsList(
                                self,{'base':'authorslist'}),
                            ['authorsframe'])

        self.submit     = Button(self,{'base':'submit'})

        self.fields = ['group','access']

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_groups(self):

        return self.group.options()


    def get_access_levels(self):

        return self.access.options()


    def populate_form(self, data):

        for k,v in data.items():
            if v is None:
                continue
            if not k in self.fields:
                # bail, the key is not a field
                raise ValueError("invalid form field: %s" % (k))
            # find the widget in the object's dictionary and set its value
            widget = getattr(self,k)
            widget.value = v


    def submit_form(self,data):

        self.populate_form(data)
        return self.submit.click()

    def populate_authors_form(self,data):

        return self.authorform.populate_form(data)


    def submit_authors_form(self,data):

        return self.authorform.submit_form(data)


    def get_authors(self):
        """return a list of authors"""

        return self.authorlist.get_authors()


    def author_role(self,author,role=None):
        """adjust an author's role"""

        return self.authorlist.author_role(author,role)


    def move_author_up(self,author):
        """increase an author's position"""

        return self.authorlist.move_author_up(author)


    def move_author_down(self,author):
        """decrease an author's position"""

        return self.authorlist.move_author_down(author)


    def delete_author(self,author):
        """remove an author from the list"""

        return self.authorlist.delete_author(author)


    def author_organization(self,author,org=None):
        """set an author's organization"""

        return self.authorlist.author_organization(author,org)


class ResourcesNewAuthorsForm_Locators_Base(object):
    """locators for ResourcesNewAuthorsForm object"""

    locators = {
        'base'              : "css=#hubForm",
        'group'             : "css=#group_owner",
        'access'            : "css=#access",
        'submit'            : "css=#hubForm [type='submit']",
        'authorsform'       : "css=#authors-form",
        'authorslist'       : "css=#authors-list",
        'authorsframe'      : "css=#authors",
    }
