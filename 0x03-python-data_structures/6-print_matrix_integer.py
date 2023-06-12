#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        l = 1
        for y in x:
            if l == len(x):
                print("{:d}".format(y), end="")
            else:
                print("{:d}".format(y), end=" ")
            l = l + 1
        print()
