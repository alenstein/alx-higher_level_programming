#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    numberOfArgs = len(argv) - 1
    if numberOfArgs == 0:
        print("{:s} arguments.".format(numberOfArgs))
    elif numberOfArgs == 1:
        print("{:s} argument:".format(numberOfArgs))
    else:
        print("{:s} arguments:".format(numberOfArgs))

    for i in range(1, numberOfArgs + 1):
        print("{:s}: {:s}".format(i, argv[i]))
