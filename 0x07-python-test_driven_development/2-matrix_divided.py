#!/usr/bin/python3
"""function that divide all elements of the matrix"""


def matrix_divided(matrix, div):
    """
    divide all element by div

    args:
    matrix
    diviser

    raises:
    TypeError: is matrix is not a list of list of int or float
                or each row aren't the same size 
                or div is not a number
    ZeroDivisionError: if div=0

    return:
    the new matrix divided
    """
    num_type = (int, float)
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not isinstance(div, num_type):
        raise TypeError("div must be a number")
    for line in matrix:
        if not isinstance(line, list) or len(line) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        for items in line:
            if not isinstance(items, num_type):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
        if len (line) != len (matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(items / div, 2) for items in line] for line in matrix]
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
