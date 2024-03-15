#!/usr/bin/env python3
"""
Module that uses the Numpy Library to perform
element-wise addition and multiplication """

import numpy as np
import time


def numpy_time():
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

    print("NumPy array addition time:", numpy_array_time_addition)
    print("NumPy array multiplication time:", numpy_array_time_multiplication)


if __name__ == "__main__":
    numpy_time()
