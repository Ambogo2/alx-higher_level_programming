#!/usr/bin/python3
"""Module containing square subclass that inherits from rectangle"""
from models.base import Rectangle


class Square(Rectangle):
    """Child class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances of square class"""
        super().__init__(size, size x, y, id)
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

    def __str__(self):
        """returns string representation of square instance"""
        return "[Square] ({}) {}/{} - {} {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes using args and kwargs"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Converts class instance of square to a dictionary"""
        return {'id': self.id, 'width': self.size,
                'x': self.x, 'y': self.y}
