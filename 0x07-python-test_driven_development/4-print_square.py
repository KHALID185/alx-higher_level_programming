#!/usr/bin/python3
"""module of printing # square"""


def print_square(size):
    """
    a function that prints a square with the character #

    args:
    size - length of the square

    raises:
    TypeError: if size is not integer
            or if it is a float and less than zero

    return:
    void
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for line in range(size):
        for col in range(size):
            print("#", end="")
        if line != size - 1:
            print()
    print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
