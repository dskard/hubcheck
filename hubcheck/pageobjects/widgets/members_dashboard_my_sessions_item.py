from hubcheck.pageobjects.basepageelement import Link
from hubcheck.pageobjects.basepageelement import TextReadOnly
from hubcheck.pageobjects.widgets.item_list_item import ItemListItem

import re
import datetime

class MembersDashboardMySessionsItem(ItemListItem):
    def __init__(self, owner, locatordict={},row_number=0):

        super(MembersDashboardMySessionsItem,self)\
            .__init__(owner,locatordict,row_number)

        # load hub's classes
        MembersDashboardMySessionsItem_Locators = \
            self.load_class('MembersDashboardMySessionsItem_Locators')

        # update this object's locator
        self.locators.update(MembersDashboardMySessionsItem_Locators.locators)

        # update the locators with those from the owner
        self.update_locators_from_owner()

        # setup page object's components
        self.quick_launch   = Link(self,{'base':'quick_launch'})
        self.title          = Link(self,{'base':'title'})
        self.snapshotlink   = Link(self,{'base':'snapshotlink'})
        self.access_time    = TextReadOnly(self,{'base':'access_time'})
        self.session_owner  = Link(self,{'base':'session_owner'})
        self.resume         = Link(self,{'base':'resume'})
        self.terminate      = Link(self,{'base':'terminate'})
        self.disconnect     = Link(self,{'base':'disconnect'})

        # update the component's locators with this objects overrides
        self._updateLocators()


    def value(self):
        """return a dictionary of properties for this session"""

        # open the slide down window if necessary
        was_open = True
        if not self.is_slide_open():
            was_open = False
            self.toggle_slide()

        properties = {
            'title'             : self.title.text(),
            'access_time'       : self.get_last_accessed()[1],
            'session_owner'     : self.get_session_owner(),
            'session_number'    : self.get_session_number(),
        }

        if was_open is False:
            # close the slide down window
            # if it was originally closed
            self.toggle_slide()

        return properties


    def quick_launch_session(self):
        """use the quick_launch link to open the session"""

        self.quick_launch.click()
        return


    def get_title(self):
        """return the title of the session"""

        return self.title.text()


    def toggle_slide(self):
        """open or close the session item slide down"""

        check_invisible = self.resume.is_displayed()

        self.title.click()

        if check_invisible:
            message = 'while closing toggle, waiting for resume to disappear'
            self.resume.wait_until_invisible(message)
        else:
            message = 'while closing toggle, waiting for resume to appear'
            self.resume.wait_until_visible(message)

        return


    def is_slide_open(self):
        """check if the session item slide down is open"""

        return (self.title.is_displayed() and self.resume.is_displayed())


    def get_last_accessed(self):
        """return the last accessed time stamp as a string and datetime object"""

        at_text = self.access_time.value
        dt_text = re.sub(r'Last Accessed:\s+','',at_text,flags=re.IGNORECASE)
        # dt_text should look something like this:
        # October 12, 2013 @ 12:44am
        dt = datetime.datetime.strptime(dt_text,'%B %d, %Y @ %I:%M%p')

        return (dt_text,dt)


    def get_session_owner(self):
        """return the session owner"""

        owner_text = None
        if self.session_owner.is_displayed():
            owner_text = self.session_owner.text()
        return owner_text


    def get_session_number(self):
        """return the session number based on the url for the "open" link"""

        self.logger.debug('retrieving session number')

        snre = re.compile(r'=([0-9]+)')
        href = self.resume.get_attribute('href')

        self.logger.debug('href = %s' % (href))

        match =  snre.search(href)
        if match:
            session_number = int(match.group(1))
        else:
            session_number = None

        self.logger.debug('session_number = %d' % (session_number))

        return session_number


    def resume_session(self):
        """open this session"""

        return self.resume.click()


    def terminate_session(self,confirm=True):
        """terminate this session"""

        self.terminate.click()
        alert = self._browser.switch_to_alert()
        if confirm:
            self.logger.debug('accepting alert')
            alert.accept()
        else:
            self.logger.debug('dismissing alert')
            alert.dismiss()
        self._browser.switch_to_default_content()


    def disconnect_session(self,confirm=True):
        """disconnect from this shared session"""

        self.disconnect.click()
        alert = self._browser.switch_to_alert()
        if confirm:
            self.logger.debug('accepting alert')
            alert.accept()
        else:
            self.logger.debug('dismissing alert')
            alert.dismiss()
        self._browser.switch_to_default_content()



class MembersDashboardMySessionsItem_Locators_Base(object):
    """locators for MembersDashboardMySessionsItem object"""

    locators = {
        'base'          : "css=.session-list li:nth-of-type({row_num})",
        'quick_launch'  : "css=.session-list li:nth-of-type({row_num}) .session-title-quicklaunch",
        'title'         : "css=.session-list li:nth-of-type({row_num}) .session-title",
        'snapshotlink'  : "css=.session-list li:nth-of-type({row_num}) .session-snapshot-link",
        'snapshotimage' : "css=.session-list li:nth-of-type({row_num}) .session-snapshot-link img",
        'access_time'   : "css=.session-list li:nth-of-type({row_num}) .session-accesstime",
        'session_owner' : "css=.session-list li:nth-of-type({row_num}) .session-sharing a",
        'resume'        : "css=.session-list li:nth-of-type({row_num}) .resume",
        'terminate'     : "css=.session-list li:nth-of-type({row_num}) .terminate-confirm",
        'disconnect'    : "css=.session-list li:nth-of-type({row_num}) .disconnect",
    }
