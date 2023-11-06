#!/usr/bin/python3
"""class inherits from list"""


class MyList(list):
    """inherit class MyList"""
    def print_sorted(self):
        """method that print the sorted list"""
        print(sorted(self))
