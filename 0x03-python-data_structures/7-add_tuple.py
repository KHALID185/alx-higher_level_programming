#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) > 0):
        a_0 = tuple_a[0]
    else:
        a_0 = 0
    if (len(tuple_b) > 0):
        b_0 = tuple_b[0]
    else:
        b_0 = 0
    if (len(tuple_a) > 1):
        a_1 = tuple_a[1]
    else:
        a_1 = 0
    if (len(tuple_b) > 1):
        b_1 = tuple_b[1]
    else:
        b_1 = 0
    a = a_0 + b_0
    b = a_1 + b_1
    return(a, b)
