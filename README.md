# nose-deadline

## Description
Enforced timelimits for nosetests.

## Example

    from nose_deadline import deadline

    @deadline(1)
    def test_sleep():
        import time
        time.sleep(5)

Then run `nosetest --with-deadline <FILE>` and you will see this error message:

    T
    ======================================================================
    Deadline exceeded.: test.test_sleep
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      [...]
      File "test.py", line 6, in test_sleep
        time.sleep(5)
      File "/home/schoellingm/tmp/nose-alarm/nose_deadline.py", line 19, in sig_handler
        raise DeadlineExceeded('Test did not finish within {}sec.'.format(sec))
    nose_deadline.DeadlineExceeded: Test did not finish within 1sec.

    ----------------------------------------------------------------------
    Ran 1 test in 1.001s

    FAILED (Deadline exceeded.=1)

## Restrictions
Only works on *nix systems because it needs POSIX signals.

