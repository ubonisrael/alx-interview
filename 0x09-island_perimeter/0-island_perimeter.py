#!/usr/bin/python3
"""Contains the island_perimeter function"""


def island_perimeter(grid):
    """Calculates the perimeter of the island (grid) passed
    as an argument to it
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for n in range(width):
            x = grid[i][n]
            if x == 1:
                if i - 1 >= 0 and grid[i - 1][n] == 0:
                    perimeter += 1
                if i - 1 < 0:
                    perimeter += 1
                if i + 1 < height and grid[i + 1][n] == 0:
                    perimeter += 1
                if i + 1 >= height:
                    perimeter += 1
                if n - 1 >= 0 and grid[i][n - 1] == 0:
                    perimeter += 1
                if n - 1 < 0:
                    perimeter += 1
                if n + 1 < width and grid[i][n + 1] == 0:
                    perimeter += 1
                if n + 1 >= width:
                    perimeter += 1
    return perimeter
