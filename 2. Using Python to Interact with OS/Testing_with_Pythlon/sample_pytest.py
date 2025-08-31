class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

import pytest
# Create a Calculator object 
@pytest.fixture
def calc():
    return Calculator()

# Test functions of the object Calculator
def test_add(calc):
    assert calc.add(2, 3) == 5

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
