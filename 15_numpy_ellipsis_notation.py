#!/usr/bin/env python3

# Python 3.9.5

# 15_numpy_ellipsis_notation.py

# Dependency
import numpy as np

# Data
matrices = np.arange(27).reshape((3, 3, 3))
print(matrices)

# Change all columns of all matrices, if 3 columns then indeces are 0, 1, 2
matrices = np.arange(27).reshape((3, 3, 3))
matrices[:, :, 0] = matrices_ones
print(matrices)

# Change all rows of all matrices, if 3 rows then indeces are 0, 1, 2
matrices = np.arange(27).reshape((3, 3, 3))
matrices[:, 0, :] = matrices_ones
print(matrices)

# Change selected matrix, if 3 x 3 matrices then indeces are: 0, 1, 2
matrices = np.arange(27).reshape((3, 3, 3))
matrices[0, :, :] = matrices_ones # First matix: 0
print(matrices)
