#!/usr/bin/env python3

# Python 3.9.7

# 03_numpy_access_subarrays.py

# Dependency
import numpy as np

np.random.seed(10) # seed for reproducibility

a = np.arange(10)

# [start:stop:step]
a[:5]    # first five elements, step 1
a[5:]    # elements after index 5, step 1
a[4:7]   # middle subarray, step 1. array([4, 5, 6])

a[::2]   # from start to end, step 2; array([0, 2, 4, 6, 8])
a[1::2]  # from start = 1 to end, step 2; array([1, 3, 5, 7, 9])
a[::-1]  # all elements reversed, step -1; array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
a[5::-2] # step -2 from index 5; array([5, 3, 1])

b = np.random.randint(10, size=(3, 4)) # Two-dimensional array

# Multidimensional subarrays:
b
# [rows, columns]
b[:2, :3]      # 2 rows, 3 columns
b[:3, ::2]     # all rows, every 2nd column
b[::-1, ::-1]  # reversing all subarray dimensions
