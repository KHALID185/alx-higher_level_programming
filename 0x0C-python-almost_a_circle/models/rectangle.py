#!/usr/bin/python3
"""rectangles inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """methodes and attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, val):
        """set a width"""
        self.validate_attr("width", val, True)
        self.__width = val

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, val):
        """set a height"""
        self.validate_attr("height", val, True)
        self.__height = val

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, val):
        """set a x"""
        self.validate_attr("x", val)
        self.__x = val

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, val):
        """set a y"""
        self.validate_attr("y", val)
        self.__y = val

    def validate_attr(self, name, val, bol=False):
        """raises attributes"""
        if not type(val) is int:
            raise TypeError("{} must be an integer".format(name))
        if val <= 0 and bol:
            raise ValueError("{} must be > 0".format(name))
        elif val < 0 and not bol:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """public method area """
        return (self.width * self.height)

    def display(self):
        """prints in stdout rectangle with#"""
        print(
            "\n" * self.y +
            (" " * self.x + "#" * self.width + "\n") * self.height, end=""
            )

    def __str__(self):
        """return the way to prints"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(
                    type(self).__name__, self.id, self.x,
                    self.y, self.width, self.height
                    )
