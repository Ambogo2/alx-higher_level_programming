#!/usr/bin/python3
"""A module containing save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file- writes an Object to a text file, using a JSON representation 
    args:
        my_obj:object
        filename:filename
    """
    with open (filename, "w") as file:
        json.dump(my_obj, file)
