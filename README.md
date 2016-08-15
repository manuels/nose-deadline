# nose-timelimit

## Description
Enforced timelimits for nosetests.

## Example

    from nose_timelimit import timelimit

    @timelimit(1)
    def test_sleep():
        import time
        time.sleep(5)

Then run `nosetest --with-timelimit <FILE>` and you will see this error message:

    T
    ======================================================================
    Timelimit exceeded.: test.test_sleep
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      [...]
      File "test.py", line 6, in test_sleep
        time.sleep(5)
      File "/home/schoellingm/tmp/nose-alarm/nose_timelimit.py", line 19, in sig_handler
        raise TimelimitExceeded('Test did not finish within {}sec.'.format(sec))
    nose_timelimit.TimelimitExceeded: Test did not finish within 1sec.

    ----------------------------------------------------------------------
    Ran 1 test in 1.001s

    FAILED (Timelimit exceeded.=1)

## Restrictions
Only works on *nix systems because it needs POSIX signals.

