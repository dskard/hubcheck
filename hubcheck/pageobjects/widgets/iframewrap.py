import random
import string

# iframe_locators    - all iframes that need to be traversed
#                      to get to this object
# iframe_locator_ids - keys into the obj's owner's locatordict for iframes
# current_framelevel - index of the current iframe in iframe_locators


class IframeTracker(object):

    def __init__(self,obj):

        self.obj = obj
        self.iframe_locators = []
        self.iframe_locator_ids = []
        self.current_framelevel = 0


    def add_iframe(self,framelocid):

        iframeloc = self.obj.owner.locators[framelocid]
        if iframeloc is not None:
            self.iframe_locators.append(iframeloc)
            self.iframe_locator_ids.append(framelocid)


    def update_iframe_locators(self):

        iframelocids = self.iframe_locator_ids
        self.iframe_locators = []
        self.iframe_locator_ids = []
        for framelocid in iframelocids:
            self.add_iframe(framelocid)


    def wrap_new_object(self,obj):

        objlist = [obj]
        for o in objlist:
            o.logger.debug('wrapping %s' % (o.__class__.__name__))
            o.iframe_tracker = self
            self.wrap_callable_attributes(o)
            self.wrap_property_attributes(o)
            objlist.extend(o.widgets)


    def wrap_callable_attributes(self,o):
        """wrap callable attributes of the object.

           traverse the object's class and base classes to find
           callable attributes to wrap.

           avoid wrapping __init__() methods and "noiframe" methods
           that were predetermined not to be affected by iframes.
        """

        clslist = [o.__class__]
        for cls in clslist:
            if cls.__name__ == 'object':
                continue
            dct = cls.__dict__
            for attr, item in dct.items():
                if attr != '__init__' and callable(item):
                    if attr in o.noiframe:
                        # skip attributes that are specifically
                        # noted not to need an iframe context change
                        # as listed in the noiframe list
                        self.obj.logger.debug('skipping function: %s' % (attr))
                        continue
                    item = getattr(o,attr)
                    setattr(o,attr,self.wrap_attribute(item))
                    self.obj.logger.debug('wrapping function: %s' % (attr))
            clslist.extend(cls.__bases__)


    def wrap_property_attributes(self,o):
        """wrap property attributes of the object.

           to do this, we first create a new class object that we can
           freely manipulate, by copying the base classes and attribute
           dictionary from the original page object class. next we search
           the new class for property attributes.

           currently we only wrap the properties of the object's class.
           properties of the object's base clases are ignored for now.
           i believe the act of accessing the property ends up executing
           the property's getter or setter methods, which will fail if
           you are not on the page and in the correct context hosting
           the object. Or perhaps the property information is associated
           with a class object, so changing the class object changes how
           all newly instantiated objects will work.
        """

        randtxt = ''.join([random.choice(string.ascii_lowercase) \
                    for i in range(5)])
        clsname = "IframeWrap_" + randtxt + "_" + o.__class__.__name__

        self.obj.logger.debug('creating new class \'%s\' from \'%s\'' \
            % (clsname,o.__class__.__name__))

        cls = type(clsname,
                   o.__class__.__bases__,
                   dict(o.__class__.__dict__))

        o.__class__ = cls

        dct = cls.__dict__
        for attr, item in dct.items():
            if isinstance(item,property):
                if attr in o.noiframe:
                    # skip attributes that are specifically
                    # noted not to need an iframe context change
                    # as listed in the noiframe list
                    self.obj.logger.debug('skipping property: %s' % (attr))
                    continue
                new_property = property(self.wrap_attribute(item.__get__),
                                        self.wrap_attribute(item.__set__),
                                        item.__delattr__)
                setattr(cls,attr,new_property)
                self.obj.logger.debug('wrapping property: %s' % (attr))


    def wrap_attribute(self,f):
        def _wrapper(*args, **kwds):
            self.obj.logger.debug('Entering wrapper function for %s' \
                % (f.__name__))

            # count our framelevels backwards
            # think of framelevel 0 as the browser context

            initial_framelevel = self.current_framelevel
            final_framelevel = -1 * len(self.iframe_locators)

            self.obj.logger.debug('starting frame level: %s' \
                % (self.current_framelevel))

            switched = self._switch_to_iframe_context(final_framelevel)

            # make sure we return to the previous context if an exception is
            # raised.  exceptions are often raised when using find_element
            # based functions or waiting for elements to appear or diappear.
            # this try/final block helps ensure we don't lose track of our
            # frame level when exceptions occur.

            r = None

            try:
                # call the function
                self.obj.logger.debug('current frame level: %s in %s' \
                    % (self.current_framelevel, self.iframe_locators))
                self.obj.logger.debug('calling function: %s' % f.__name__)
                r = f(*args, **kwds)
            finally:
                # exit the frame
                if switched:
                    self._switch_to_iframe_context(initial_framelevel)

                self.obj.logger.debug('ending frame level = %s' \
                    % (self.current_framelevel))

                self.obj.logger.debug('Exiting wrapper function for %s' \
                    % (f.__name__))

            return r

        return _wrapper


    def _switch_to_iframe_context(self,framelevel):

        switched_frames = False

        if framelevel > self.current_framelevel:
            self.obj.logger.debug('-> switching to default context')
            self.obj._browser.switch_to_default_content()
            self.current_framelevel = 0
            switched_frames = True

        while self.current_framelevel > framelevel:
            next_framelevel = self.current_framelevel - 1
            frameloc = self.iframe_locators[next_framelevel]

            # we use the obj's owner's find_element to help us deal
            # with the edge case where obj is in an iframe and the owner is not
            # if obj and owner are in different frames, we will first
            # get into the owner's frame, then perform a search for the element
            frame = self.obj.owner.find_element(frameloc)

            self.obj.logger.debug('-> switching to iframe: %s' % (frameloc))
            self.obj._browser.switch_to_frame(frame)
            self.current_framelevel = next_framelevel

            switched_frames = True

        return switched_frames


def IframeWrap(obj,framelocids):

    if obj.iframe_tracker is not None:
        ift = obj.iframe_tracker
    else:
        ift = IframeTracker(obj)

    # accept a string or list of frame locator ids
    if not hasattr(framelocids,'__iter__'):
        framelocids = [framelocids]

    # add each iframe, inner most iframe first
    for framelocid in framelocids:
        ift.add_iframe(framelocid)

    ift.wrap_new_object(obj)

    return obj


# a = A()
# a = IframeWrap(a,['iframe'])
# a = IframeWrap(a,['iframe2','iframe1'])
# a = IframeWrap(IframeWrap(a,'iframe2'),'iframe1')


