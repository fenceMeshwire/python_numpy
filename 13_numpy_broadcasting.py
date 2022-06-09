#!/usr/bin/env python3

# Python 3.9.7

# 13_numpy_broadcasting.py

# Dependency
import numpy as np

# Matching rows length:
identity_matrix = np.identity(3)
print(identity_matrix)

single_row_matrix = [0, 0, 1]

result = identity_matrix + single_row_matrix
print(result)

# Not matching row length:
identity_matrix = np.identity(3)
coefficient = 2

result = identity_matrix * coefficient
print(result)
