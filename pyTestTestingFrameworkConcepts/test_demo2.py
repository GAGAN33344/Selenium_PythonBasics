# Any pytest file should start with test_ or end with _test keyword
# pytest method names should start with test
# Any code should be wrapped in method only
# Methods name should have sense
# -k stands for method names execution, -s logs in out put, -v stands for more info metadata
# we can run specific file with py.test <filename> through cmd
# we can mark(tag) test @pytest.mark.smoke and then run with -m
# we can skip test with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used for setup and tear down methods for test cases - conftest file to generalize
# fixture and make it available to all test cases

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test fail due to strings unmatched"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition don not match"
