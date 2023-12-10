#!/usr/bin/python3
"""This is a module for base class"""
import json
import csv
import sys


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        args:
            list dictionaries:dictionary lists
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a list of objects to a JSON file
        Args:
            list_obj:list objects to be saved
        """
        filename = Cls.__name__ + ."json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        method that desirializes JSON string to a pyhon object

        Args:
        json_string: A JSON-formatted string to be deserialized.

        Returns:
             A Python list or dictionary repr deserialized JSON data.

       """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        method that creates an instance attributes already set
        args:
            dictionary:A dictionary with keys corresponding to class attributes
        Returns:
              An instance of the class with all attributes set
        """
        if dictionary and dictionary ! = {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            else:
                dummy_instance = cls(1)
                dummy_instance.update(**dictionary)
                return dummy_instance

    @classmethod
    def load_from_file(cls):
        """loads a list of objects from a JSON file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves a list of objects to a CSV file
        Args:
            list_objs:A list of object instances
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        csv_writer.writerow(fieldnames)

        for obj in list_objs:
            csv_writer.writerow([getattr(obj, attr) for attr in fieldnames])

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)]
                                   for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []
