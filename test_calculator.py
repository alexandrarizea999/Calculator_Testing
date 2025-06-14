# test file for my calculator

# import the libraries i need
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    # testing the add function
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    # testing the substract function
    def test_subtract(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(-1, -1), 0)

    # testing the multiply function
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 0), 0)

    # testing the divide function
    # make sure we test the error for dividing by 0
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-1, 1), -1)

        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
