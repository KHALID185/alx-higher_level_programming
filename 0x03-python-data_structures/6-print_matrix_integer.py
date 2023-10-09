#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for items in matrix:
        if len(items) == 0:
            print()
        for el in range(len(items)):
            if el is len(items) - 1:
                print("{:d}".format(items[el]), end="\n")
            else:
                print("{:d}".format(items[el]), end=" ")
