#!/usr/bin/python3
"""Unittest for square class"""
import io
import sys
from models.base import Base
from models.rectangle import Square
import unittest


class TestSquare(unittest.TestCase):
    def test_init(self):
        square_instance = Square(size=5, x=2, y=3, id=1)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

    def test_str(self):
        square_instance = Square(size=4, x=1, y=2, id=10)
        expected_result = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(square_instance), expected_result)

    def test_update(self):
        square_instance = Square(size=3, x=0, y=0, id=5)
        square_instance.update(id=7, size=6, x=2, y=1)
        self.assertEqual(square_instance.id, 7)
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 1)

    def test_to_dictionary(self):
        square_instance = Square(size=2, x=1, y=3, id=8)
        expected_result = {'id': 8, 'width': 2, 'x': 1, 'y': 3}
        self.assertEqual(square_instance.to_dictionary(), expected_result)

if __name__ == "__main__":
        unittest.main()
