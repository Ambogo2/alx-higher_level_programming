#!/usr/bin/python3
"""A module containing append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file.
    Args:
        - filename: file to be modified
        - search_string: string to search in each line
        - new_string: string to append after each line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as f:
        string = ""
        for line in lines:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
