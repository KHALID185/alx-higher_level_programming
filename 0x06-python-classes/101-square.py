#!/usr/bin/python3
"""class with instance prvt and public advance"""


class Square:
    """initialize private attribute"""

    def __init__(self, size=0, position=(0, 0)):

        """add size and position as arguments"""
        self.size = size
        self.position = position

    @property
    def size(self):

        """property to retrieve it (size)"""
        return (self.__size)

    @size.setter
    def size(self, value):

        """property setter size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):

        """property to retrieve it (position)"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(items, int) for items in value) or
                not all(items >= 0 for items in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """public instance"""
        return (self.__size * self.__size)

    def my_print(self):
        """objet to print the # and space"""
        if self.__size == 0:
            print("")
            return

        [print("") for items in range(0, self.__position[1])]
        for items_2 in range(0, self.__size):
            [print(" ", end="") for items_3 in range(0, self.__position[0])]
            [print("#", end="") for items_4 in range(0, self.__size)]
            print("")

    def __str__(self):
        """how to represnete the output"""
        if self.__size != 0:
            [print("") for items in range(0, self.__position[1])]
        for items_1 in range(0, self__size):
            [print(" ", end="") for items_2 in range(0, self.__position[0])]
            [print("#", end="") for items_3 in range(0, self.__size)]
            if items_1 != self.__size - 1:
                print("")
                return ("")
