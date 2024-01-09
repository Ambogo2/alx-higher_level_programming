#!/usr/bin/python3
"""Contains a function that reads a file."""


def read_file(filename=""):
    """
    read_file:reads a file.
    Args:
        filename:The file to be read.
    """
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
