import browsermobproxy
import logging
import os

from ..conf import settings
from ..exceptions import ProxyPortError
from ..utils import is_port_listening, which

class Proxy(object):


    def __init__(self, path=None, port=9090):
        """
        path: the filepath to the browsermob-proxy executable
        port: port for running the server

        path defaults to the browsermob-proxy from PATH or raises RuntimeError
        if port is set to None, the proxy will not be started
        """

        self.logger = logging.getLogger(__name__)

        bmp_bin = which('browsermob-proxy')

        if path is not None:
            self.path = path
        elif bmp_bin is not None:
            self.path = bmp_bin
        else:
            raise RuntimeError("can't find browsermob_proxy binary in PATH")

        self.port = port
        self.server = None


    def __str__(self):

        return "%s (port = %s, path = %s, started = %s)" \
            % (self.__class__.__name__,
               self.port,
               self.path,
               self.server is not None)


    def start(self):
        """
        start up browsermobproxy server
        """

        # check if there is already a proxy started for this instance of HUBcheck.
        self.logger.info('checking for previously started browsermob proxy')
        self.logger.info('hubcheck.conf.settings.proxy = %s' % (settings.proxy))
        if settings.proxy is not None:
            self.logger.info('reusing previously started browsermob proxy')
            self.logger.debug("browsermob proxy path = %s" % (settings.proxy.path))
            self.logger.debug("browsermob proxy port = %s" % (settings.proxy.port))
            self.path = settings.proxy.path
            self.port = settings.proxy.port
            self.server = settings.proxy.server
            return

        if (self.port is None) or (self.port < 0):
            self.logger.info('browsermob proxy not started, invalid port: %s'
                % (self.port))
            return

        # find an open port to start the server on
        # based on the suggested port
        self.logger.info("looking for an open port for the proxy server")
        for i in xrange(0,100):
            test_port = self.port + i
            self.logger.debug("checking port: %d" % (test_port))
            if not is_port_listening("localhost",test_port):
                self.logger.debug("found open port: %d" % (test_port))
                self.port = test_port
                break

        self.logger.info("setting up user agent files")

        # modify the browsermobproxy user agent files
        # we do this because of a browsermob proxy bug
        # https://github.com/webmetrics/browsermob-proxy/issues/66
        # they claim it has been resolved, but I still
        # experience it when the following website is down:
        # http://user-agent-string.info/rpc/get_data.php?key=free&format=ini

        path = '/tmp/userAgentString.properties'
        if not os.path.isfile(path):
            self.logger.debug("creating new user agent file: %s" % (path))
            with open(path,'w') as f:
                f.write('lastUpdateCheck=200000000000000\ncurrentVersion=1\n')
        else:
            self.logger.debug("user agent file exists: %s" % (path))

        path = '/tmp/userAgentString.txt'
        if not os.path.isfile(path):
            self.logger.debug("creating new user agent file: %s" % (path))
            with open(path,'w') as f:
                f.write('')
        else:
            self.logger.debug("user agent file exists: %s" % (path))

        self.logger.info("starting web proxy")

        if not os.path.isfile(self.path):
            raise RuntimeError("invalid path for browsermob_proxy: %s" % (self.path))

        self.logger.debug("browsermob proxy path = %s" % (self.path))
        self.logger.debug("browsermob proxy port = %s" % (self.port))
        self.server = browsermobproxy.Server(self.path,
                        {'port':self.port})
        self.server.start()
        settings.proxy = self
        self.logger.info('hubcheck.conf.settings.proxy = %s' % (settings.proxy))


    def stop(self):
        """
        stop the browsermobproxy server
        """

        # check if we are using a server inhereted from the
        # hubcheck instance.
        if settings.proxy != self:
            self.logger.info("destroying copy of web proxy details")
            self.server = None
            return

        # check if proxy_server attribute exists and is not None
        if self.server is not None:
            self.logger.info("stopping web proxy")
            self.server.stop()
            self.server = None
            settings.proxy = None


    def create_client(self,port=None):
        """
        create a proxy client on the provided port

        if port is None, an open port will be searched
        for, starting at the proxy server's port + 1 and
        ending at the proxy server's port + 9
        """

        if self.server is None:
            self.logger.info("proxy server not started, no client available")
            return None

        if port is None:
            # find an open port for the proxy client
            # use browsermob_proxy_port+1 as the starting point
            # count up until we find an open port.
            # there is a bit of a race condition if running multiple
            # hubcheck instances at a time on the same machine.
            # be sure to give each instance a different proxy server port.
            self.logger.debug("finding browser proxy client port")
            proxy_client_port = 0
            for i in xrange(1,10):
                test_port = self.port + i
                self.logger.debug("checking port: %d" % (test_port))
                if not is_port_listening("localhost",test_port):
                    self.logger.debug("found open port: %d" % (test_port))
                    proxy_client_port = test_port
                    break
            if proxy_client_port == 0:
                msg = "trouble finding an open port for the proxy client"
                self.logger.error(msg)
                raise ProxyPortError(msg)
        else:
            proxy_client_port = port

        self.logger.info("browser proxy client port: %d" %
            (proxy_client_port))

        # start the client
        client = self.server.create_proxy({'port':proxy_client_port})

        return client
