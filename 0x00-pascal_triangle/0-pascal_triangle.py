#!/usr/bin/python3
"""
generates a list representing pascal's triangle based on an input integer depth
"""


def pascal_triangle(n):
    """
    generate pascal's triangle depth 'n'
    """
    i = 0
    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle
    while i < n - 1:
        triangle.append([1] + [triangle[-1][j] + triangle[-1][j + 1] for j in range(i)] + [1])
        i += 1
    return triangle
