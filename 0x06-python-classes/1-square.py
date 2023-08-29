#!/usr/bin/python3
class Square:
    """
    A class that defines a square.

    This is an empty class that defines a square.
    """
    def __init__(self, size):
        """
        A method that initializes the square with size.
        :param size: size of a square.
        """
        try:
            self.__size = size
        except Exception as e:
            print("Error occured", e)
