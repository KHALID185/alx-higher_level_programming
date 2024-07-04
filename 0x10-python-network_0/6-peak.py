#!/usr/bin/python3
"""dunction to Defines a peak"""


def find_peak(list_of_integers):
    """peak in a list of int"""
    if list_of_integers == []:
        return None

    sz = len(list_of_integers)
    if sz == 1:
        return list_of_integers[0]
    elif sz == 2:
        return max(list_of_integers)

    md = int(sz / 2)
    peak = list_of_integers[md]
    if peak > list_of_integers[md - 1] and peak > list_of_integers[md + 1]:
        return peak
    elif peak < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
    else:
        return find_peak(list_of_integers[md + 1:])
