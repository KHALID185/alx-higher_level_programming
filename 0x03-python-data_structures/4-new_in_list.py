#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = [None] * len(my_list)
    dx = 0
    lgt = len(my_list) - 1
    if idx < 0 or idx > lgt:
        return my_list
    while dx <= lgt:
        if dx == idx:
            cpy[dx] = element
        else:
            cpy[dx] = my_list[dx]
        dx += 1
    return cpy
