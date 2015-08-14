# hub utilities

from .account import Account
from .contribtool import Contribtool
from .groups import Groups
from .support import Support
from .tags import Tags

class HubzeroActions(object):

    def __init__(self, hubname, browser, catalog):

        self.account = Account(browser,catalog)
        self.contribtool = Contribtool(hubname,browser,catalog)
        self.groups = Groups(browser,catalog)
        self.support = Support(browser,catalog)
        self.tags = Tags(browser,catalog)
