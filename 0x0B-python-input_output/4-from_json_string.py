#!/usr/bin/python3
"""
    Module containing a function that returns an object (Python data structure)
    represented by a JSON string:
"""

import json


def from_json_string(my_str):
    """
        definition for from_json_string function.

        Args:
        my_str: string object to be serialised to json format.
    """

    return (json.loads(my_str))
