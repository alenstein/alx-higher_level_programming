#!/usr/bin/python3

def element_at(my_list, idx):
    if not idx:
        return None
    elif idx > len(my_list):
        return None
    else:
        for index in range(len(my_list)):
            if index == idx:
                return my_list[index]
