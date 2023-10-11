#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = list(map(lambda num: list(map(lambda items: items**2, num)), matrix))
    return res
