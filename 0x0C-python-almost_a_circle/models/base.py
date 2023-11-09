#!/usr/bin/python3
"""a classe base"""


class Base:
    """insert attributes and methodes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize
        args: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
