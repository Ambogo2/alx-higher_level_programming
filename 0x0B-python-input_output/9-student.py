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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        Returns:
               A dictionary containing the attributes.
        """
    student_dict = {
        'first_name':self.first_name,
        'last_name':self.last_name,
        'age':self.age

    }
    return student_dict
