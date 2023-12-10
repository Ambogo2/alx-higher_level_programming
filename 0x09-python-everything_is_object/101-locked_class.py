#!/usr/bin/python3
"""
Module for a class that prevents dynamic attributes creation
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass

    def __setattr__(self, name, value):
        """Override __setattr__ to raise AttributeError"""
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
