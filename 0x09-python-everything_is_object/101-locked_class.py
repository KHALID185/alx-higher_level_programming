#!/usr/bin/python3
"""a class dynamicaly creating"""


class LockedClass:
    """prevent from dynamically creating new instance except first_name"""
    __slots__ = ["first_name"]
