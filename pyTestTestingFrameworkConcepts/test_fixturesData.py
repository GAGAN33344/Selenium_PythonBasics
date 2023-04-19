import pytest

from pyTestTestingFrameworkConcepts.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample(BaseClass):

    def test_editProfile(self, dataload):
        log = self.getLogger() # call this method from BaseClass
        log.info(dataload)
        log.info(dataload[0])