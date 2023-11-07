#!/usr/bin/python3
"""fct that writes a string in a file and return len"""


def write_file(filename="", text=""):
    """write in a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        wr = file.write(text)
    print(wr, end="")
    return len(text)
