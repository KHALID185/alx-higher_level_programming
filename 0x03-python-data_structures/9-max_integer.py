#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        lst = my_list.copy()
        lst.sort()
        return (lst[len(lst) - 1])
