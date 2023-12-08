#!/usr/bin/python3
"""This is a module for base class"""

import json

class Base:
    """defines class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization for class base
        """
        if id is not None:
            self.id = id
        else:
           base. __nb_objects += 1
           self.id = base. __nb_objects
