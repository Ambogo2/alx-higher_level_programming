#!/usr/bin/python3
""" Define a Class BaseGeometry """


class BaseGeometry:
    """ A class that defines BaseGeometry."""
    def area(self):
        """area: area of Geometry."""
        raise Exception ("area() is not implemented")
    def integer_validator(self, name, value):
        """
            integer_validator:validates if value is an integer.
            args:
                name:name
                value:value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
