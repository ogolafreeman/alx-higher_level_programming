#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for z in range(len(matrix)):
        new_matrix[z] = list(map(lambda x: x**2, matrix[z]))

    return (new_matrix)
