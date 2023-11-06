#!/usr/bin/python3
"""fct object is an instance of class inherited from"""


def inherits_from((obj, a_class):
    """
    function return true if object is in the class inherited from

    args: the object and lass

    return: true or false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
