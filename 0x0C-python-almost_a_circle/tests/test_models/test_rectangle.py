#!/usr/bin/python3
"""Unittest for rectangle class"""

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

    def test_width_setter(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.width = 8
        self.assertEqual(rect.width, 8)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_setter(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.height = 12
        self.assertEqual(rect.height, 12)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -8

    def test_x_setter(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.x = 4
        self.assertEqual(rect.x, 4)

        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y_setter(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.y = 7
        self.assertEqual(rect.y, 7)

        with self.assertRaises(ValueError):
            rect.y = -3

    def test_area(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(5, 3, 1, 2, 1)
        expected_output = "\n     #####\n     #####\n     #####"
        with self.assertLogs(level="INFO") as logs:
            rect.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5 10"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 8, 6, 4, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 2)

        rect.update(width=12, y=7)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.y, 7)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == "__main__":
        unittest.main()
