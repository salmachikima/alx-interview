#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for s in range(1, n):
        temp = [1]
        for r in range(len(k[s - 1]) - 1):
            curr = k[s - 1]
            temp.append(k[s - 1][r] + k[s - 1][r + 1])
        temp.append(1)
        k.append(temp)
    return k
