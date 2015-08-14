import os
import random
import re
import sys
import hubcheck
# from hubcheck.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException
import time


class Tags(object):

    def __init__(self, browser, catalog):

        self.browser = browser
        self.catalog = catalog
        self.logger = self.browser.logger

    def find_tag_with_items(self):
        """
        return a tag name that is used by items

        Some tags are either not used or have no items that
        are displayed by the tags component (private items,
        unpublished items, pending items). This function returns
        the name of a tag that is used and has items people can see
        or returns None if no tags with items are available.
        """

        self.logger.info("looking for a tag with items")

        tag_name = None

        # goto /browse and get all of the tags for the site
        self.logger.info("getting the list of all tags")
        po = self.catalog.load_pageobject('TagsPage')
        po.goto_page()

        all_tag_names = []

        all_tag_names.extend([x['name'] for x in po.get_recently_used_tags()])
        all_tag_names.extend([x['name'] for x in po.get_top_100_tags()])

        tag_name = self.find_tag_with_items_from_list(all_tag_names)

        if tag_name is not None:
            return tag_name

        # didn't find a valid tag from first level search, try harder
        # get tags from the /browse page
        po.goto_page()
        po.goto_all_tags()

        po = self.catalog.load_pageobject('TagsBrowsePage')
        # change the display limit to 'All'
        new_display_limit = 'All'
        po.form.footer.display_limit(new_display_limit)

        # get all of the tag names
        for row in po.search_result_rows():
            # tag_info = row.value()
            # only save tags with a positive tag count
            # all_tag_names.append(tag_info['name'])

            all_tag_names.append(row.name.text())


        return self.find_tag_with_items_from_list(all_tag_names)


    def find_tag_with_items_from_list(self,search_strings):

        tag_name = None

        # go back to the tags page and search for a tag with items
        po = self.catalog.load_pageobject('TagsPage')
        po2 = self.catalog.load_pageobject('TagsViewPage')
        self.logger.info("searching for a tag with items")

        while len(search_strings) > 0:
            # do a random walk of the list to avoid all of the
            # numeric version tags that usually populate the
            # beginning of these lists, but have no resources.
            search_str = search_strings.pop(
                random.randint(0,len(search_strings)-1))
            self.logger.debug("checking tag %s" % (search_str))
            po.goto_page()
            po.search_for_content([search_str])
            try:
                po2.get_caption_counts()
                # this page seems to have counts
                # which suggests it has viewable items
                # return the tag name
                self.logger.debug("found tag with items: %s" % (search_str))
                tag_name = search_str
                break
            except TimeoutException:
                # this page probably doesn't have items
                # keep searching
                pass

        return tag_name
