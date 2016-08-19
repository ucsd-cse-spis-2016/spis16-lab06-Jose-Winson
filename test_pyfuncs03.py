# test_pyfuncs03.py

import unittest 

from pyfuncs03 import isAdditivePrimaryColor
from pyfuncs03 import isSimpleNumeric

class TestPyFuncs03(unittest.TestCase):   

    # tests for isAdditivePrimaryColor

    def test_isAdditivePrimaryColor1(self):
        self.assertEqual( isAdditivePrimaryColor("blue"), True)

    def test_isAdditivePrimaryColor2(self):
        self.assertEqual( isAdditivePrimaryColor("black"),    False)

    def test_isAdditivePrimaryColor3(self):
        self.assertEqual( isAdditivePrimaryColor(42),    False)


    # tests for isSimpleNumeric

    def test_isSimpleNumeric1(self):
        self.assertEqual( isSimpleNumeric(5),   True)

    def test_isSimpleNumeric2(self):
        self.assertEqual( isSimpleNumeric(3.5),   True)

    def test_isSimpleNumeric3(self):
        self.assertEqual( isSimpleNumeric("5"),   False)

    def test_isSimpleNumeric4(self):
        self.assertEqual( isSimpleNumeric([5]),   False)

    def test_isSimpleNumeric5(self):
        self.assertEqual( isSimpleNumeric(6.0221415E23),   True)
   
# This code says: when you run this file, run the tests!

if __name__ == '__main__':
    unittest.main(exit=False)
