#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for j in row:
            print("{:d}".format(j), end=" ")
        print()
