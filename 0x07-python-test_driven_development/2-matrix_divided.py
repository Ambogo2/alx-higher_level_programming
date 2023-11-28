#!/usr/bin/python3
"""
This module is made up of a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function that divides the elements of a matrix
    Args:
        matrix: A matrix with elements to be divided
        div:The divisor
    Returns:
        A new matrix.
    Raises:
        TypeError:
            if the matrix is not a list of floats or integers
            if the rows of the matrix are not the same size
            if the divisor is not an integer or a float
        ZeroDivisionError if the divisor is 0
    """
    result_matrix = []
    error = "matrix must be a matrix(list of lists) of integers/floats"

    if not matrix or matrix == [[]] or matrix is None:
        raise TypeError(error)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error)
    for i in range(len(matrix)):
        row_result = []
        for j in range(len(matrix[0])):
            result = matrix[i][j]/div
            row_result.append(round(result, 2))
        result_matrix.append(row_result)
    return result_matrix
