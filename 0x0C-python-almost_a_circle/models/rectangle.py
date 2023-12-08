#!/usr/bin/python3

class Rectangle(base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        

