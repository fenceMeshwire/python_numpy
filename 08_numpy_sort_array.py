#!/usr/bin/env python3

# Python 3.9.7

# # Dependency
import numpy as np

A = np.array([1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2])
n = 3

# Get the n-smallest values:
idx = np.argpartition(A, n)
print(A[idx[:n]])

# Get the n-largest values
idx = np.argpartition(A, -n)
print(A[idx[-n:]])
