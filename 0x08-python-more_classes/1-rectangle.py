#!/usr/bin/python3
"""a rectancgle class with some method"""


class Rectangle:
    """rectangle class not empty"""

    def __init__(self, width=0, height=0):
        """initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the private instance of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the instance height and raises"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
