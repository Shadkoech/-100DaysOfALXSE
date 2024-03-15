#!/usr/bin/env python3
"""
Python Module that uses the Numpy Library to perform
element-wise addition and multiplication """

import time


def nestedlist_time():
    """
    Calculate the time taken for element-wise addition and multiplication
    on a large nested list.
    Returns:
        tuple: tuple containing time taken for addition and multiplication.
    """

    # Creating a large nested list
    nested_list = [[i for i in range(1000)] for _ in range(1000)]

    # Element-wise addition using nested lists
    start_time = time.time()
    nested_list_sum = [[elem + 1 for elem in row] for row in nested_list]
    nested_list_time_addition = time.time() - start_time

    # Element-wise multiplication using nested lists
    start_time = time.time()
    nested_list_product = [[elem * 2 for elem in row] for row in nested_list]
    nested_list_time_multiplication = time.time() - start_time

    return nested_list_time_addition, nested_list_time_multiplication


if __name__ == "__main__":
    addition_time, multiplication_time = nestedlist_time()

# print("Nested list addition time:", addition_time)
# print("Nested list multiplication time:", multiplication_time)
