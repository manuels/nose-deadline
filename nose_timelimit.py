import logging
import signal
from functools import wraps

from nose.plugins.errorclass import ErrorClassPlugin, ErrorClass

logger = logging.getLogger(__name__)

class TimelimitExceeded(Exception):
    pass

class TimelimitPlugin(ErrorClassPlugin):
    timelimit = ErrorClass(TimelimitExceeded, label='Timelimit exceeded.', isfailure=True)


def timelimit(sec):
    """Unix-like operating systems do not support milliseconds, so `sec` must be of type int."""
    def sig_handler(signum, frame):
        raise TimelimitExceeded('Test did not finish within {}sec.'.format(sec))

    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwds):
            # enable alarm
            signal.signal(signal.SIGALRM, sig_handler)
            old_timeout = signal.alarm(sec)

            if old_timeout != 0:
                logger.critical('TimelimitPlugin installed a new SIGALRM timer, but there was a previous timer installed! This timer was overwritten!')

            try:
                result = func(*args, **kwds)
            finally:
                # disable alarm
                old_timeout = signal.alarm(0)

            return result
        return func_wrapper
    return decorator
