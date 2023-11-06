#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"intialize a subclass of derived class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
