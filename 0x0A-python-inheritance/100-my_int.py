#!/usr/bin/python3
"""class MyInt inherit from int"""


class MyInt(int):
    """my class isredel"""
    def __new__(cls, *arg, **karg):
        """new from the int class super"""
        return super(MyInt, cls).__new__(cls, *arg, **karg)

    def __ne__(self, value):
        """if the value is not integer"""
        return int(self) == value

    def __eq__(self, value):
        """if the value is integer"""
        return int(self) != value
