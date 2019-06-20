#############################
#### SIMPLE #################
#############################

import unittest      
 
class TestMyCode(unittest.TestCase):   
    def test_addition_2_2(self):    
        self.assertEqual(2+2, 5)   
    def test_subtraction_2_2(self): 
        self.assertNotEqual(2-2, 4)   
 
unittest.main()        

#############################
#### TEST FUNCS #############
#############################

import unittest
import funcs
 
class TestPrime(unittest.TestCase):
    def test_prime_5(self): 
        isprime = funcs.is_prime(5)
        self.assertEqual(isprime, True) 
    def test_prime_4(self):
        isprime = funcs.is_prime(4)
        self.assertEqual(isprime, False)
    def test_prime_10000(self):
        isprime = funcs.is_prime(10000)
        self.assertEqual(isprime, False)
        
class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = funcs.absolute_value(5)
        self.assertEqual(absolute, 5)
    def test_abs_neg5(self):
        absolute = funcs.absolute_value(-5)
        self.assertEqual(absolute, 5)
    def test_abs_0(self):
        absolute = funcs.absolute_value(0)
        self.assertEqual(absolute, 0)
        
unittest.main() 
