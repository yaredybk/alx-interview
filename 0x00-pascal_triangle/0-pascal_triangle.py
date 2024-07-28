#!/usr/bin/python3
"""Pascal's triangle.

Generates a list representing pascal's triangle.
based on an input integer as depth.
"""


def pascal_triangle(n):
    """Generate pascal's triangle depth 'n'."""
    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle
    for i in range(n - 1):
        triangle.append([1] + [triangle[-1][j] + triangle[-1][j + 1]
                               for j in range(i)] + [1])
    return triangle
