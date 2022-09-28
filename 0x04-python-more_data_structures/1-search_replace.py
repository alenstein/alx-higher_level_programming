#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updated_list = []

    for item in my_list:
        if item == search:
            item = replace
        updated_list.append(item)
    return updated_list
