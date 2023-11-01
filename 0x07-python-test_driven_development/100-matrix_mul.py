#!/usr/bin/python3
"""Module for multiple 2 matrix"""


def matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
        Args:
        matrice a and matrice b
        raises:
        TypeError and ValueError
        Return: a * b
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    a_vide = False
    b_vide = False
    a_norect = False
    b_norect = False
    a_nonumb = False
    b_nonumb = False
    for line in m_a:
        if not isinstance(line, list):
            raise TypeError("m_a must be a list of lists")
        if len(line) != len(m_a[0]):
            a_norect = True
        for items in line:
            if not isinstance(items, (int, float)):
                a_nonumb = True

    for line in m_b:
        if not type(line) is list:
            raise TypeError("m_b must be a list of lists")
        if len(line) != len(m_b[0]):
            b_norect = True
        for items in line:
            if not isinstance(items, (int, float)):
                b_nonumb = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if a_nonumb:
        raise TypeError("m_a should contain only integers or floats")

    if b_nonumb:
        raise TypeError("m_b should contain only integers or floats")

    if a_norect:
        raise TypeError("each row of m_a must should be of the same size")

    if b_norect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    resultat = [[] for i in range(len(m_a))]

    for ln in range(len(m_a)):
        for cl in range(len(m_b[0])):
            c = 0
            for itm in range(len(m_b)):
                c += m_a[ln][itm] * m_b[itm][cl]
            resultat[ln].append(c)

    return resultat

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
