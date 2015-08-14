import unittest
import pytest
import sys

import hubcheck

pytestmark = [ pytest.mark.fail]

class hcunit_failure(hubcheck.testcase.TestCase):

    def test_failure(self):
        """
        a test that will fail
        """

        self.assertFalse(True,"this is an example of a test failure")


if __name__ == '__main__':
    # unittest.main(verbosity=0)
    tr = unittest.TextTestRunner(stream=sys.stdout,verbosity=0)
    unittest.main(testRunner=tr,exit=False)


