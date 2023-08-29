#!/usr/bin/python3
"""Define a class"""


class Square:
    """
    A class that defines a square.
    This is an empty class that defines a square.
    """
    def __init__(self, size=0):
        """
        A method that initializes the square with size
        param:
            size(int): size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size == 0:
            raise ValueError("size must be >= 0")
        self.__size = size
