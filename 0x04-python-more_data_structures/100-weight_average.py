#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        return (sum(x * y for x, y in my_list) / sum(b for x, y in my_list))
