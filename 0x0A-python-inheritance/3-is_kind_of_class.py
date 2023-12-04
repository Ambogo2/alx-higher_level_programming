#!/usr/bin/python3
"""A module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: a function that checks if object instance is of as class or subclass
    args:
        obj: object
        a_class: class
    Return:True is onject is class instance, false otherwise.
    """
    return isinstance(obj, a_class)
