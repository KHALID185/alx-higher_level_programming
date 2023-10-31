#!/usr/bin/python3
"""a rectancgle class with some method"""


class Rectangle:
    """rectangle class not empty"""

    number_of_instances = 0
    """number of active inst"""

    print_symbol = "#"
    """can be any type"""

    def __init__(self, width=0, height=0):
        """initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.height * self.width

    def perimeter(self):
        """the perimeter of the rectanggle"""
        if self.__width != 0 and self.__height != 0:
            return (self.height * 2) + (self.width * 2)
        return 0

    def __str__(self):
        """return printable rectangle with #"""
        if self.__width == 0 and self.__height == 0:
            return ""
        return (
                (str(self.print_symbol) * self.width + "\n")
                * self.height
                )[:-1]

    def __repr__(self):
        """Developer-Friendly Representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a text for evry delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
