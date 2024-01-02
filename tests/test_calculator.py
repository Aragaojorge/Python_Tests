import unittest
from myfiles import calculator

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self):
        self.assertEqual(calculator.sum(5,5), 10)
    
    def test_sum_5_negative_and_5_should_return_0(self):
        self.assertEqual(calculator.sum(-5,5), 0)
        
    def test_many_values(self):
        x_y_out = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200),
        )
        
        for x_y_out in x_y_out:
            with self.subTest(x_y_out=x_y_out):
                x, y, out = x_y_out
                self.assertEqual(calculator.sum(x, y), out)
                
    def test_sum_x_not_int_or_float_should_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            calculator.sum('11', 0)
            
    def test_sum_y_not_int_or_float_should_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            calculator.sum(11, '0')

if __name__ == '__main__':
    unittest.main(verbosity=2)