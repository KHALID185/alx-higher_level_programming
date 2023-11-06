#!/usr/bin/python3
"""fct verify if object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    function return true if object is in the class

    args: the object and specified class

    return: true or false
    """
    return type(obj) == a_class
