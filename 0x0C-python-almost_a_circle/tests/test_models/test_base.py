#!/usr/bin/python3
""" Unittest for testing base class."""


import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """unittests for testing base class instantiation."""
    def test_int_id(self):
        obj = Base(id=42)
        result = obj.id
        self.assertEqual(result, 42)

    def test_bool_id(self):
        obj_true = Base(id=True)
        obj_false = base(id=False)
        result_true = obj_true.id
        result_false=obj_false.id
        self.assertion(result_true, True)
        self.assertEqual(result_false, False)
        
    def test_float_id(self):
        obj = Base(id=4.2)
        result = obj.id
        self.assertEqual(result, 4.2)

    def test_list_id(self):
        obj = Base(id=[1, 2, 3])
        result = obj.id
        self.assertEqual(result, [1, 2, 3])
        
    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id -1)

class TestBase_to_json_string(unittest.TestCase):
    """unittest for testing to json sring."""
    


if __name__ == '__main__':
    unittest.main()
