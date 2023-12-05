#!/usr/bin/python3
"""A module containing to_json_string function."""
import json


def to_json_string(my_obj):
    """
    to_json_string- returns the JSON representation of an object
    args:
        my_obj:object
    """
    json_string = json.dumps(my_obj)
    return json_string
