#!/usr/bin/python3
"""class student"""


class Student:
    """class with 3 attributes public
    first_name, last name, age
    """
    def __init__(self, first_name, last_name, age):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionnary representention"""
        return self.__dict__
