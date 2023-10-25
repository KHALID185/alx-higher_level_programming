#!/usr/bin/python3
"""class with instance prvt 5-square"""


class Square:
    """initialize private attribute"""

    def __init__(self, size=0):

        """add size as argument"""
        self.__size = size

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

    def my_print(self):
        """objet to print the square"""
        for items in range(0, self.size):
            for items_2 in range(0, self.size):
                if items_2 is not self.size - 1 or items == items_2:
                    print("#", end="")
                else:
                    print("#", end="\n")
        print()
