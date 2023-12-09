#!/usr/bin/python3
"""This is a module for base class"""

import json
import csv
import turtle
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
        if list_dictionaries is None or list_dictionaries  == []:
             return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ 
        writes the JSON string representation of list_objs to a file
        args:
            list_obj:list objects
        """
        filename= Cls.__name__ +."json"
        with open(filename, 'w') as file:
            if list_objs is None:
                 file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))
            
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):



    @classmethod
    def load_from_file(cls):


    @classmethod
    def save_to_file_csv(cls, list_objs):


    @classmethod
    def load_from_file_csv(cls):


    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
