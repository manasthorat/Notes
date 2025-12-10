import pytest
from main import Calculator

@pytest.fixture(scope="class")
def calc():
    print("\nCreate Calculator")
    return Calculator()

class TestCalc:
    def test_add1(self, calc):
        assert calc.add(1, 2) == 3

    def test_add2(self, calc):
        assert calc.add(2, 3) == 5
