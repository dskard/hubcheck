import json
import os
from urlparse import urlsplit, urlunsplit, urljoin, SplitResult, ParseResult
import base64
import hashlib
import pprint

class LinkTracker(object):
    def __init__(self):
        self.ERRORCODE      = 'errorcode'
        self.EXCEPTION      = 'exception'
        self.NO_HREF        = 'no_href'
        self.COMPLETEDLINK  = 'completed_link'
        self.COMPLETEDPAGE  = 'completed_page'
        self.BADLINK        = 'bad_links'
        self.TODO           = 'todo'
        self.SCHEMECHANGE   = 'scheme_change'

        self._datastore = {
            self.NO_HREF        : {},
            self.ERRORCODE      : {},
            self.EXCEPTION      : {},
            self.COMPLETEDLINK  : {},
            self.COMPLETEDPAGE  : {},
            self.BADLINK        : {},
            self.TODO           : {},
            self.SCHEMECHANGE   : {},
        }

    def is_bad_link(self,link_url):

        return self._datastore[self.BADLINK].has_key(link_url)


    def bad_link_status(self,link_url):

        if not self.is_bad_link(link_url):
            return None

        key = self._datastore[self.BADLINK][link_url][0]
        status = self._datastore[self.ERRORCODE][key]['status']

        return status


    def store_bad_link(self,parent_url,locator,target):

        if parent_url == None or locator == None or target == None:
            raise TypeError("invalid value: parent_url = %s, locator = %s, target = %s" %
                (parent_url,locator,target))

        pu = urlsplit(parent_url)
        pk = urlunsplit(SplitResult('',pu.netloc,pu.path,pu.query,''))
        key = base64.urlsafe_b64encode(hashlib.sha256(pk+locator).digest())

        if not self._datastore.has_key(self.ERRORCODE):
            self._datastore[self.ERRORCODE] = {}

        if not self._datastore.has_key(self.BADLINK):
            self._datastore[self.BADLINK] = {}

        if not self._datastore[self.ERRORCODE].has_key(key):
            self._datastore[self.ERRORCODE][key] = {}
        self._datastore[self.ERRORCODE][key].update({
            'parent_url'  : parent_url,
            'locator'     : locator,
            'target'      : target,
            'screenshot'  : None,
        })

        if not self._datastore[self.BADLINK].has_key(target):
            self._datastore[self.BADLINK][target] = []
        self._datastore[self.BADLINK][target].append(key)

        return key


    def next_bad_link(self):

        return self._datastore[self.ERRORCODE].iteritems()


    def remove_bad_link(self,target):

        if self.is_bad_link(target):
            for key in self._datastore[self.BADLINK][target]:
                del self._datastore[self.ERRORCODE][key]
            del self._datastore[self.BADLINK][target]


    def set_bad_link_record_property(self,key,prop,value):

        if not self._datastore[self.ERRORCODE].has_key(key):
            raise ValueError("invalid key: %s" % (key))
        self._datastore[self.ERRORCODE][key][prop] = value


    def get_bad_link_record_property(self,key,prop,default=None):

        if not self._datastore[self.ERRORCODE].has_key(key):
            raise ValueError("invalid key: %s" % (key))
        if self._datastore[self.ERRORCODE][key].has_key(prop):
            return self._datastore[self.ERRORCODE][key][prop]
        else:
            return default


    def count_bad_links(self):

        return len(self._datastore[self.ERRORCODE].keys())


    def store_exception_link_old_1(self,parent_url,link_url,link_text,detail):

        if parent_url == None or link_url == None or link_text == None or detail == None:
            raise TypeError("invalid value: parent_url = %s, link_url = %s, link_text = %s detail = %s" %
                (parent_url, link_url, link_text, detail))

        if not self._datastore[self.EXCEPTION].has_key(link_url):
            self._datastore[self.EXCEPTION][link_url] = []
        self._datastore[self.EXCEPTION][link_url].append({
            'parent_url'  : parent_url,
            'link_text'   : link_text,
            'detail'      : detail,
        })


    def store_exception_link(self,parent_url,link_url,locator,detail):

        if parent_url == None or link_url == None or locator == None or detail == None:
            raise TypeError("invalid value: parent_url = %s, link_url = %s, locator = %s detail = %s" %
                (parent_url, link_url, locator, detail))

        if not self._datastore[self.EXCEPTION].has_key(link_url):
            self._datastore[self.EXCEPTION][link_url] = []
        self._datastore[self.EXCEPTION][link_url].append({
            'parent_url'  : parent_url,
            'locator'     : locator,
            'detail'      : detail,
        })


    def next_exception_link(self):

        for (target,v) in self._datastore[self.EXCEPTION].iteritems():
            for record in v:
                parent  = record['parent_url']
                locator = record['locator']
                yield(parent,locator,target)


    def store_bad_href(self,parent_url,locator):

        if parent_url == None or locator == None:
            raise TypeError("invalid value: parent_url = %s, locator = %s" %
                (parent_url, locator))

        if not self._datastore[self.NO_HREF].has_key(parent_url):
            self._datastore[self.NO_HREF][parent_url] = []
        self._datastore[self.NO_HREF][parent_url].append(locator)


    def store_scheme_change(self,parent_url,locator,target):

        if parent_url == None or locator == None or target == None:
            raise TypeError("invalid value: parent_url = %s, locator = %s, target = %s" %
                (parent_url, locator, target))

        pu = urlsplit(parent_url)
        pk = urlunsplit(SplitResult('',pu.netloc,pu.path,pu.query,''))
        key = base64.urlsafe_b64encode(hashlib.sha256(pk+locator).digest())

        if not self._datastore.has_key(self.SCHEMECHANGE):
            self._datastore[self.SCHEMECHANGE] = {}

        if not self._datastore[self.SCHEMECHANGE].has_key(key):
            self._datastore[self.SCHEMECHANGE][key] = {}
        self._datastore[self.SCHEMECHANGE][key].update({
            'parent_url'  : parent_url,
            'locator'     : locator,
            'target'      : target,
        })

        return key


    def is_completed_link(self,link_url):

        return self._datastore[self.COMPLETEDLINK].has_key(link_url)


    def store_completed_link(self,link_url):

        self._datastore[self.COMPLETEDLINK].update({link_url : None})


    def is_completed_page(self,page_url):

        return page_url in self._datastore[self.COMPLETEDPAGE]


    def store_completed_page(self,page_url):

        if page_url == None:
            raise TypeError("invalid value: page_url = %s" % (page_url))

        self._datastore[self.COMPLETEDPAGE].update({page_url : None})


    def schedule_page(self,url,depth):

        self._datastore[self.TODO].update({url : depth})


    def count_scheduled_pages(self):

        return len(self._datastore[self.TODO].keys())


    def next_scheduled_page(self):

        (url,depth) = self._datastore[self.TODO].popitem()
        return (url,depth)


    def save(self,fname):

        # sort the lists
        #self._datastore[self.COMPLETEDLINK].sort()
        #self._datastore[self.COMPLETEDPAGE].sort()
        # write the bad links to a file
        # we use a temporary file incase the write fails,
        # we will still have a valid state file.

        tmpfname = fname + '.tmp'
        with open(tmpfname,'w') as f:
            f.write(json.dumps(self._datastore, indent=4))
        if os.path.exists(fname):
            os.remove(fname)
        os.rename(tmpfname,fname)


    def load(self,fname):

        with open(fname,'r') as f:
            self._datastore = json.load(f)


    def convert1(self):

        for dkey in [self.COMPLETEDPAGE, self.COMPLETEDLINK]:
            dkey2 = dkey + "2"
            self._datastore[dkey2] = {}
            for item in self._datastore[dkey]:
                self._datastore[dkey2].update({item : None})
            dklen = len(self._datastore[dkey])
            dk2len = len(self._datastore[dkey2].keys())
            print "datastore[%s] = %d\ndatastore[%s] = %d" % (dkey,dklen,dkey,dk2len)
            if dklen != dk2len:
                raise ValueError("counts are off")
            del self._datastore[dkey]
            self._datastore[dkey] = self._datastore[dkey2]
            del self._datastore[dkey2]

        for dkey in [self.TODO]:
            dkey2 = dkey + "2"
            self._datastore[dkey2] = {}
            for (url,depth) in self._datastore[dkey]:
                self._datastore[dkey2].update({url : depth})
            dklen = len(self._datastore[dkey])
            dk2len = len(self._datastore[dkey2].keys())
            print "datastore[%s] = %d\ndatastore[%s] = %d" % (dkey,dklen,dkey,dk2len)
            if dklen != dk2len:
                raise ValueError("counts are off")
            del self._datastore[dkey]
            self._datastore[dkey] = self._datastore[dkey2]
            del self._datastore[dkey2]
