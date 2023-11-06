#!/usr/bin/python3
"""Module class"""


class BaseGeometry:
    """basegeometry class
    method area()
    method integer_validator(self, name, value)
    """
    def area(self):
        """method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method two integer validiton
        args: name should be string"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
