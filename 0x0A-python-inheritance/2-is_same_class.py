#!/usr/bin/python3
"""A module for is_same_class function"""

def is_same_class(obj, a_class):
    """
    is_same_class: a function that checks if object instance is same as class.
    args:
        obj: object
        a_class: class
    Return:True is object is class instance, false otherwise.
    """
    return type(obj) is a_class
