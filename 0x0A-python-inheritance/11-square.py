#!/usr/bin/python3
""" Defines a Class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from rectangle.
    """
    def __init__(self, size):
        """
         A method that initializes a square with size
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area: area of a square
        """
        return super().area()

    def __str__(self) -> str:
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    square = Square(4)
    print(square)
    print(f"Area: {square.area()}")
