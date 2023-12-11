#!/usr/bin/python3
"""Unittest for base class"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
        def test__init__with_int_id(self):
            base_instance = Base(id=42)
            self.assertEqual(base_instance.id, 42)

        def test_init_without_id(self):
            base_instance = Base()
            self.assertEqual(base_instance.id, 1)

        def test__init__with_float_id(self):
            base_instance = Base(id=4.2)
            self.assertEqual(base_instance.id, 4.2)

        def test__init__with_string_id(self):
            base_instance = Base(id="id")
            self.assertEqual(base_instance.id, "id")

        def test__init__with_list_id(self):
            base_instance = Base(id=[1, 2, 3])
            self.assertEqual(base_instance.id, [1, 2, 3])
        
        def test__init__with_tuple_id(self):
            base_instance = Base(id=(1, 2, 3))
            self.assertEqual(base_instance.id, (1, 2, 3))

        def test__init__with_bool_id(self):
            base_instance = Base(id=True)
            base_instance = Base(id=False)
            self.assertEqual(base_instance.id, True)
            self.assertEqual(base_instance.id, False)

        def test__init__with_dict_id(self):
            base_instance = Base(id={"key": "value"})
            self.assertEqual(base_instance.id, {"key": "value"})

        def test__init__with_set_id(self):
            base_instance = Base(id=98)
            self.assertEqual(base_instance.id, 98)

        def test_to_json_string_empty_list(self):
            base_instance = Base(id=1)
            result = base_instance.to_json_string([])
            self.assertEqual(result, "[]")

        def test_to_json_string_with_dicts(self):
            base_instance = Base(id=1)
            input_list = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
            result = base_instance.to_json_string(input_list)
            expected_result = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
            self.assertEqual(result, expected_result)

        def test_from_json_string_empty_string(self):
            base_instance = Base(id=1)
            result = base_instance.from_json_string("")
            self.assertEqual(result, [])

        def test_from_json_string_valid_string(self):
            base_instance = Base(id=1)
            input_string = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
            result = base_instance.from_json_string(input_string)
            expected_result = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
            self.assertEqual(result, expected_result)
             

if __name__ == "__main__":
        unittest.main()
