#!/usr/bin/python3
"""nxn matrix clockwise rotation"""


def rotate_2d_matrix(matrix):
    """rotates a matrix 90deg clockwise"""
    dimension = len(matrix)
    """row_i = 0
    row_n = len(matrix) - 1  # where row_n is dimension - i
    # to rotate the matrix 90 deg anticlockwise
    for num in range(dimension // 2):
        col = 0
        while col < len(matrix):
            temp_entry = matrix[row_i][col]
            matrix[row_i][col] = matrix[row_n][col]
            matrix[row_n][col] = temp_entry
            col += 1"""
    matrix.reverse()

    # to rotate again the matrix 180 deg ie 270 anticlock = 90 clockwise
    i = 0
    k = 1
    while i < (dimension):
        j = k
        while j < (dimension):
            temp_entry = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp_entry
            j += 1
        i += 1
        k += 1
