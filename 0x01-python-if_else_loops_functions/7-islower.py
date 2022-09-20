#!/usr/bin/python3
def islower(c):
    for i in range(ord("a"), ord("z")):
        if i == ord(c):
            return True
    return False
