#!/usr/bin/python3
"""
    Module containing a function that writes an Object to a text file
    using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text file, using JSON representation

        Args:
        my_obj: object to be  written to a text file
        filename: name of file to write to
    """

    with open(filename, 'w', encoding="UTF-8") as jfile:
        json.dump(my_obj, my_file)

    jfile.close()
