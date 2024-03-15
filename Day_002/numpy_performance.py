#!/usr/bin/env python3
"""
Python Module that uses the Numpy Library to perform
element-wise addition and multiplication
"""

import numpy as np
import time


def numpy_time():
    """
    Calculate the time taken for element-wise addition and multiplication
    using NumPy arrays.

    Returns:
        tuple: tuple containing time taken for addition and multiplication.
    """
    # Creating a large NumPy array
    numpy_array = np.array([[i for i in range(1000)] for _ in range(1000)])

    # Element-wise addition using NumPy arrays
    start_time = time.time()
    numpy_array_sum = numpy_array + 1
    numpy_array_time_addition = time.time() - start_time

    # Element-wise multiplication using NumPy arrays
    start_time = time.time()
    numpy_array_product = numpy_array * 2
    numpy_array_time_multiplication = time.time() - start_time

    return numpy_array_time_addition, numpy_array_time_multiplication


if __name__ == "__main__":
    numpy_addition_time, numpy_multiplication_time = numpy_time()

# print("NumPy array addition time:", numpy_addition_time)
# print("NumPy array multiplication time:", numpy_multiplication_time)
