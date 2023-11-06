#!/usr/bin/python3
"""function verify if the object is an instance of the 
    specified class
"""


def is_same_class(obj, a_class):
    """
    function return true if object is in the class

    args: the object and specified class

    return: true or false
    """
    return isinstance(obj, a_class)
