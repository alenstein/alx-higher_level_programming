#!/usr/bin/python3
""" Module containing definition for write_file function"""


def write_file(filename="", text=""):
    """
       Writes a string to a text file (UTF8) and returns the number of
       characters written. The function creates the file if it doesn't exist
       and overwrites the content of the file if it already exists.

       Parameters:
       filename (str): The name of the file to write to.
       text (str): The text to write to the file.

       Returns:
       int: The number of characters written to the file.
       """
    char_count = 0
    with open(filename, "w", encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
