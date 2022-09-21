#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(b):
            result *= a
    elif b == 0:
        result = 1
    else:
        for i in range(-(b)):
            result = float(result * a)
        result = float(1 / result)
        return result
