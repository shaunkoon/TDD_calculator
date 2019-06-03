from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        #syntax assertEqual(#test, #result)
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 4), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
