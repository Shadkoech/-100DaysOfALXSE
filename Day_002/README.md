# Day_002

The second day of the #100days of code challenge



## Overview

I came across very interesting concept on Python `Numpy Arrays`.

Numpy arrays are a fundamental data structure provided by the `NumPy` library in python. They are similar to nested lists but come with added features for numerical operations. Numpy is actually written in C and therefore all its complexities are backed intoa simple to use module. On the contrary, python lists are dynamically typed. This forces python to counter check the datatype of each element every time it is put to use. This fact makes Numpy much faster than lists. 


Therefore, when in need to use nested lists in Python, you can as well pick Numpy over it. Numpy arrays offer several advantages of nested lists in the following ways:

- Enhanced efficieny: When dealing with large datasets, Numpy arrays are much better in speed and memory efficiency compared to nested lists. This is because NumPy arrays are homogeneous and contiguous in memory, whereas nested lists can store elements of different types and are not necessarily contiguous.
- Vector operations: Numpy arrays support vectorized operations and that means that it allows developers to perform element-wise arithmetic operations without the need for explicit looping. This improves speed and efficiency
- Rich functionality: NumPy provides a wide range of mathematical functions and methods for array manipulation, such as linear algebra, Fourier transforms, random number generation, and more.



## Task

In order to orchestrate the above observation, I did two separate code snippets using Numpy and Nested arrays that demonstrate element-wise addition and multiplication of large dataset. 
The metric of measurement is the addition time and multiplication time of each instances.

### File 1:
	- nestedlist_performance.py
Contains a function `nestedlist_time` that Calculates the time taken for element-wise addition and multiplication on a large nested list.
Applies nested list concept

### File 2:
	- numpy_performance.py
Contains a function `numpy_time()` that calculates the Calculate the time taken for element-wise addition and multiplication using NumPy arrays.

### File 3:
	- main.py
Main file that imports the two modules and computes their output



## Output

On running the main file that imports the two modules (nestedlist_performance and numpy_performance) the output is as follows:

- `./main.py`

Nested list addition time: 0.10794377326965332
Nested list multiplication time: 0.10654616355895996


NumPy array addition time: 0.002912759780883789
NumPy array multiplication time: 0.0029675960540771484

* It is clear that Python Numpy arrays have an edge over python nested lists



## Application

- When developing systems for Scientific Computing, NumPy is extensively used in fields such as physics, engineering, finance, and bioinformatics for numerical simulations, data analysis, and modeling.
- Machine Learning and Data Analysis: Many machine learning libraries, such as TensorFlow and PyTorch, rely on NumPy arrays for data representation and computation.
- Image and Signal Processing: NumPy arrays are commonly used for processing and analyzing digital images, audio signals, and other types of signals due to their efficiency and array-based operations.
