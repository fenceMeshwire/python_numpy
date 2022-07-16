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

# ---------------------------------------------------------------------------
# Function proposal for the application of the ellipsis notation:
def change_matrix_values(matrices, matrix=None, m=3, r=3, c=3):
    matrices = np.arange(27).reshape((m, r, c))
    matrices_ones = np.ones((3, 3))
    matrices[matrix] = matrices_ones
    return matrices

if __name__ == '__main__':
    matrices = change_matrix_values(matrices, 0)
    print(matrices)
# ---------------------------------------------------------------------------
