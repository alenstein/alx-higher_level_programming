#!/usr/bin/python3
""" Module containing function for appending text to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
     returns the number of characters added.

    Parameters:
        filename (str): The name of the file to be written to.
        text (str): The string to be appended to the file.

    Return:
        int: The number of characters added.
    """
    try:
        with open(filename, 'a', encoding="UTF-8") as f:
            return f.write(text)
    except FileNotFoundError:
        with open(filename, 'w', encoding="UTF-8") as f:
            return f.write(text)
