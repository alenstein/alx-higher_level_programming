#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *

    list = dir()
    for a in range(0, len(list)):
        if list[a][0:2] != "__":
            print("{}".format(list[a]))
