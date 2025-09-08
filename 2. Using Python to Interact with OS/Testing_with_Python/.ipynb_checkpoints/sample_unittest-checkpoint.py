import unittest

# Simple Cake class
class Cake:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: str):
        self.toppings.append(topping)

    def check_price(self) -> float:
        return self.base_price + len(self.toppings)  # Each topping adds 1


class TestCake(unittest.TestCase):

    def test_create_cake(self):
        cake = Cake("Vanilla", 8)
        self.assertEqual(cake.name, "Vanilla")
        self.assertEqual(cake.base_price, 8)
        self.assertEqual(len(cake.toppings), 0)

    def test_add_topping(self):
        cake = Cake("Chocolate", 10)
        cake.add_topping("sprinkles")

        self.assertIn("sprinkles", cake.toppings)
        self.assertEqual(len(cake.toppings), 1)

    def test_check_price(self):
        cake = Cake("Vanilla", 8)
        cake.add_topping("sprinkles")
        cake.add_topping("cherries")
        
        self.assertEqual(cake.check_price(), 10)  # 8 + 2 toppings

# Run the tests
if __name__ == "__main__":
    unittest.main()
