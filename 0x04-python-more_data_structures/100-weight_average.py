#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        for x,y in my_list:
            s1 += x * y
            s2 += y
        s = s1 / s2
        return s
