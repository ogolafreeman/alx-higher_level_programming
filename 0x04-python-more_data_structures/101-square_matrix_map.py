#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda z: list(map(lambda d: d**2, z)), matrix)))
