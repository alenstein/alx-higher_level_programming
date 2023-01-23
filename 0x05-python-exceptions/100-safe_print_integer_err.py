#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("Exception: ", TypeError)
        return False
    except ValueError:
        print("Exception: ", ValueError)
        return False
