#!/usr/bin/python3
"""Define a function to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return list_of_integers[bin_search(list_of_integers, 0, len(list_of_integers) - 1)]


def bin_search(arr, low, high):
    """Binary search algorithm to find a peak."""
    if low == high:
        return low
    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
        return bin_search(arr, low, mid)
    return bin_search(arr, mid + 1, high)
