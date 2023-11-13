#!/usr/bin/python3
"""class inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherit class
    methods & attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize attr"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the way to prints"""
        return "[{}] ({}) {}/{} - {}".\
            format(
                type(self).__name__, self.id, self.x,
                self.y, self.height
                )

    @property
    def size(self):
        """get the value of size"""
        return self.width

    @size.setter
    def size(self, val):
        """ste the value of size"""
        self.width = val
        self.height = val

    def __fct_updt(self, id=0, size=0, x=0, y=0):
        """iteret attributes"""
        if id:
            self.id = id
        if size:
            self.size = size
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """update by args and kwargs"""
        if args:
            self.__fct_updt(*args)
        if kwargs:
            self.__fct_updt(**kwargs)

    def to_dictionary(self):
        """return dictionary by ordre"""
        return {"id": self.id, "size": self.width, "y": self.y, "x": self.x}
