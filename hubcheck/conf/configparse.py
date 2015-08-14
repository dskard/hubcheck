import ConfigParser

class ConfigurationOptions(object):
    """
    generic shell object for storing attributes
    """
    pass

class ConfigurationParser(object):

    def __init__(self,path=""):
        self._options = {}
        self._path = path


    def set_path(self,path):

        self._path = path


    def add_option(self,dest,path,help=None,action="get",default=None,type="string"):

        self._options[dest] = {
            'path' : path,
            'help' : help,
            'action' : action,
            'default' : default,
            'type' : type,
        }


    def del_option(self,dest):

        if dest in self._options:
            del self._options[dest]


    def parse_config(self):

        options = ConfigurationOptions()
        config = ConfigParser.ConfigParser(allow_no_value=True)
        config.read(self._path)

        for dest,details in self._options.items():

            path = details['path']
            actionfxn = getattr(config,details['action'])

            try:
                value = details['type'](actionfxn(*path))
            except:
                value = details['default']

            setattr(options,dest,value)

        return options


