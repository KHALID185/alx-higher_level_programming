#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = list(map(lambda items: replace if items == search else items, my_list))
    return res
