#!/usr/bin/python3
""" Define a Class rectangle """


class Rectangle:
    """
    A class that defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with width and height.
        Increments number_of_instances during each instantiation.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If width or height is equal to 0, perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.
        """
        if self.__width > 0 or self.__height > 0:
            result = ""
            for i in range(self.__height):
                result += str(self.print_symbol) * self.__width + "\n"
        return result[:-1] 

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints the message "Bye rectangle...".
        Decrements number_of_instances during each instance deletion.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
