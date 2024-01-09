#!/usr/bin/python3
"""Contains a function that appends to a file."""


def append_write(filename="", text=""):
    """
    append_write:appends a string to end of file.
    Args:
        filename:file to append
        text:text to be appended
    """
    with open(filename, "a", encoding='utf-8')as file:
        append = file.write(text)
        return append
