#!/usr/bin/python3
"""script read line by line in stdin"""


from sys import stdin


code_status = {
            '200': 0, '301': 0, '400': 0,
            '401': 0, '403': 0, '404': 0,
            '405': 0, '500': 0
        }
size = j = 0


def fct_print():
    """prints statistics since the beginning"""
    print(f"File size: {size}")
    for ky, val in sorted(code_status.items()):
        if val > 0:
            print("{:s}: {:d}".format(ky, val))


try:
    for ln in stdin:
        spline = ln.split()
        if len(spline) >= 2:
            stts = spline[-2]
            size += int(spline[-1])
            if stts in code_status:
                code_status[stts] += 1
        j += 1

        if j % 10 == 0:
            fct_print()
    fct_print()

except KeyboardInterrupt as e:
    fct_print()
