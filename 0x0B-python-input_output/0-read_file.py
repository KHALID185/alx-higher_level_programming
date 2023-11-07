#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """read filename"""
    with open(filename, encode='utf-8') as file:
        rd = file.read()
    print(rd, end="")
