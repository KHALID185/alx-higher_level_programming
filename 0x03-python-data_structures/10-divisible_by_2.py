#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    lst = []
    for items in my_list:
        if (items % 2) == 0:
            lst.append(True)
        else:
            lst.append(False)
    return lst
