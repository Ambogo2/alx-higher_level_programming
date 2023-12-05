#!/usr/bin/python3
"""A module containing a class Student"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list): A list of strings specifying attributes to include.
        returns:
            dict: A dictionary containing the specified attributes and their values.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values from a dictionary.
        Args:
            json (dict): A dictionary with attribute names as keys and corresponding values.
        """
        for key, value in json.items():
            setattr(self, key, value)
