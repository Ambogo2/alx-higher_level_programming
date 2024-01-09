#!/usr/bin/python3
"""Contains a function that writes to a file."""


def write_file(filename="", text=""):
    """
    write_file:reads a file.
    Args:
        filename:The file to be written.
        text:text to be written
    """
    with open(filename, "w", encoding='utf-8') as file:
        chars_count = file.write(text) 
        return chars_count
