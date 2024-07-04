#!/usr/bin/python3
"""Define a function to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)

def find_peak_util(nums, low, high):
    """Binary search algorithm to find a peak."""
    mid = (low + high) // 2
    # If the mid element is greater than or equal to its neighbors, then it's a peak
    if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
        return nums[mid]
    # If the left neighbor is greater, then there must be a peak on the left half
    elif mid > 0 and nums[mid - 1] > nums[mid]:
        return find_peak_util(nums, low, mid - 1)
    # If the right neighbor is greater, then there must be a peak on the right half
    else:
        return find_peak_util(nums, mid + 1, high)
