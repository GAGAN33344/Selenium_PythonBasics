import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Gagan", "Mann", "rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome", "Gagan"), ("Firefox", "Mann"), ("IE", "SSN")])
def crossBrowser(request):
    return request.param


