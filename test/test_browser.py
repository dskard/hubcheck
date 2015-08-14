import pytest
import os
import hubcheck
from hubcheck.browser import Firefox
from hubcheck.browser import Proxy
from hubcheck.utils import which, is_port_listening

pytestmark = [ pytest.mark.hcunit,
               pytest.mark.hcunit_browser,
             ]


@pytest.mark.firefox
class TestHCUnitBrowserFirefox(object):

    def test_launch(self):
        """
        launch the browser
        """

        ff = Firefox()
        ff.launch()

    def test_get(self):
        """
        load a web page in the browser
        """

        ff = Firefox()
        ff.launch()

        ff.get('https://hubzero.org')


@pytest.fixture(scope="function")
def setup_clear_path(request):
    original_path = os.environ['PATH']
    os.environ['PATH'] = ''
    def fin():
        os.environ['PATH'] = original_path
    request.addfinalizer(fin)


@pytest.fixture(scope="function")
def teardown_stop_proxy(request):
    def fin():
        proxy = hubcheck.conf.settings.proxy
        if proxy is not None:
            proxy.stop()

    request.addfinalizer(fin)

@pytest.fixture(scope="function")
def proxy(request):
    proxy = Proxy()
    proxy.start()
    def fin():
        proxy = hubcheck.conf.settings.proxy
        if proxy is not None:
            proxy.stop()

    request.addfinalizer(fin)
    return proxy


@pytest.mark.proxy
class TestHCUnitBrowserProxy(object):

    def test_init_1(self):
        """
        instantiate a Proxy object with default parameters
        """

        proxy = Proxy()
        assert proxy.path == which('browsermob-proxy')
        assert proxy.port == 9090
        assert proxy.server is None


    def test_init_2(self):
        """
        Proxy object with custom path /usr/bin/browsermob-proxy
        """

        proxy = Proxy(path='/usr/bin/browsermob-proxy')
        assert proxy.path == '/usr/bin/browsermob-proxy'


    @pytest.mark.usefixtures("setup_clear_path")
    def test_init_3(self):
        """
        Proxy object cannot find browsermob-proxy exe
        """

        with pytest.raises(RuntimeError):
            proxy = Proxy()


    @pytest.mark.usefixtures("teardown_stop_proxy")
    def test_start_1(self):
        """
        setup a new proxy server with valid inputs and start it
        at the end of the process the following should be true:
        1. hubcheck.conf.settings.proxy is not None
        2. proxy.port is listening
        3. /tmp/userAgentString.properties is populated
        4. /tmp/userAgentString.txt is populated
        """

        assert hubcheck.conf.settings.proxy is None

        proxy = Proxy()
        proxy.start()

        assert hubcheck.conf.settings.proxy is not None
        assert is_port_listening('localhost',proxy.port) is True
        assert os.path.isfile('/tmp/userAgentString.properties')
        assert os.path.isfile('/tmp/userAgentString.txt')


    def test_stop_1(self):
        """
        stop the proxy server
        at the end of the process the following should be true:
        1. hubcheck.conf.settings.proxy is None
        2. proxy.port is not listening
        """

        proxy = Proxy()
        proxy.start()
        proxy.stop()

        assert hubcheck.conf.settings.proxy is None
        assert is_port_listening('localhost',proxy.port) is False
        # stop() doesn't clean up tmp files.
        # assert not os.path.isfile('/tmp/userAgentString.properties')
        # assert not os.path.isfile('/tmp/userAgentString.txt')


    def test_create_client_1(self,proxy):
        """
        create a proxy client on the default port
        """

        # make sure the potential client port is not occupied
        assert not is_port_listening("localhost",proxy.port+1)

        # start the client
        proxy_client = proxy.create_client()

        assert is_port_listening("localhost",proxy.port+1)


    def test_create_client_2(self,proxy):
        """
        create a proxy client on the default port
        """

        # make sure the potential client port is not occupied
        assert not is_port_listening("localhost",proxy.port+1)

        # start the client
        proxy_client = proxy.create_client(proxy.port+1)

        assert is_port_listening("localhost",proxy.port+1)
