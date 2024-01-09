#!/usr/bin/python3
"""A module containing class_to_json function."""


def class_to_json(obj):
    """
    Converts the attributes of an object to a dictionary.
    Args:
        obj: An instance of a class with serializable attributes.
    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    attributes = obj.__dict__
    serializable_attributes = {
        key: value
        for key, value in attributes.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serializable_attributes
