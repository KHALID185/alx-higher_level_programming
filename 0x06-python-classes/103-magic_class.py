#!/usr/bin/python3
"""define a class magic"""

import math


class MagicClass:
    """represente the class magic and all the fct"""

    def __init__(self, radius=0):
        """initialization of arguments"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the area of the magic calculateur"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """the circumference of the calcl"""
        return 2 * math.pi * self.__radius
