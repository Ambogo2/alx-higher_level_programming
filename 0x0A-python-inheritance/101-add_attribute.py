#!/usr/bin/python3
"""A module for add_attribute."""


def add_attribute(obj, attribute, value):
    """
        A function that adds a new attribute
        args:
            Args:
                obj: The object to which the attribute should be added.
                attribute: The name of the attribute.
                value: The value of the attribute.

        Raises:
            TypeError: If the object can't have a new attribute.
        """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    
    obj.__dict__[attribute] = value
