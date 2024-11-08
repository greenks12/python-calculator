import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 7), 12)
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(15, 8), 7)
        self.assertEqual(self.calc.subtract(-2, 7), -9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(6, 4), 24)

    def test_divide(self):
        self.assertEqual(self.calc.divide(35, 5), 7)
        self.assertEqual(self.calc.divide(27, 3), 9)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(13, 4), 1)
        self.assertEqual(self.calc.modulo(10, 4), 2)

if __name__ == '__main__':
    unittest.main()