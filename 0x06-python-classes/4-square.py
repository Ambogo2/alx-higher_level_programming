#!/usr/bin/python3
"""Define a class"""


class Square:
    """
    A class that defines a square."""
    def __init__(self, size=0):
        """
        initializes a square witha given size.
        arg:
            size: the size of the square.
        """
        self.size = size

    @property
    def size(self):

        """
        gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):

        """
        sets the size of square
        args:
            value: the new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        size.self = value

    def area(self):
        """
        returns the current area of a square.
        """
        return self.__size*self.__size
