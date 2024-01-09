#!/usr/bin/python3
"""A module containing Student class."""


class Student():
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        Args:
            first_name:first name
            last_name:last name
            age:age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return d

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        Args:
            json (dict): A dictionary with attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
