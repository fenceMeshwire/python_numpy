#!/usr/bin/env python3

# Python 3.9.7

# 02_numpy_array_indexing.py

#     Indexing of a two-dimensional array
# 
#                       axis 1 ->
#                       col-0   col-1   col-2
#     axis 0    row-0   0.0     0.1     0.2
#        |      row-1   1.0     1.1     1.2
#        V      row-2   2.0     2.1     2.2

# Dependency
import numpy as np

np.random.seed(10) # seed for reproducibility

a = np.random.randint(10, size=4) # One-dimensional array
b = np.random.randint(10, size=(3, 4)) # Two-dimensional array

# Accessing elements in an one-dimensional array:
a[0]            # Access first element
a[3]            # Access fourth element
a[-1]           # Access last element
a[-2]           # Access penultimate element

# Access elements in a multidimensional array:
b[0, 0]         # Access the value of the first row, first column
b[2, 0]         # Access the value of the third row, first column
b[2, -1]        # Access the value of the third row and the last column

# Modifing values by using the index notation (row, column)
b[0, 0] = 12    # Access and change the value of the first row, first column
b               # Show the change result
