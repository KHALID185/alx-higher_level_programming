#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for num in range(4, 6):
            res = add(c, num)
        return res
    else:
        num_2 = sub(a, b)
        return num_2
    return 0

