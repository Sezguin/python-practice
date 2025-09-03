import unittest
from app.inventory import Inventory
from app.car import Car

class TestSomething(unittest.TestCase):
    def test_assertion(self):
        self.assertTrue(True)

class TestInventory(unittest.TestCase):
    def test_add_car(self):

        # Given
        inv = Inventory()
        car = Car(
            name='test_car',
            year=1996,
            price_pence=1000,
            colour='green'
        )

        # When
        car_added = inv.add_car(car.name, car.year, car.price_pence, car.colour)

        # Then
        found = inv.find(car.name)
        self.assertIs(found, car_added)
        self.assertIn(car_added, inv.all())

if __name__ == "__main__":
    unittest.main()
