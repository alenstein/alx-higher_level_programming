#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    numberOfArgs = len(argv) - 1

    if numberOfArgs == 0:
        print("{} arguments.".format(numberOfArgs))
    elif numberOfArgs == 1:
        print("{} argument:".format(numberOfArgs))
    else:
        print("{} arguments:".format(numberOfArgs))

    for i in range(1, numberOfArgs + 1):
        print("{}: {}".format(i, argv[i]))
