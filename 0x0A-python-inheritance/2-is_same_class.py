#!/usr/bin/python3
"""fct verify if object is an instance of class inherited from"""


def is_same_class(obj, a_class):
    """
    function return true if object is in the class inherited from

    args: the object and specified class

    return: true or false
    """
    return isinstance(obj, a_class)
