#!/usr/bin/python3
"""
This module contains function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    Args:
        text: text to be printed
    Returns:
        a text with 2 new lines
    Raises:
        TypeError if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    characters = [',', ':', '?']
    current_line = ""

    for chars in text:
        current_line += chars
        if chars in characters:
            print(current_line.strip(), end="\n\n")
            current_line = ""
    print(current_line.strip(), end="")
