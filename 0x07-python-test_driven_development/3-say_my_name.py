#!/usr/bin/python3
"""
This module contains a function that prints name.
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints name
    Args:
        first_name: first name
        last_name: last name
    Returns:
        Name.
    Raises:
        TypeError if first name and last name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
