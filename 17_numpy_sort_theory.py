#!/usr/bin/env python3

# Python 3.9.5

# 17_numpy_sort_theory.py

# Dependency
import numpy as np

a = np.array([1, 6, 3, 2, 8, 4, 9, 10, 7, 5])

# Sort an unsorted array with np.sort(a)
print(np.sort(a))

# Get the original indices in their new sorted order
# by using np.argsort(a)
print(np.argsort(a))

#   Axis 1
#   -------->
# | 3   6   2
# | 6   1   5
# v 9   0   1
# 
# Axis 0

# Sort Axis 0:
#   3   0   1
#   6   1   2
#   9   6   5

# Sort Axis 1
#   2   3   6
#   1   5   6
#   0   1   9

# The array has two axes: axis 0 (rows) and axis 1 (columns)
# Vertical sorting takes place along axis 0
# Horizontal sorting takes place along axis 1
