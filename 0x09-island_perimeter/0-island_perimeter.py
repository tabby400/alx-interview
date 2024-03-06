#!/usr/bin/python3
"""
getting the perimeter of an island in 2grid
"""


def island_perimeter(grid):
    """
     calculates the perimeter of island described in grid
    """
    perimeter = 0
    # rotate 90 degree for both rows and colum to be iterated
    for row in grid + list(map(list, zip(*grid))):
        for currcel, nxtcel in zip([0] + row, row + [0]):
            perimeter += int(currcel != nxtcel)  # adds perimeter by 1
    return perimeter
