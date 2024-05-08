# Day_056

- #100daysofalxse 
- #DoingHardThings
- #DailyGrowth

I handled a number of Python concepts into one assessment question.
The perimeter island puzzle is all about calculating the perimeter of a single island within a grid. The grid is represented by a 2D array of integers, where each cell can either be land (represented by 1) or water (represented by 0). The cells are arranged in rows and columns, forming a rectangular shape

## Concepts needed
`2D Arrays (Matrices):`
- Accessing and iterating over elements in a 2D array.
- Understanding how to navigate through adjacent cells (horizontally and vertically).

`Conditional Logic:`
- Applying conditions to determine whether a cell contributes to the perimeter of the island.

`Counting Techniques:`
- Developing a method to count the edges that contribute to the island’s perimeter.

`Problem-Solving Strategies:`
- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

`Python Programming:`
- Nested loops for iterating over grid cells.
- Conditional statements to check the status of adjacent cells.

## Question
File:

    - 0-island_perimeter.py
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:
 - grid is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
- grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)