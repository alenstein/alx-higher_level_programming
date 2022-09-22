#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv)
    total = 0

    for i in range(1, args):
        total += int(argv[i])
    print(total)
