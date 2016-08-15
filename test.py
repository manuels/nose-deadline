import time
import unittest

import nose

from nose_timelimit import timelimit, TimelimitExceeded

class TestException(Exception):
    pass

class TestTimelimit(unittest.TestCase):
    @timelimit(2)
    @nose.tools.raises(TimelimitExceeded)
    def test_raise_timeout(self):
        time.sleep(20)
        raise TestException()

    @timelimit(2)
    @nose.tools.raises(TestException)
    def test_raise_other(self):
        raise TestException()

    @timelimit(2)
    def test_pass(self):
        time.sleep(1)

#if __name__ == '__main__':
#    from nose_timelimit import TimelimitPlugin
#    nose.main(addplugins=[TimelimitPlugin()])
