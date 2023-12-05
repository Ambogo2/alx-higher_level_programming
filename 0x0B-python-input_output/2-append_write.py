#!/usr/bin/python3
"""A module containing append_write function."""


def append_write(filename="", text=""):
    """
    append_write - appends to a file
    args:
        filename:file to be appended
        text:text to be appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        append = file.write(text)
    return append
