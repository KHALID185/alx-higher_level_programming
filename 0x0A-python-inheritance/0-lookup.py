#!/usr/bin/python3
"""function lookup"""


def lookup(obj):
    """
    look for all attributes and methodes of an object
    
    args: object to look up in it

    return: list of attributes and methodes
    """

    return dir(obj)
