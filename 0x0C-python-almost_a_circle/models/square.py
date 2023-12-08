#!/usr/bin/python3
"""Module containing square subclass that inherits from rectangle"""

from models.base import rectangle

class Square(Rectangle):
    """Child class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances of square class"""
        super().__init__(size,size x, y,id,)
        self.size = size

    @property
    def size(self):
        """retrieves attributes from rectangle class"""
        return self.width
    
    @size.setter
    def size(self, value):
        """sets and validates from rectangle class"""
        self.width = value
        self.height = value

    def __str__ (self):
        """returns string representation of square instance"""
        return "[Square] ({}) {}/{} - {} {}".format(
            self.id, self.x, self.y, self.width) 

