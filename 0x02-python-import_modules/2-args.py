#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    numberOfArgs = len(argv) - 1
    if numberOfArgs == 0:
        print("{:d} arguments.".format(numberOfArgs))
    elif numberOfArgs == 1:
        print("{:d} argument:".format(numberOfArgs))
    else:
        print("{:d} arguments:".format(numberOfArgs))

    for i in range(1, numberOfArgs + 1):
        print("{:d}: {}".format(i, argv[i]))
