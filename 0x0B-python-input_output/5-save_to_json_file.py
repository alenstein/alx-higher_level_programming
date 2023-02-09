#!/usr/bin/python3
""" Module containing definition for save_to_json function"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file in JSON format.

    Parameters:
    my_obj (object): The object to be written to the file.
    filename (str): The name of the file to write to.

    Returns:
    None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

