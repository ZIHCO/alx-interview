#!/usr/bin/python3
"""Calculate the island perimeter"""


def island_perimeter(grid):
    """calculate the perimeter of an island"""
    count = 0
    if grid:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    # try:
                    top = grid[i - 1][j]
                    if not top:
                        count += 1
                    """except Exception:
                        pass
                    try:"""
                    left = grid[i][j - 1]
                    if not left:
                        count += 1
                    """except Exception:
                        pass
                     try:"""
                    right = grid[i][j + 1]
                    if not right:
                        count += 1
                    """except Exception:
                        pass
                    try:"""
                    bottom = grid[i + 1][j]
                    if not bottom:
                        count += 1
                    """except Exception:
                        pass"""
    return count
