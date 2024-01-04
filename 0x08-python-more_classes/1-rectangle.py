#!/usr/bin/python3
""" Define a Class rectangle """


class Rectangle():
    """A class that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """
        A method that initializes rectangle with height and width
        param:
            Height: height of the rectangle
            Width: width of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        retrives attributes.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets attributes.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """
        retrieves attributes.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets attributes.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
