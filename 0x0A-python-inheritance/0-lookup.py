#!/usr/bin/python3
"""
A module for lookup function
"""


def lookup(obj):
    """
    lookup: returns list of available attributes and methods of an object
    arg:
        obj: list of objects
    Returns: a list of objects
    """
    return dir(obj)
