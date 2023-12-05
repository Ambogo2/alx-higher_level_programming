#!/usr/bin/python3
"""A module containing from_json_string function."""
import json


def from_json_string(my_str):
    """
    from_json_string- returns an object represented by a JSON string
    args:
        my_str:string
    """
    data = json.loads(my_str)
    return data
