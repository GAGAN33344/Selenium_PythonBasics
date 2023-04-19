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
# data-driven & parameterization can be done with return statements in tuple format
# when we define fixture scope to class only, It will run once before class is initiated and at the end

import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondgoodMorningCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
     print(crossBrowser[1])

