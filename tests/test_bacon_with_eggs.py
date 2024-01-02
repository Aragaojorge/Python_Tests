"""

TDD - Test Driven Develpoment

Red
Part 1 -> Create the test and see if fail

Green
Part 2 -> Create the code and see it the test pass

Refactor
Part 3 -> improve your code
 
"""

import unittest
from myfiles import baconwitheggs


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_should_raise_assertion_error_if_do_not_receive_int(self):
        with self.assertRaises(AssertionError):
            baconwitheggs.bacon_with_eggs('')
            
    def test_bacon_with_eggs_should_return_bacon_wth_eggs_if_input_is_multiple_of_3_and_5(self):
        
        inputs = (15, 30, 45, 60)
        output = 'Bacon with eggs'
        
        for input in inputs:
            with self.subTest(input = input, output = output):
                self.assertEqual(
                    baconwitheggs.bacon_with_eggs(input),
                    output,
                    msg = f'"{input}" did not return "{output}"'
                )
                
    def test_bacon_with_eggs_should_starve__if_input_is_not_a_multiple_of_3_and_5(self):
       
        inputs = (1, 2, 4, 7, 8)
        output = 'Starve'
            
        for input in inputs:
            with self.subTest(input = input, output = output):
                self.assertEqual(
                    baconwitheggs.bacon_with_eggs(input),
                    output,
                    msg = f'"{input}" did not return "{output}"'
                )
                    
    def test_bacon_with_eggs_should_return_bacon_if_input_is_multiple_of_3(self):
        
        inputs = (3, 6, 9, 12, 18, 21)
        output = 'Bacon'
            
        for input in inputs:
            with self.subTest(input = input, output = output):
                self.assertEqual(
                    baconwitheggs.bacon_with_eggs(input),
                    output,
                    msg = f'"{input}" did not return "{output}"'
                )
                
    def test_bacon_with_eggs_should_return_bacon_if_input_is_multiple_of_3(self):
        
        inputs = (5, 10, 20, 25, 35)
        output = 'Eggs'
            
        for input in inputs:
            with self.subTest(input = input, output = output):
                self.assertEqual(
                    baconwitheggs.bacon_with_eggs(input),
                    output,
                    msg = f'"{input}" did not return "{output}"'
                )
                
if __name__ == '__main__':
    unittest.main(verbosity=2)    