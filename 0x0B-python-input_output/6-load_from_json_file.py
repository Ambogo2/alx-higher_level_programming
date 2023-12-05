#!/usr/bin/python3
"""A module containing load_from_json_file function."""
import json


def load_from_json_file(filename):
    """
    load_from_json_file- creates an Object from a “JSON file"
    args:
        filename:filename
    """
    with open(filename, "r") as file:
        data = json.load(file)
        return data
