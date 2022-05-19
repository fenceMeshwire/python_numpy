#!/usr/bin/env python3

# Python 3.9.7

# 07_numpy_array_split.py

# Dependency
import numpy as np

a = [3, 4, 5, 6, 10, 12, 14, 21, 24, 27]

# Two splitting points [4, 7], three resulting arrays a1, a2, a3
a1, a2, a3 = np.split(a, [4, 7]) 

print(a1)   # [3 4 5 6]
print(a2)   # [10 12 14]
print(a3)   # [21 24 27]

b = np.arange(20)
# Four splitting points [4, 7, 10, 15], five resulting arrays
np.split(b, [4, 7, 10, 15])

matrix = np.arange(25).reshape((5, 5)) # Generate a 5x5-matrix with values from 0-24
print(matrix)

upper, lower = np.vsplit(matrix, [2]) # Split matrix at second row
print(upper)
print(lower)

left, right = np.hsplit(matrix, [3]) # Split matrix at third column
print(left)
print(right)

# Further split into upper left and upper right
upper_left, upper_right = np.hsplit(upper, [2])
print(upper_left)
print(upper_right)

# Further split into lower left and lower right
lower_left, lower_right = np.hsplit(lower, [4])
print(lower_left)
print(lower_right)
