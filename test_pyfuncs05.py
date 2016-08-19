# test_pyfuncs05.py

import unittest 

from pyfuncs05 import totalValue
from pyfuncs05 import productOfAll
from pyfuncs05 import isOdd
from pyfuncs05 import isEven
from pyfuncs05 import countOdds
from pyfuncs05 import sumOdds

class TestPyFuncs05(unittest.TestCase):   

    # tests for totalValue

    def test_totalValue_1(self):
        self.assertEqual( totalValue([]),0)

    def test_totalValue_2(self):
        self.assertEqual( totalValue([2]),2)

    def test_totalValue_3(self):
        self.assertEqual( totalValue((10,20,30)),60)

    def test_totalValue_4(self):
        self.assertEqual( totalValue((10,20,30,-5)),55)

    def test_totalValue_5(self):
        self.assertEqual( totalValue([1.0,0.2,0.03]),1.23)

    def test_totalValue_6(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = totalValue(12)

    def test_totalValue_7(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = totalValue("UCSD")

    # tests for productOfAll

    def test_productOfAll_1(self):
        self.assertEqual( productOfAll([]),1)

    def test_productOfAll_2(self):
        self.assertEqual( productOfAll([2]),2)

    def test_productOfAll_3(self):
        self.assertEqual( productOfAll((10,20,30)),6000)

    def test_productOfAll_4(self):
        self.assertEqual( productOfAll((10,20,30,-5)),-30000)

    def test_productOfAll_5(self):
        self.assertEqual( productOfAll([1.0,0.2,0.03]),0.006)

    def test_productOfAll_6(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = productOfAll(12)

    def test_productOfAll_7(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = productOfAll("UCSD")


    # tests for isOdd

    def test_isOdd_1(self):
        self.assertFalse(isOdd(0))

    def test_isOdd_2(self):
        self.assertTrue(isOdd(1))

    def test_isOdd_3(self):
        self.assertFalse(isOdd(10))

    def test_isOdd_4(self):
        self.assertTrue(isOdd(21))

    def test_isOdd_5(self):
        self.assertFalse(isOdd(-10))

    def test_isOdd_6(self):
        self.assertTrue(isOdd(-21))

    def test_isOdd_7(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = isOdd("UCSD")

    def test_isOdd_8(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = isOdd([1])

    # tests for isEven

    def test_isEven_1(self):
        self.assertTrue(isEven(0))

    def test_isEven_2(self):
        self.assertFalse(isEven(1))

    def test_isEven_3(self):
        self.assertTrue(isEven(10))

    def test_isEven_4(self):
        self.assertFalse(isEven(21))

    def test_isEven_5(self):
        self.assertTrue(isEven(-10))

    def test_isEven_6(self):
        self.assertFalse(isEven(-21))

    def test_isEven_7(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = isEven("UCSD")

    def test_isEven_8(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = isEven([2])

    # tests for countOdds

    def test_countOdds_1(self):
        self.assertEqual( countOdds([]),0)

    def test_countOdds_2(self):
        self.assertEqual( countOdds([2]),0)

    def test_countOdds_3(self):
        self.assertEqual( countOdds([3]),1)

    def test_countOdds_4(self):
        self.assertEqual( countOdds((10,21,30)),1)

    def test_countOdds_5(self):
        self.assertEqual( countOdds((10,21,30,43)),2)

    def test_countOdds_6(self):
        self.assertEqual( countOdds((17,21,39,43)),4)

    def test_countOdds_7(self):
        self.assertEqual( countOdds((10,20,30,44)),0)

    def test_countOdds_8(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = countOdds(12)

    def test_countOdds_9(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = countOdds("UCSD")
    

   
# This code says: when you run this file, run the tests!

if __name__ == '__main__':
    unittest.main(exit=False)
