#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            print("IndexError: list index out of range")
    print()
    return index
