import unittest
from calculations import Calculations

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.getSum(), 10, 'The sum is wrong')

    def test_diff(self):
        self.assertEqual(self.calculation.getDifference(), 6, 'The difference is wrong')

    def test_product(self):
        self.assertEqual(self.calculation.getProduct(), 16, 'The product is wrong')

    def test_quotient(self):
        self.assertEqual(self.calculation.getQuotient(), 4, 'The quotient is wrong')


if __name__ == '__main__':
    unittest.main()