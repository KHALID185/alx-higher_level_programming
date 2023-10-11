#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_l = []
    for i in my_list:
        if i == search:
            i = replace
            n_l.append(i)
        elif i != search:
            n_l.append(i)
    return n_l
