#!/usr/bin/python3
"""A module containing read_file function."""


def read_file(filename=""):
    """
    read_file - reads a file
    filename:file to be read
    """
    with open("my_file_0.txt", "r") as file:
        content = file.read()
        print(content)
