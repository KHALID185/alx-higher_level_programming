#!/usr/bin/python3
"""fct  that return the dictionary description with data strct"""


def class_to_json(obj):
    """return data structure as dict"""
    return obj.__dict__
