#!/usr/bin/python3
"""class with instance prvt, public and raise the error"""


class Square:
    """initialize private attribute"""

    def __init__(self, size=0):

        """add size as argument"""
        self.size = size

    @property
    def size(self):

        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):

        """property setter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):

        """public instance"""
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
