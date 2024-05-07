"""
import unittest
from Calculator import Calculator

def test_sum_from_number():
    calc = Calculator()
    result = calc.sum_form_number(7, 3)
    if result == 10:
        print("test passed!")
    else:
        print("test failed!")
test_sum_from_number()
"""
# Upotreba frameworka unittest
"""
import unittest
from Calculator import Calculator

class test_sum_form_numbers(unittest.TestCase):
    def test_sum_from_number(self):
        calc = Calculator()
        result = calc.sum_form_number(7, 3)
        if result == 10:
            print("Test passed!")
        else:
            print("Test failed!")

unittest.main()
"""
# spovodim unittest bez uslova i na taj nacin ukidama uticaj programera na samu logiku testa.
"""
import unittest
from Calculator import Calculator

class test_sum_firms_numbers(unittest.TestCase):
    def test_sum_from_numbers2(self):
        calc = Calculator()
        result = calc.sum_form_number(7, 3)
        self.assertEquals(result, 7)

unittest.main()
"""
# formiranje vise assert naredbe u okviru jednog testa. on proveri sve testove i ako prepozna gresku u nekom od testova
"""
import unittest
from Calculator import Calculator

class TestSumfromNumbers(unittest.TestCase):
    def test_sum_from_numbers(self):
        calc = Calculator()
        result = calc.sum_form_number(7, 3)
        expected = 10
        self.assertEqual(result, expected)
        self.assertNotEqual(result, expected)
        self.assertGreaterEqual(result, expected)

unittest.main()
"""
# praviim grupe testova test suit.
"""
import unittest
from Calculator import Calculator


class TestSumfromNumbers(unittest.TestCase):
    def test_sum_from_number(self):
        calc = Calculator()
        result = calc.sum_form_number(3, 7)
        expected = 10
        self.assertEqual(result, expected)
        self.assertNotEqual(result, expected)
        self.assertGreaterEqual(result, expected)

def suit():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSumfromNumbers))
    return test_suite
my_suite = suit()
runner = unittest.TextTestRunner()
runner.run(my_suite)
"""
# Grupa testova test_suit sa vise metoda i vise testova

import unittest

class Calculator:
    def sum_from_numbers(self, firnst_number, second_number):
        result = firnst_number + second_number
        return result
    
class TestSumFromNumbers(unittest.TestCase):
    def test_is_corect(self):
        calc = Calculator()
        result = calc.sum_from_numbers(7, 3)
        expected = 10
        self.assertEqual(result, expected)
    
    def test_is_negative(self):
        calc = Calculator()
        result = calc.sum_from_numbers(-4, 1)
        expected = 0
        self.assertLess(result, expected)
    
    def test_is_greater(self):
        calc = Calculator()
        result = calc.sum_from_numbers(7, 3)
        expected = 10
        self.assertGreaterEqual(result, expected)

def suit():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSumFromNumbers))
    return test_suite

mySuit = suit()

runner = unittest.TextTestRunner()
runner.run(mySuit)