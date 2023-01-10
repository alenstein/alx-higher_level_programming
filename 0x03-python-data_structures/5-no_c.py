#!/usr/bin/python3

def no_c(my_string):
    new_string = ""

    for index in range(len(my_string)):
        item = my_string[index]

        if item == 'c' or item == 'C':
            pass
        else:
            new_string += item
    return new_string
