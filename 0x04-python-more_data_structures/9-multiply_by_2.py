#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_dict = {}
    for key in a_dictionary:
        updated_dict[key] = a_dictionary.get(key) * 2
    return updated_dict
