#!/usr/bin/python3
"""
    Module that creates a class that inherits from the list class
"""


class MyList(list):
    """
        Class MyList inherits from list class
    """

    def print_sorted(self):
        """
            prints the list in ascending sort
        """

        my_list = self[:]
        my_list.sort()
        print("{}".format(my_list))
