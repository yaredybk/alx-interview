#!/usr/bin/python3
"""
calculate the perimeter of a single island in a grid,
where the grid is represented by a 2D array of integers.
"""


def island_perimeter(grid):
    """the perimeter of the island described in grid"""
    prev = set()
    net = 0

    for row in grid:
        cur = set()
        left = False
        for ind, ele in enumerate(row):
            if ele:
                cur.add(ind)
                if ind in prev:
                    if not left:
                        net += 2
                else:
                    if left:
                        net += 2
                    else:
                        net += 4
                left = True
            else:
                left = False
        prev = cur

    return net
