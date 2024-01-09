#!/usr/bin/python3
"""A module containing  a script that adds all arguments to a Python list."""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def adds_all_arguments(arguments):
    """
    adds_arguments:adds arguments to a list.
    args:
        arguments:arguments to be added.
    """
    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_data = []
    existing_data.extend(arguments)
    save_to_json_file(existing_data, 'add_item.json')


if __name__ == "__main__":
    arguments = sys.argv[1:]

    if not arguments:
        print("Usage: python script.py arg1 arg2 arg3 ...")
        sys.exit(1)

    adds_all_arguments(arguments)
    print(f"Arguments added and saved to 'add_item.json'")
