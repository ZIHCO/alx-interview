#!/usr/bin/python3
"""Calculate the island perimeter"""


def island_perimeter(grid):
    """calculate the perimeter of an island"""
    count = 0
    if grid:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if not grid[i - 1][j]:
                        count += 1
                    if not grid[i][j - 1]:
                        count += 1
                    if not grid[i][j + 1]:
                        count += 1
                    if not grid[i + 1][j]:
                        count += 1
    return count
