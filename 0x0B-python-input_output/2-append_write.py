#!/usr/bin/python3
"""fct that appends a string in a file and return len added"""


def append_write(filename="", text=""):
    """appends in a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        ap = file.write(text)
    return len(text)
