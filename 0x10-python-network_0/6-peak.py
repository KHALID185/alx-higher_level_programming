#!/usr/bin/python3
"""Define a function to find a peak in a list."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return bin_search(list_of_integers, 0, len(list_of_integers) - 1)

def bin_search(arr, low, high):
    """Binary search algorithm to find a peak"""
    if low == high:
        return arr[low]
    mid = (low + high) // 2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return bin_search(arr, low, mid - 1)
    else:
        return bin_search(arr, mid + 1, high)
