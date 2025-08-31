class Cake:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: str):
        self.toppings.append(topping)

    def check_price(self) -> float:
        return self.base_price + len(self.toppings)  # Each topping adds 1

import pytest
# Create a Calculator object 
@pytest.fixture
def cake():
    return Cake("vanilla", 8)

# Test functions of the object Calculator
def test_add_topping(cake):
    cake.add_topping("chocolate")

    assert "chocolate" in cake.toppings

def test_multiply(cake):
    cake.add_topping("chocolate")

    assert cake.check_price() == 9
