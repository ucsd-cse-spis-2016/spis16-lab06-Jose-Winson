# test_pyfuncs02.py

import unittest 


from pyfuncs02 import isList
from pyfuncs02 import isString

class TestPyFuncs02(unittest.TestCase):  


    # If an answer should be exact, use self.assertEqual
    # If an answer is approximate (floating pt math, square roots, pi, etc.)
    #    use self.assertAlmostEqual

    def test_isList1(self):
        self.assertEqual( isList(3),   False)

    def test_isList2(self):
        self.assertEqual( isList([3]),   True)

    def test_isList3(self):
        self.assertEqual( isList([5,10,15,20]),   True)

    def test_isList4(self):
        self.assertEqual( isList("foo"),   False)

    def test_isList5(self):
        self.assertEqual( isList(["John","Paul","Ringo","George"]),   True)

    def test_isList6(self):
        self.assertEqual( isList([]),   True)


    ### @@@ HERE, WRITE FOUR TEST CASES FOR isString
    ### @@@   one for a string of length 0, 
    ### @@@   one for a string of length 4,
    ### @@@   two values that are not strings.


if __name__ == '__main__':
    unittest.main(exit=False)
