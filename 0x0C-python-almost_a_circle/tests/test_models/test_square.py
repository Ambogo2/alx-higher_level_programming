#!/usr/bin/python3
"""unittest for testing Square."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """unittests for testing Square class instantiation."""
    def test_with_valid_arguments(self):
        sqr = Square(size=8, x=2, y=7, id=0)
        self.assertEqual(sqr.size, 8)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 7)
        self.assertEqual(sqr.id, 7)

class TestSquare_area(unittest.TestCase):
    """unitests for testing area method."""
    def test_area_small(self):
        sqr = Square(4, 4, 0, 0)
        self.assertEqual(16, sqr.area())
    
    def test_area_large(self):
        sqr = Rectangle(1000000, 1000000, 0, 0)
        self.assertEqual(1000000000000, sqr.area())


if __name__ == '__main__':
    unittest.main()