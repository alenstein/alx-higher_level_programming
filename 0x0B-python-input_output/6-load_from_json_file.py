#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """This function takes a filename as an argument and creates an object from the JSON file.

    Parameters:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
