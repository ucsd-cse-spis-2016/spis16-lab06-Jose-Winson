# test_pyfuncs01.py

import unittest # this is so we can set up testing of functions

# the imports below import the functions we want to test

from pyfuncs01 import perimRect
from pyfuncs01 import areaRect

class TestPyFuncs01(unittest.TestCase):   # How you do testing in Python

    # Every test case should be a function definition
    # The name should start with test_ and the parameter should be "self".
    # Then, you can write tests using self.assertEqual(actual, expected) and 
    # self.assertAlmostEquals(actual, expected, numberOfDecimalPlaces)
    #
    # If an answer should be exact, use assertEqual
    # If an answer is approximate (floating pt math, square roots, pi, etc.)
    #    use assertAlmostEqual

    def test_perimRect1(self):
        self.assertAlmostEqual(perimRect(2,3), 10)
        # accurate to seven decimal places (default)

    def test_perimRect2(self):
        self.assertAlmostEqual(perimRect(4,2.5), 13.0, 2) 
        # accurate to two decimal places

    def test_perimRect3(self):
        self.assertAlmostEqual(perimRect(3,3), 12)
        # accurate to seven decimal places (default)

    ### @@@ TODO @@@ 
    ### ADD THREE TEST CASES for areaRect here.
    ### Use self.assertAlmostEqual


# This code says: when you run this file, run the tests!

if __name__ == '__main__':
    unittest.main(exit=False)
