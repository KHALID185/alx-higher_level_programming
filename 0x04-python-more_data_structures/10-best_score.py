#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    vm= 0
    for val in a_dictionary.values():
        if val > vm:
            vm = val
    return vm
