#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix inplace

    requirements:
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty."""
    l = len(matrix)
    r = range(matrix)
    def swap(i, j):
        """swap elements of a matrix inplace"""
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    [[swap(i, j) for i in range(j + 1, l)] for j in range(l - 1)]
