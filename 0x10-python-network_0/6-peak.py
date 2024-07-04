#!/usr/bin/python3
""" define Peak value in a list"""


def find_peak(list_of_integers):
    """Find the peak in a list of integer unsorted"""
    list_i = len(list_of_integers)
    if list_i is 0:
        return None
    peak = bin_search(list_of_integers, 0, list_i - 1)
    return list_of_integers[peak]


""" binary search algorithim """


def bin_search(aa, l, h):
    """binary search of the peak"""
    if l >= h:
        return l
    md = ((h - l) // 2) + l
    if aa[md] > aa[md + 1]:
        return bin_search(aa, l, md)
    else:
        return bin_search(aa, md + 1, h)
