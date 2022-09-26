#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for index in range(len(my_list)):
            if index == idx:
                my_list[index] = element
                return my_list
