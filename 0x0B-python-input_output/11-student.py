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

    def to_json(self, attrs=None):
        """return a dictionnary representention instances"""
        try:
            for items in attrs:
                if not isinstance(items, str):
                    return self.__dict__
        except Exception:
            return self.__dict__
        dct = dict()
        for ky, val in self.__dict__.items():
            if ky in attrs:
                dct[ky] = val
        return dct

    def reload_from_json(self, json):
        """replaces all attributes of the Student instances"""
        for ky, val in json.items():
            if ky in self.__dict__:
                self.__dict__[key] = val
