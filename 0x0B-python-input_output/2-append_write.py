#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Parameters:
        filename (str): The name of the file to be written to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf8") as f:
        char_count = 0
        char_count = f.write(text)
        return char_count
