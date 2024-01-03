"""
class Person
    __init__
        name str
        lastname str
        recovered_data bool (starts false)
        
    API:
        recovered_all_data -> method
            OK
            404
            
            (recovered_data become True if recovered data successful)
"""

try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../myfiles'
            )
        )
    )
except:
    raise


import unittest
from Person import Person
# Import fake data
from unittest.mock import patch

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Jorge', 'Aragão')
        
    def test_person_attr_name_has_right_value(self):
        self.assertEqual(self.p1.name, 'Jorge')
           
    def test_person_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        
    def test_person_attr_lastname_has_right_value(self):
        self.assertEqual(self.p1.lastname, 'Aragão')
        
    def test_person_attr_lastname_is_str(self):
        self.assertIsInstance(self.p1.lastname, str)
        
    def test_person_attr_obtained_data_starts_false(self):
        self.assertFalse(self.p1.recovered_data)
        
    def test_recovered_all_data_success_ok(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.recovered_all_data(), 'Connected')
            self.assertTrue(self.p1.recovered_data)
                        
    def test_recovered_all_data_fail_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            
            self.assertEqual(self.p1.recovered_all_data(), 'Error 404')
            self.assertFalse(self.p1.recovered_data)
            
    def test_recovered_all_data_success_and_fail_sequence(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.recovered_all_data(), 'Connected')
            self.assertTrue(self.p1.recovered_data)
            
            fake_request.return_value.ok = False
                
            self.assertEqual(self.p1.recovered_all_data(), 'Error 404')
            self.assertFalse(self.p1.recovered_data)
            
            
if __name__ == '__main__':
    unittest.main(verbosity=2)