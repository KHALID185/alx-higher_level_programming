#!/usr/bin/python3
"""define a peak algorithm"""


def find_peak(list_of_integers):
    """find a peak in a list of integer"""
    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        md = (lo + hi) // 2
        if list_of_integers[md] < list_of_integers[md + 1]:
            lo = md + 1
        else:
            hi = md

    return list_of_integers[lo]
