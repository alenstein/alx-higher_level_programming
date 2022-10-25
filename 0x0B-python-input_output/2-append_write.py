#!/usr/bin/python3
"""
    Module  containing a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
        definition for append_write function.
        returns number of characters added.

        Args:
        filename: name of the file to be appended to.
        text: the string to be appended to the file.
    """

    with opens(filename, 'a', encoding='UTF-8') as af:
        return(af.write(text))
