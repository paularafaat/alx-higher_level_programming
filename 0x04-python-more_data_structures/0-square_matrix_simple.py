#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cp = matrix.copy()
    for i in range(len(cp)):
        for j in range(len(cp[i])):
            cp[i][j] = cp[i][j] * cp[i][j]
    return cp
