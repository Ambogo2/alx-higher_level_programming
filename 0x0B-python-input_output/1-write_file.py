#!/usr/bin/python3
"""A module containing write_file function."""


def write_file(filename="", text=""):
    """
    write_file - writes to a file
    args:
        filename:file to be written
        text:text to be written
    """
    with open(filename, "w", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
