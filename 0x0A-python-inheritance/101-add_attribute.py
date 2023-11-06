#!/usr/bin/python3
"""fct that add new attribute"""


def add_attribute(obj, att, value):
    """add attributes
    args: object and attributs and the value

    raise: type error

    """
    if hasattr(obj, "__dict__") != 0:
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
