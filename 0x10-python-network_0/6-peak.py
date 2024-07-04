#!/usr/bin/python3
"""define a peak algorithm"""


def find_peak(list_of_integers):
    """find a peak in a list of integers"""
    if list_of_integers:
        pk = 0
        xl = len(list_of_integers) - 1
        while pk < x:
            m = (p+x) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                xl = m
            else:
                pk = m + 1
        return list_of_integers[pk]
