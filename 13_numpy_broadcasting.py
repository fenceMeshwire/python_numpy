#!/usr/bin/env python3

# Python 3.9.7

# 13_numpy_broadcasting.py

# Dependency
import numpy as np

# CASE 1: Not matching row length:
identity_matrix = np.identity(3)
coefficient = 2

result = identity_matrix * coefficient
print(result)

# CASE 2: Matching rows length:
identity_matrix = np.identity(3)
print(identity_matrix)

single_row_matrix = [0, 0, 1]

result = identity_matrix + single_row_matrix
print(result)

# CASE 3: If the shapes are incompatible, an exception is raised.
matrix_a = np.array([4, 9, 2, 4])
matrix_b = np.array([6, 1, 7])

result = matrix_a[:, np.newaxis] + matrix_b # correct notation for desired output.
print(result)

try: # Raises a ValueError.
    result = matrix_a + matrix_b
except ValueError as err:
    print(err) # operands could not be broadcast together with shapes (4,) (3,)
