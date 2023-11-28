#!/usr/bin/python3
"""
This is a unittest file for finding the maximum integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax_integer(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_duplicates(self):
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-2, -1, -9, -6]), -1)
    def test_positive_numbers(self):
        self.assertEqual(max_integer([7, 10, 4, 8]), 10)
    def test_one_value(self):
        self.assertEqual(max_integer([8]), 8)
    def test_mixed_positives_negatives(self):
        self.assertEqual(max_integer([8, -1, 2, 9]), 9)
    def test_mixed_datatypes(self):
        with self.assertRaises(TypeError):
            max_integer([2, "Hello"])
    def test_float_ints(self):
        self.assertEqual(max_integer([1.2, 3, 5.7, 9]), 9)
    def test_ordered_list(self):
        self.assertEqual(max_integer([11, 12, 13, 14]), 14)
    def test_unordered_list(self):
        self.assertEqual(max_integer([12, 15, 4, 1]), 15)
    def test_string(self):
        self.assertEqual(max_integer("Happy"), 'y')


if __name__ == '__main__':
    unittest.main()