#!/usr/bin/python3

for i in range(90, 64, -2):
    print("{1}{0}".format(chr(i-1), chr(i+32)), end="")
