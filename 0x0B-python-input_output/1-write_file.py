#!/usr/bin/python3
"""
    Module containing function  that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
        definition for write_file function.

        Args:
        filename: name of the file to write to.
        text: the content to be written to the file.
    """        
    with open(filename, encoding="UTF-8") as wf:
        return(wf.write(text))

    wf.close()    
