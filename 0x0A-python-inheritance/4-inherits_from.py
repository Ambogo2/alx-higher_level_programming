#!/usr/bin/python3
    """"
    A module of inherits_from function
    """


def inherits_from(obj, a_class):
    """
    inherits_from: a function that checks if an object is an instance of a class or a subclass.
    args:
        obj: object
        a_class: class
    Return: True if the object is an instance of the specified class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
