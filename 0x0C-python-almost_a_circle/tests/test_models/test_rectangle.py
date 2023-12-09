#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

        def test_init_with valid args(self):
        rect = Rectangle(width=3, height=10, x=1, y=2, id=1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 1)

if __name__ == "__main__":
        unittest.main()
