#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    vm= 0
    for val in a_dictionary.values():
        if val > vm:
            vm = val
    return (list(a_dictionary.keys())[list(a_dictionary.values()).index(vm)])
