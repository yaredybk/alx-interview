#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix inplace

    requirements:
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty."""
    l = len(matrix)
    r = range(l / 2)
    # to prevent swapping middle row twice in odd matrixs
    r2 = range((l + 1) / 2)
    # to prevent IndexError: list index out of range
    l -= 1
    def swap(i, j):
        """rotate 4 elements of a matrix inplace"""
        ii, jj = l - i, l - j
        matrix[i][j], matrix[j][ii], matrix[ii][jj], matrix[jj][i] = 
        matrix[jj][i], matrix[i][j], matrix[j][ii], matrix[ii][jj]

    [[swap(i, j) for i in r] for j in r]
