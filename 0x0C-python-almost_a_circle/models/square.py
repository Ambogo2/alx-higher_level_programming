#!/usr/bin/python3
"""Module for class Square."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes instances of square class.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """returns string representation of square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update attributes using args and kwargs"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    setattr(self, 'id', value)
                elif i == 1:
                    setattr(self, 'size', value)
                elif i == 2:
                    setattr(self, 'x', value)
                elif i == 3:
                    setattr(self, 'y', value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts class instance of square to a dictionary"""
        return {
            'id': self.id,
            'width': self.size,
            'x': self.x,
            'y': self.y}
