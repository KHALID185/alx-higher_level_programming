#!/usr/bin/python3
"""class that inherits from"""


class Rectangle(BaseGeometry):
    """initialize the subclass"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
