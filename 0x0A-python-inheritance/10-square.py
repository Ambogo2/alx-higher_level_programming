#!/usr/bin/python3
""" Defines a Class that inherits from Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
rectangle = __import__('9-rectangle').rectangle


class Square(Rectangle):
    """A subclass of rectangle."""
    def __init__(self, size):
        """
        initializes a square with size
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area: area of a square"""
        return super().area()
