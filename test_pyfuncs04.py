# test_pyfuncs04.py

import unittest 

from pyfuncs04 import first
from pyfuncs04 import rest
from pyfuncs04 import last
from pyfuncs04 import allButLast

class TestPyFuncs04(unittest.TestCase):   

    # tests for first

    def test_first_1(self):
        self.assertEqual( first("UCSD"),"U")

    def test_first_2(self):
        self.assertEqual( first([2,4,6,8]),2)

    def test_first_3(self):
        self.assertEqual( first((255,0,0)),255)

    def test_first_4(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = first(12)

    def test_first_5(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = first(True)

    # tests for rest

    def test_rest_1(self):
        self.assertEqual( rest("UCSD"),"CSD")

    def test_rest_2(self):
        self.assertEqual( rest([2,4,6,8]),[4,6,8])

    def test_rest_3(self):
        self.assertEqual( rest((255,0,0)),(0,0))

    def test_rest_4(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = rest(12)

    def test_rest_5(self):
        with self.assertRaises(TypeError):
            x = rest(True)

    # tests for last

    def test_last_1(self):
        self.assertEqual( last("UCSD"),"D")

    def test_last_2(self):
        self.assertEqual( last([2,4,6,8]),8)

    def test_last_3(self):
        self.assertEqual( last((255,0,0)),0)

    def test_last_4(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = last(12)

    def test_last_5(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = last(True)

    # tests for allButLast

    def test_allButLast_1(self):
        self.assertEqual( allButLast("UCSD"),"UCS")

    def test_allButLast_2(self):
        self.assertEqual( allButLast([2,4,6,8]),[2,4,6])

    def test_allButLast_3(self):
        self.assertEqual( allButLast((255,0,0)),(255,0))

    def test_allButLast_4(self):
        # This is what a test case looks like when you
        # expect that an error will happen
        with self.assertRaises(TypeError):
            x = allButLast(12)

    def test_allButLast_5(self):
        with self.assertRaises(TypeError):
            x = allButLast(True)

   
# This code says: when you run this file, run the tests!

if __name__ == '__main__':
    unittest.main(exit=False)
