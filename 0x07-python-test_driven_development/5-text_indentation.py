#!/usr/bin/python3
""" definition for text_indentation function"""


def text_indentation(text):
    """
    prints a text string `text` with 2 new lines
    after each of these characters: ., ? and :

    parameters:
        text: string, input text to the function.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    indent = False
    for char in text:
        if char in ".?:":
            print(char, end="\n\n")
            indent = True
        else:
            if indent:
                print("", end="")
                indent = False
            print(char, end="")
