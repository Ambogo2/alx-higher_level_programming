#!/usr/bin/python3
"""A module containing from_json_string function."""
import json


def from_json_string(my_str):
    """
    from_json_string:object represented by a JSON string
    Args:
        my_str:str
    """
    data = json.loads(my_str)
    return data
