#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    resultat = list(map(lambda i: list(map(lambda j: j**2, i)), matrix))
    return resultat
