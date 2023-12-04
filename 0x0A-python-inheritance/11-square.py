#!/usr/bin/python3
""" Define a Class BaseGeometry """


class BaseGeometry:
    """ A class that defines BaseGeometry."""
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

    def area(self):
        """
        area: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__: Returns a string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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
