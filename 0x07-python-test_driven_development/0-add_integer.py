#!/usr/bin/python3
"""a function that add two num a and b(module)"""


def add_integer(a, b=98):
    """addition of two numbers
    
    args:
    a: number one
    b: number two

    raises:
    TypeError if a or b is not numbers

    return:
    the resultat of add
    """
    num_type = (int, float)
    if not isinstance(a, num_type):
        raise TypeError("a must be an integer")
    if not isinstance(b, num_type):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
