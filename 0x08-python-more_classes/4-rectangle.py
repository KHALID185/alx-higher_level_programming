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
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """the perimeter of the rectanggle"""
        if self.__width != 0 and self.__height != 0:
            return (self.__height * 2) + (self.__width * 2)
        return 0

    def __str__(self):
        """return printable rectangle with #"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            s += "\n".join(
                "#" * self.__width for line in range(0, self.__height))
        return s
    def __repr__(self):
        """Developer-Friendly Representation"""
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)
