#!/usr/bin/python3
"""fct returns list of list"""


def pascal_triangle(n):
    """representition pascal triangle"""
    if n <= 0:
        return []

    trgl = [[1]]
    while len(trgl) != n:
        ls = trgl[-1]
        garage = [1]
        for items in range(len(ls) - 1):
            garage.append(ls[items] + ls[items + 1])
        garage.append(1)
        trgl.append(garage)
    return trgl
