#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    new_tuple = ()

    if lenght == 0:
        new_tuple = 0, None
    else:
        new_tuple = lenght, sentence[0]
    return new_tuple
