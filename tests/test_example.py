import unittest

class TestSomething(unittest.TestCase):
    def test_assertion(self):
        self.assertTrue(True)

class TestSomethingElse(unittest.TestCase):
    def test_number_assertion(self):
        self.assertEqual(1, 1)

class TestWordMatching(unittest.TestCase):
    def test_word_matching(self):
        self.assertEqual("this", "this")

if __name__ == "__main__":
    unittest.main()
