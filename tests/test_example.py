import unittest
from app.cars import CarClass, Car

class TestSomething(unittest.TestCase):
    def test_assertion(self):
        self.assertTrue(True)

class TestSomethingElse(unittest.TestCase):
    def test_number_assertion(self):
        self.assertEqual(1, 1)

class TestWordMatching(unittest.TestCase):
    def test_word_matching(self):
        self.assertEqual("this", "this")

class TestNumberThings(unittest.TestCase):
    def test_two_number_addition(self):
        # Given
        number_a = 10
        number_b = 5
        example_class = CarClass()

        # When
        result = example_class.add_two_numbers_together(number_a, number_b)

        # Then
        self.assertEqual(result, 15)

class TestCarPriceReduction(unittest.TestCase):
    def test_discounting(self):
        # Given
        test_car = Car(name="test_car", year=1999, price=100, colour="grey")
        car_class = CarClass()

        # When
        car_class.add_car(test_car.name, test_car.year, test_car.price, test_car.colour)

        # And
        car_class.update_car_price(test_car.name)

        # Then
        result = car_class.get_single_car(test_car.name)
        self.assertEqual(result.price, 89)

if __name__ == "__main__":
    unittest.main()
