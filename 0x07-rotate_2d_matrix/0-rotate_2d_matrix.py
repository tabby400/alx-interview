#!/usr/bin/python3
"""
Rotating a 2d matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Function rotates elements of matrix 90 degrees to right
    """
    n = len(matrix)  # finding size of the matrix
    for border in range(n // 2):  # outer layers rotating means inner as well
        first, last, adjustment = border, n - 1 - border, 0
        for x in range(first, last):
            orig = matrix[first][x]
            matrix[first][x] = matrix[last - adjustment][first]
            matrix[last - adjustment][first] = matrix[last][last - adjustment]
            matrix[last][last - adjustment] = matrix[x][last]
            matrix[x][last] = orig
            adjustment = adjustment + 1
