from hubcheck.pageobjects.po_generic_page import GenericPage

class ResourcesNewAuthorsPage(GenericPage):
    """resources new authors page"""

    def __init__(self,browser,catalog):
        super(ResourcesNewAuthorsPage,self).__init__(browser,catalog)
        self.path = "/resources/draft"

        # load hub's classes
        ResourcesNewAuthorsPage_Locators = self.load_class('ResourcesNewAuthorsPage_Locators')
        ResourcesNewAuthorsForm = self.load_class('ResourcesNewAuthorsForm')

        # update this object's locator
        self.locators.update(ResourcesNewAuthorsPage_Locators.locators)

        # setup page object's components
        self.form = ResourcesNewAuthorsForm(self,{'base':'form'})

    def get_groups(self):
        return self.form.get_groups()

    def get_access_levels(self):
        return self.form.get_access_levels()

    def populate_form(self, data):
        return self.form.populate_form(data)

    def submit_form(self,data):
        return self.form.submit_form(data)

    def populate_authors_form(self,data):
        return self.form.populate_authors_form(data)

    def submit_authors_form(self,data):
        return self.form.submit_authors_form(data)

    def get_authors(self):
        return self.form.get_authors()

    def author_role(self,author,role=None):
        return self.form.author_role(author,role)

    def move_author_up(self,author):
        return self.form.move_author_up(author)

    def move_author_down(self,author):
        return self.form.move_author_down(author)

    def delete_author(self,author):
        return self.form.delete_author(author)

    def author_organization(self,author,org=None):
        return self.form.author_organization(author,org)

class ResourcesNewAuthorsPage_Locators_Base(object):
    """locators for ResourcesNewAuthorsPage object"""

    locators = {
        'form' : "css=#hubForm",
    }
