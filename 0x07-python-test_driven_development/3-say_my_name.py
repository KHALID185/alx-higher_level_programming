#!/usr/bin/python3
"""function the print myfirst and last name (module)"""


def say_my_name(first_name, last_name=""):
    """
    function that print my name

    args:
    first name
    last name

    raises:
    TypeError: first and last name must br a string

    Return: void

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
