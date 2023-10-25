#!/usr/bin/python3
"""class with instance prvt, public and raise the error"""


class Square:
    """initialize private attribute"""

    def __init__(self, size=0):

        """add size as argument
            and raise the errors"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """public instance"""
        return self.__size ** 2
