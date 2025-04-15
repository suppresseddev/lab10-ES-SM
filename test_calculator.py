# https://github.com/suppresseddev/lab10-ES-SM
# Partner 1: Eli Simon
#Partner 2: Santiago Mena

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(3,5),15)
        self.assertEqual(mul(-2,4),-8)
        self.assertEqual(mul(2.5,-2),-5)
    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_divide(self):
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(-40,5),-8)
        self.assertAlmostEqual(div(6.6,6),1.1)
    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_arguement(self):
        with self.assertRaises(ValueError):
            logarithm(0,5)
    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(2,3),(sqrt((2 ** 2) + (3 ** 2))))
        self.assertAlmostEqual(hypotenuse(8, 5), (sqrt((8 ** 2) + (5 ** 2))))
        self.assertAlmostEqual(hypotenuse(5, -10), (sqrt((5 ** 2) + (-10 ** 2))))
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(3),(3 ** (1/2)))
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(36),6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()