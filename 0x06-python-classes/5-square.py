#!/usr/bin/python3
"""Define a class"""


class Square:

    """A class that defines a square"""

    def __init__(self, size=0):
        """
        initializes a square witha given size.
        arg:
            size: the size of the square.
        """
        self.size = size

    @property
    def size(self):

        """gets the size of the square"""
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
        elif size < 0:
            raise ValueError("size must be >= 0")
        size.__self = value

    def area(self):
        """returns the current area of a square with # character."""

        return self.__size*self.__size

    def my_print(self):
        """prints the square"""

        for i in range(0, self._size):
            [print('#', end="")for j in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
