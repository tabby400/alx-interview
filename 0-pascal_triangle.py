#!/usr/bin/python3
"""
This is pascal's triangle where each number is the sum of
two numbers above it and it starts with 1
"""

def pascal_triangle(n):
    """
         this returns a list of lists of
         integers representing
          the Pascal’s triangle of n(no of rows, integer)
         empty list returned if  n <= 0
    """
    # if n is less than or equal to 0 and empty list of ints is returned
    if n <= 0:
        return []
    pascaltri = [[1]]  # first row starts with 1 initialized
    for p in range(1, n):
        row = [1]  # the specific row(p) initialized to start with 1
        for k in range(1, p):
            row.append(pascaltri[p - 1][k - 1] + pascaltri[p - 1][k])
        row.append(1)  # 1 is appended as last element to row always
        pascaltri.append(row)  # row added to overall pascall triangle
    return pascaltri
