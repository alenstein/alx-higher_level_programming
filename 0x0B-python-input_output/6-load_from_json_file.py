#!/usr/bin/python3
"""
    Module containing a function that creates an Object from a "JSON file".
"""

import json


def load_from_json_file(filename):
    """
        creates an Object from a "JSON file"
    """

    with open(filename, 'r', encoding="UTF-8") as obj_file:
        return (json.load(obj_file))

    obj_file.close()
