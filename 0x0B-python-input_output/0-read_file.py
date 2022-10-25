#!/usr/bin/python3
"""
    Module containing a function that reads a text file (UTF8)
    and prints it to stdout:
"""


def read_file(filename=""):
    """
        definition for read_file function

        Args:
        filename: the name of the file to read.
    """

    with open(filename, encoding="utf-8") as rf:
         print(rf.read(), end="")

    rf.close()
