import time
import unittest

import nose

from nose_deadline import deadline, DeadlineExceeded

class TestException(Exception):
    pass

class TestDeadline(unittest.TestCase):
    @deadline(2)
    @nose.tools.raises(DeadlineExceeded)
    def test_raise_timeout(self):
        time.sleep(20)
        raise TestException()

    @deadline(2)
    @nose.tools.raises(TestException)
    def test_raise_other(self):
        raise TestException()

    @deadline(2)
    def test_pass(self):
        time.sleep(1)

#if __name__ == '__main__':
#    from nose_deadline import DeadlinePlugin
#    nose.main(addplugins=[DeadlinePlugin()])
