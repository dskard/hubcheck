from hubcheck.pageobjects.widgets.item_list_item import ItemListItem
from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.exceptions import NoSuchFileAttachmentError
from selenium.common.exceptions import NoSuchElementException
import re

class TicketCommentBase(ItemListItem):
    def __init__(self, owner, locatordict={}, row_number=0):
        super(TicketCommentBase,self).__init__(owner,locatordict,row_number)

        # load hub's classes
        TicketCommentBase_Locators = self.load_class('TicketCommentBase_Locators')

        # update this object's locator
        self.locators.update(TicketCommentBase_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.commenter = Link(self,{'base':'commenter'})
        self.body      = TextReadOnly(self,{'base':'body'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def get_commenter(self):
        """return the commenter"""

        return self.commenter.text()


    def get_body(self):
        """return the body of the comment"""

        return self.body.value


    def download_attachment(self,attachment):
        """download a file attachment in the comment"""

        links = []

        try:
            # ticket content widgets (and old style comments?)
            # store downloadable content in the body
            bodytext = self.find_element_in_owner(self.locators['body'])
            links.extend(self.find_elements('css=a',bodytext))
        except NoSuchElementException as e:
            self.logger.exception(e)
            pass

        try:
            # ticket comments store downloadable content in the
            # attachments section
            attext = self.find_element_in_owner(self.locators['attachments'])
            links.extend(self.find_elements('css=a',attext))
        except NoSuchElementException as e:
            self.logger.exception(e)
            pass

        download_element = None
        href = None
        for link in links:
            href = link.get_attribute('href')
            self.logger.debug('found link: %s' % (href))
            if re.search(attachment,href):
                download_element = link
                break
        if download_element is None:
            raise NoSuchFileAttachmentError(attachment)

        download_element.click()

        return href


    def download_image(self,imageName):
        """
        download an image file attachment in the comment
        """

        # click the link to download the image
        self.download_attachment(imageName)

        # clicking the download link takes user to another
        # webpage with just an image return the src
        # attribute of the image

        e = self.find_element(self.locators['image'])
        return e.get_attribute('src')


class TicketCommentBase_Locators_Base(object):
    """locators for TicketCommentBase object"""

    locators = {
        'base'           : "css=.ticket",
        'commenter'      : "css=.ticket-title a",
        'body'           : "css=p:nth-child(2)",
        'attachments'    : None,
        'image'          : "css=img",
    }
