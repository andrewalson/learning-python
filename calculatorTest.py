import unittest
import calculator

class CalculatorTest(unittest.TestCase):
    
    def test_add_adds_two_numbers(self):
        self.assertEqual(calculator.add(5,6), 11)
        self.assertEqual(calculator.add(12,13), 25)

    def test_add_two_strings_returns_number(self):
        self.assertEqual(calculator.add('1', "2"), 3)

    def test_subtract_subtracts_two_numbers(self):
        self.assertEqual(calculator.subtract(6,5), 1)
        self.assertEqual(calculator.subtract(7,2), 5)

    def test_subtract_two_strings_returns_number(self): 
        self.assertEqual(calculator.subtract('2', '1'), 1)
        