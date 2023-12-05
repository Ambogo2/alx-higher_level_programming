#!/usr/bin/python3
"""A module containing append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after - inserts a line of text to a file.
    args:
        filename: file to be modified
        search_string: string to search in each line
        new_string: string to append after each line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
