#!/usr/bin/python3
""" Module containing definition for append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string

    Parameters:
        filename (str): name for the file to be processed.
        search_string (str): specific string to be searched for.
        new_string (str): line of text to be inserted.

    Return:
        void.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
