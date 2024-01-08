#!/usr/bin/python3
""""A module of inherits_from function"""


def inherits_from(obj, a_class):
    """
    inherits_from:checks if an object is an instance of a class or a subclass.
    args:
        obj: object
        a_class: class
    Return:
        True if the object is an instance.
        False otherwise.
    """
    return issubclass(obj, a_class) and type(obj) is not a_class
