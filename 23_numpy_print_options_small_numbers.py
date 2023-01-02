#!/usr/bin/env python3

# Python 3.9.5

# 23_numpy_print_options_small_numbers.py

# Purpose: When visualizing a result, show very small numbers as zero.
#          This is e.g. useful, when calculating with matrices.

# Dependency
import numpy as np

np.set_printoptions(precision=3, suppress=True)

matrix = np.random.randn(3, 3)  # (3 x 3) matrix

matrix = matrix.T.dot(matrix)   # Dot product matrix and transposed matrix
matrix.dot(inv(matrix))         # Dot product of the above result with the inverted above result

print(matrix)                   # Result will be the (3 x 3) identity matrix.
