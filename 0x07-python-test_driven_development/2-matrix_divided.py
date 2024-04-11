#!/usr/bin/python3
"""module for matrix_divided method"""


def matrix_divided(matrix, div):
    """fun to divide the elements inside the matrix

    Args:
        matrix (list of lists): elements where will be divided by div
        div (int): the divisor
    Return:
        matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not any(matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(
        isinstance(row, list) and all(
            isinstance(x, (int, float)) for x in row
                ) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
