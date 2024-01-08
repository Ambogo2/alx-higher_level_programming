#!/usr/bin/python3
""" Define a Class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry."""
    def __init__(self, width, height):
        """
        A method that initializes rectangle with height and width.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        area: area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__: Returns a string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
