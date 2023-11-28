#!/usr/bin/python3
"""
This module is made up of a function that prints a square.
"""


def print_square(size):
    """
    A function that prints a square.
    Args:
        Size:The length of the square
    Returns:
        A square
    Raises:
        TypeError if size is not an integer or float and is less than 0
        ValueError if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
