import unittest
from app.car import Car
from app.settings import Settings

class TestSomething(unittest.TestCase):
    def test_assertion(self):
        self.assertTrue(True)

class TestCarWorkings(unittest.TestCase):
    def test_apply_percentage_discount(self):

        # Given
        car = Car(
            name='test_car',
            year=1995,
            price_pence=1000,
            colour='blue'
          )
        car_discount = 50

        # When
        car.apply_percentage_discount(car_discount)

        # Then
        self.assertEqual(car.price_pence, 500)

if __name__ == "__main__":
    unittest.main()
