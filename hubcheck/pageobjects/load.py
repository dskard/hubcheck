import importlib

class PageObjectCatalog(object):

    def __init__(self,locator_key,browser=None):
        self.locator_key = locator_key
        self.browser = browser

    def load(self,classname):
        if self.locator_key.find('.') == -1:
            modname = "hubcheck.pageobjects.m_%s" % (self.locator_key)
        else:
            modname = self.locator_key
        mod = importlib.import_module(modname)
        cls = getattr(mod,classname)
        return cls

    def load_pageobject(self,classname,*args,**kwargs):
        clsobj = self.load(classname)
        po = clsobj(self.browser,self,*args,**kwargs)
        return po
