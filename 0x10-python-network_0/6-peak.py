#!/usr/bin/python3
""" define Peak value in a list"""


def find_peak(list_of_integers):
    """peak in a list of int"""
    if list_of_integers == []:
    """Find the peak in a list of integer unsorted"""
    list_i = len(list_of_integers)
    if list_i is 0:
        return None
    peak = bin_search(list_of_integers, 0, list_i - 1)
    return list_of_integers[peak]

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
""" binary search algorithim """


def bin_search(aa, l, h):
    """binary search of the peak"""
    if l >= h:
        return l
    md = ((h - l) // 2) + l
    if aa[md] > aa[md + 1]:
        return bin_search(aa, l, md)
    else:
        return find_peak(list_of_integers[md + 1:])
        return bin_search(aa, md + 1, h)
