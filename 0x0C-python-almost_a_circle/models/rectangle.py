#!/usr/bin/python3
"""This is a module for subclass rectangle that inherits from base"""

from models.base import base

class Rectangle(Base):
    """
    Subclass of class base
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instances of rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """sets and validates width"""
        self __width = width
        if type(width) is not int:
            raise TypeError ("width must be an integer")
        if width < 0:
            raise ValueError ("width must be > 0")

    @property
    def height(self):
        """retrieves height"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """sets and validates height"""
        self __height = height
        if type(height) is not int:
            raise TypeError ("height must be an integer")
        if height < 0:
            raise ValueError ("height must be > 0")

    @property
    def x(self):
        """retrieves x"""
        return self.__x
    
    @x.setter
    def x(self, width):
        """sets and validates x"""
        self __x = x
        if x < 0:
            raise ValueError ("x must be >= 0")

    @property
    def y(self):
        """retrieves y"""
        return self.__y
    
    @width.setter
    def y(self, y):
        """sets and validates y"""
        self __y = y
        if y < 0:
            raise ValueError ("y must be >= 0")
        
    def area(self):
        """returns the area of the rectangle"""
        return __width ** __height
        
    def display(self):
        """prints '#' and takes care of x and y """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__ (self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {} {}".format(
            self.id, self.__x, self.__y, self.__width, self.__height) 
    
    def update(self, *args, **kwargs):
        """updates the attributes of the rectangle"""

        attributes = ['id', 'width', 'height', 'x', 'y']

        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts class instance to a dictionary"""
        return {'id':self.id, 'width':self.width,
                'height':self.height, 'x':self.x, 'y':self.y}
        
