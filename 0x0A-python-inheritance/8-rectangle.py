#!/usr/bin/python3
""" Define a Class BaseGeometry """


class BaseGeometry:
    """ A class that defines BaseGeometry."""
    def area(self):
        """
        area: area of geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator: validates if a given value is an integer
        args:
            name: name
            value: value
        return:
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that inherits."""
    def __init__(self, width, height):
        """
        A method that initializes rectangle with height and width
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
