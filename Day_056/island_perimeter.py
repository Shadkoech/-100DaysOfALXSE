#!/usr/bin/python3
"""Module that calculates the perimeter of a single island in a grid"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    Args:
        grid (list of list (int)): 2D array representing the grid where:
                - 0 represents water
                - 1 represents land
    Returns:
        int: The perimeter of the island """

    # Check if grid is empty
    if not grid:
        return 0

    # Initialize the perimeter to zero
    perimeter = 0

    # Get grid dimensions
    rows = len(grid)
    columns = len(grid[0])

    # Loop over all cells in the grid
    for i in range(rows):
        for j in range(columns):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check if the cell to the left is water or out of bounds
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check if the cell to the right is water or out of bounds
                if j == columns-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check if the cell above is water or out of bounds
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check if the cell below is water or out of bounds
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
