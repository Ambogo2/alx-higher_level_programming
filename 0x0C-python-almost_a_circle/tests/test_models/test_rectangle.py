#!/usr/bin/python3
"""unittest for testing rectangle."""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """unittests for testing Rectangle class instantiation."""
    def test_with_valid_arguments(self):
        rect = Rectangle(width=12, height=5, x=2, y=7, id=1)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 1)

class TestRectangle_area(unittest.TestCase):
    """unitests for testing area method."""
    def test_area_small(self):
        rect = Rectangle(12, 10, 0, 0)
        self.assertEqual(120, rect.area())
    
    def test_area_large(self):
        rect = Rectangle(12000000, 10000000, 0, 0)
        self.assertEqual(120000000000000, rect.area())


if __name__ == '__main__':
    unittest.main()