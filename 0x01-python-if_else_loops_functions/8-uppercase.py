#!/usr/bin/python3
def uppercase(str):
    for i in str:
        _ord = ord(i)
        if _ord > 96:
            _ord = 65 +(_ord - 97)
        print("{}".format(chr(_ord)), end="")
    print()          
