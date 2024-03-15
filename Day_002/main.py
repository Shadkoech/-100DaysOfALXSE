#!/usr/bin/env python3
"""
Main python module that runs the comparison of two functions """

import nestedlist_performance
import numpy_performance


if __name__ == "__main__":
    nested_addition_time, nested_multiplication_time = nestedlist_performance.nestedlist_time()
    print("Nested list addition time:", nested_addition_time)
    print("Nested list multiplication time:", nested_multiplication_time)

    numpy_addition_time, numpy_multiplication_time = numpy_performance.numpy_time()
    print("NumPy array addition time:", numpy_addition_time)
    print("NumPy array multiplication time:", numpy_multiplication_time)
