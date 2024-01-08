#!/usr/bin/python3
""" Define a Class MyInt """


class MyInt(int):
    """ A subclass of  class int"""

    def __new__(cls, *args, **kwargs):
        """initializes rectangle with height and width"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Invert the behavior of the equality operator"""
        return int(self) != other

    def __ne__(self, other):
        """Invert the behavior of the inequality operator"""
        return int(self) == other
